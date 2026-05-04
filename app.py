"""
Álbum Virtual — Figurinhas Copa do Mundo 2026

Multi-usuário com senha. Configure no Railway/ambiente:
  ALBUM_USERS=joao:minhasenha,amigo:senhadele
  SECRET_KEY=qualquerstring

Acesso:
  /?u=joao   →  pede senha do João
  /?u=amigo  →  pede senha do amigo

Se ALBUM_USERS não estiver definido, qualquer ?u= funciona sem senha.
"""

import os
import re
import sqlite3
from flask import Flask, jsonify, render_template, request, session

from stickers_data import SECTIONS, get_total

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "album-copa-2026-dev")

DB_PATH = os.getenv("DB_PATH", "album.db")

# Lê senhas do env: "joao:senha1,amigo:senha2" → {"joao": "senha1", "amigo": "senha2"}
def _parse_users() -> dict:
    raw = os.getenv("ALBUM_USERS", "")
    users = {}
    for entry in raw.split(","):
        parts = entry.strip().split(":", 1)
        if len(parts) == 2:
            users[parts[0].strip().lower()] = parts[1].strip()
    return users

USERS = _parse_users()


# ── Utilitários ───────────────────────────────────────────────────────────────

def sanitize_user(raw: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9_-]", "", raw or "")[:20]
    return clean.lower() or "default"


def get_user_id() -> str:
    return sanitize_user(request.args.get("u", "default"))


def is_authenticated(user_id: str) -> bool:
    """Retorna True se não houver senha configurada ou se a sessão for válida."""
    if user_id not in USERS:
        return True
    return session.get(f"auth_{user_id}") is True


# ── Banco de Dados ────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cols = [row[1] for row in conn.execute("PRAGMA table_info(figurinhas)").fetchall()]
    if cols and ("numero" in cols or "user_id" not in cols):
        conn.execute("DROP TABLE figurinhas")
        conn.commit()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS figurinhas (
            id      TEXT    NOT NULL,
            user_id TEXT    NOT NULL DEFAULT 'default',
            status  INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (id, user_id)
        )
    """)
    conn.commit()
    conn.close()


def get_status_all(user_id: str) -> dict:
    conn = get_db()
    rows = conn.execute(
        "SELECT id, status FROM figurinhas WHERE user_id = ?", (user_id,)
    ).fetchall()
    conn.close()
    return {row["id"]: row["status"] for row in rows}


# ── Rotas ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    user_id    = get_user_id()
    needs_auth = not is_authenticated(user_id)

    if needs_auth:
        return render_template("index.html",
            sections=[], status_map={}, total=get_total(),
            tenho=0, repetidas=0, faltam=get_total(), pct=0,
            user_id=user_id, needs_auth=True)

    status_map = get_status_all(user_id)
    total      = get_total()
    tenho      = sum(1 for s in status_map.values() if s == 1)
    repetidas  = sum(1 for s in status_map.values() if s == 2)
    faltam     = total - tenho - repetidas

    return render_template("index.html",
        sections=SECTIONS, status_map=status_map,
        total=total, tenho=tenho, repetidas=repetidas,
        faltam=faltam, pct=round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
        user_id=user_id, needs_auth=False)


@app.route("/api/login", methods=["POST"])
def login():
    data     = request.get_json() or {}
    user_id  = sanitize_user(data.get("user_id", ""))
    password = data.get("password", "")

    if user_id not in USERS:
        return jsonify({"ok": True})  # sem senha configurada → libera

    if USERS[user_id] == password:
        session[f"auth_{user_id}"] = True
        return jsonify({"ok": True})

    return jsonify({"ok": False, "error": "Senha incorreta"}), 401


@app.route("/api/toggle", methods=["POST"])
def toggle():
    data       = request.get_json()
    sticker_id = str(data.get("id", "")).strip()
    user_id    = sanitize_user(data.get("user_id", "default"))

    if not sticker_id:
        return jsonify({"error": "id obrigatório"}), 400
    if not is_authenticated(user_id):
        return jsonify({"error": "não autenticado"}), 401

    conn = get_db()
    row  = conn.execute(
        "SELECT status FROM figurinhas WHERE id = ? AND user_id = ?",
        (sticker_id, user_id),
    ).fetchone()

    novo_status = ((row["status"] if row else 0) + 1) % 3

    conn.execute(
        "INSERT INTO figurinhas (id, user_id, status) VALUES (?, ?, ?) "
        "ON CONFLICT(id, user_id) DO UPDATE SET status = excluded.status",
        (sticker_id, user_id, novo_status),
    )
    conn.commit()

    rows      = conn.execute("SELECT status FROM figurinhas WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()
    total     = get_total()
    tenho     = sum(1 for r in rows if r["status"] == 1)
    repetidas = sum(1 for r in rows if r["status"] == 2)

    return jsonify({
        "id": sticker_id, "status": novo_status,
        "stats": {
            "total": total, "tenho": tenho, "repetidas": repetidas,
            "faltam": total - tenho - repetidas,
            "pct": round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
        },
    })


@app.route("/api/faltam")
def faltam_lista():
    user_id = get_user_id()
    if not is_authenticated(user_id):
        return jsonify({"error": "não autenticado"}), 401
    status_map = get_status_all(user_id)
    result = []
    for sec in SECTIONS:
        items = [{"id": s["id"], "label": s["label"]}
                 for s in sec["stickers"] if status_map.get(s["id"], 0) == 0]
        if items:
            result.append({"secao": sec["label"], "emoji": sec["emoji"], "stickers": items})
    return jsonify(result)


@app.route("/api/repetidas")
def repetidas_lista():
    user_id = get_user_id()
    if not is_authenticated(user_id):
        return jsonify({"error": "não autenticado"}), 401
    status_map = get_status_all(user_id)
    result = []
    for sec in SECTIONS:
        items = [{"id": s["id"], "label": s["label"]}
                 for s in sec["stickers"] if status_map.get(s["id"], 0) == 2]
        if items:
            result.append({"secao": sec["label"], "emoji": sec["emoji"], "stickers": items})
    return jsonify(result)


@app.route("/api/reset", methods=["POST"])
def reset():
    data    = request.get_json() or {}
    user_id = sanitize_user(data.get("user_id", "default"))
    if not is_authenticated(user_id):
        return jsonify({"error": "não autenticado"}), 401
    conn = get_db()
    conn.execute("DELETE FROM figurinhas WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})


# ── Inicialização ─────────────────────────────────────────────────────────────

init_db()

if __name__ == "__main__":
    port  = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
