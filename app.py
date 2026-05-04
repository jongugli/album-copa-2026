"""
Álbum Virtual — Figurinhas Copa do Mundo 2026

Fluxo:
  /           → tela de login (usuário + senha)
  /album      → álbum do usuário logado
  /gerenciar  → painel para adicionar/remover usuários
                protegido pela variável ADMIN_KEY

Variáveis de ambiente:
  ALBUM_USERS  = joao:senha1,amigo:senha2   (usuários iniciais, opcional)
  ADMIN_KEY    = suasenhaadmin               (para acessar /gerenciar)
  SECRET_KEY   = qualquerstring              (segurança das sessões)
  DB_PATH      = /caminho/album.db           (padrão: album.db)
"""

import os
import re
import sqlite3
from flask import (Flask, jsonify, redirect, render_template,
                   request, session, url_for)

from stickers_data import SECTIONS, get_total

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "album-copa-2026-dev")

DB_PATH    = os.getenv("DB_PATH", "album.db")
ADMIN_KEY  = os.getenv("ADMIN_KEY", "")


# ── Utilitários ───────────────────────────────────────────────────────────────

def sanitize_user(raw: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9_-]", "", raw or "")[:20]
    return clean.lower()


def usuario_logado() -> str | None:
    return session.get("usuario")


# ── Banco de Dados ────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    # Migra tabela de figurinhas se necessário
    cols = [r[1] for r in conn.execute("PRAGMA table_info(figurinhas)").fetchall()]
    if cols and ("numero" in cols or "user_id" not in cols):
        conn.execute("DROP TABLE figurinhas")
        conn.commit()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS figurinhas (
            id      TEXT    NOT NULL,
            user_id TEXT    NOT NULL,
            status  INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (id, user_id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

    # Seed a partir de ALBUM_USERS (não sobrescreve quem já existe)
    for entry in os.getenv("ALBUM_USERS", "").split(","):
        parts = entry.strip().split(":", 1)
        if len(parts) == 2:
            u, p = parts[0].strip().lower(), parts[1].strip()
            if u:
                conn.execute(
                    "INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)",
                    (u, p),
                )
    conn.commit()
    conn.close()


def get_status_all(user_id: str) -> dict:
    conn = get_db()
    rows = conn.execute(
        "SELECT id, status FROM figurinhas WHERE user_id = ?", (user_id,)
    ).fetchall()
    conn.close()
    return {r["id"]: r["status"] for r in rows}


def validar_senha(username: str, password: str) -> bool:
    conn = get_db()
    row = conn.execute(
        "SELECT password FROM usuarios WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return row is not None and row["password"] == password


# ── Rotas principais ──────────────────────────────────────────────────────────

@app.route("/")
def home():
    """Página de login."""
    if usuario_logado():
        return redirect(url_for("album"))
    return render_template("login.html")


@app.route("/album")
def album():
    """Álbum do usuário logado."""
    user_id = usuario_logado()
    if not user_id:
        return redirect(url_for("home"))

    status_map = get_status_all(user_id)
    total      = get_total()
    tenho      = sum(1 for s in status_map.values() if s == 1)
    repetidas  = sum(1 for s in status_map.values() if s == 2)
    faltam     = total - tenho - repetidas

    return render_template("index.html",
        sections=SECTIONS, status_map=status_map,
        total=total, tenho=tenho, repetidas=repetidas,
        faltam=faltam,
        pct=round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
        user_id=user_id,
    )


@app.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("home"))


# ── Gerenciamento de usuários ─────────────────────────────────────────────────

@app.route("/gerenciar")
def gerenciar():
    key = request.args.get("key", "")
    if not ADMIN_KEY or key != ADMIN_KEY:
        return "Acesso negado.", 403

    conn = get_db()
    usuarios = [r["username"] for r in
                conn.execute("SELECT username FROM usuarios ORDER BY username").fetchall()]
    conn.close()
    return render_template("gerenciar.html", usuarios=usuarios, key=key)


@app.route("/api/usuarios/add", methods=["POST"])
def add_usuario():
    key = request.args.get("key", "")
    if not ADMIN_KEY or key != ADMIN_KEY:
        return jsonify({"error": "Acesso negado"}), 403

    data     = request.get_json() or {}
    username = sanitize_user(data.get("username", ""))
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Usuário e senha obrigatórios"}), 400

    conn = get_db()
    existe = conn.execute(
        "SELECT 1 FROM usuarios WHERE username = ?", (username,)
    ).fetchone()
    if existe:
        conn.close()
        return jsonify({"error": "Usuário já existe"}), 409

    conn.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})


@app.route("/api/usuarios/remove", methods=["POST"])
def remove_usuario():
    key = request.args.get("key", "")
    if not ADMIN_KEY or key != ADMIN_KEY:
        return jsonify({"error": "Acesso negado"}), 403

    data     = request.get_json() or {}
    username = sanitize_user(data.get("username", ""))

    conn = get_db()
    conn.execute("DELETE FROM usuarios WHERE username = ?", (username,))
    conn.execute("DELETE FROM figurinhas WHERE user_id = ?", (username,))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})


# ── API do álbum ──────────────────────────────────────────────────────────────

def _require_auth():
    """Retorna user_id ou None se não autenticado."""
    return usuario_logado()


@app.route("/api/login", methods=["POST"])
def api_login():
    data     = request.get_json() or {}
    username = sanitize_user(data.get("username", ""))
    password = data.get("password", "")

    if not username:
        return jsonify({"ok": False, "error": "Usuário obrigatório"}), 400

    if validar_senha(username, password):
        session["usuario"] = username
        return jsonify({"ok": True})

    return jsonify({"ok": False, "error": "Usuário ou senha incorretos"}), 401


@app.route("/api/toggle", methods=["POST"])
def toggle():
    user_id = _require_auth()
    if not user_id:
        return jsonify({"error": "não autenticado"}), 401

    data       = request.get_json()
    sticker_id = str(data.get("id", "")).strip()
    if not sticker_id:
        return jsonify({"error": "id obrigatório"}), 400

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
    user_id = _require_auth()
    if not user_id:
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
    user_id = _require_auth()
    if not user_id:
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
    user_id = _require_auth()
    if not user_id:
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
