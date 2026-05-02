"""
Álbum Virtual — Figurinhas Copa do Mundo 2026

Estados de cada figurinha:
  0 = não tenho   (cinza)
  1 = tenho       (verde)
  2 = repetida    (laranja)

IDs no formato "FRA 10", "BRA 5", "FWC 3", etc.

Como rodar localmente:
    pip install -r requirements.txt
    python app.py
    Acesse: http://localhost:5000
"""

import os
import sqlite3
from flask import Flask, jsonify, render_template, request

from stickers_data import SECTIONS, get_total

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "album.db")


# ── Banco de Dados ────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    # Migra schema antigo (numero INTEGER) para novo (id TEXT) se necessário
    cols = [row[1] for row in conn.execute("PRAGMA table_info(figurinhas)").fetchall()]
    if cols and "numero" in cols:
        conn.execute("DROP TABLE figurinhas")
        conn.commit()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS figurinhas (
            id      TEXT PRIMARY KEY,
            status  INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def get_status_all() -> dict:
    """Retorna {id: status} para todas as figurinhas salvas."""
    conn = get_db()
    rows = conn.execute("SELECT id, status FROM figurinhas").fetchall()
    conn.close()
    return {row["id"]: row["status"] for row in rows}


# ── Rotas ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    status_map = get_status_all()
    total = get_total()

    tenho     = sum(1 for s in status_map.values() if s == 1)
    repetidas = sum(1 for s in status_map.values() if s == 2)
    faltam    = total - tenho - repetidas

    return render_template(
        "index.html",
        sections=SECTIONS,
        status_map=status_map,
        total=total,
        tenho=tenho,
        repetidas=repetidas,
        faltam=faltam,
        pct=round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
    )


@app.route("/api/toggle", methods=["POST"])
def toggle():
    """
    Alterna o estado de uma figurinha.
    Ciclo: não tenho (0) → tenho (1) → repetida (2) → não tenho (0)

    Recebe JSON: { "id": "FRA 10" }
    Retorna JSON: { "id": "FRA 10", "status": 1, "stats": {...} }
    """
    data = request.get_json()
    sticker_id = str(data.get("id", "")).strip()

    if not sticker_id:
        return jsonify({"error": "id obrigatório"}), 400

    conn = get_db()

    row = conn.execute(
        "SELECT status FROM figurinhas WHERE id = ?", (sticker_id,)
    ).fetchone()

    status_atual = row["status"] if row else 0
    novo_status  = (status_atual + 1) % 3

    conn.execute(
        "INSERT INTO figurinhas (id, status) VALUES (?, ?) "
        "ON CONFLICT(id) DO UPDATE SET status = excluded.status",
        (sticker_id, novo_status),
    )
    conn.commit()

    rows = conn.execute("SELECT status FROM figurinhas").fetchall()
    conn.close()

    total     = get_total()
    tenho     = sum(1 for r in rows if r["status"] == 1)
    repetidas = sum(1 for r in rows if r["status"] == 2)
    faltam    = total - tenho - repetidas

    return jsonify({
        "id":     sticker_id,
        "status": novo_status,
        "stats": {
            "total":     total,
            "tenho":     tenho,
            "repetidas": repetidas,
            "faltam":    faltam,
            "pct":       round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
        },
    })


@app.route("/api/stats")
def stats():
    """Estatísticas gerais e por seção."""
    status_map = get_status_all()
    total     = get_total()
    tenho     = sum(1 for s in status_map.values() if s == 1)
    repetidas = sum(1 for s in status_map.values() if s == 2)

    secoes = []
    for sec in SECTIONS:
        ids = [s["id"] for s in sec["stickers"]]
        sec_tenho     = sum(1 for n in ids if status_map.get(n, 0) == 1)
        sec_repetidas = sum(1 for n in ids if status_map.get(n, 0) == 2)
        secoes.append({
            "id":        sec["id"],
            "label":     sec["label"],
            "total":     len(ids),
            "tenho":     sec_tenho,
            "repetidas": sec_repetidas,
            "faltam":    len(ids) - sec_tenho - sec_repetidas,
        })

    return jsonify({
        "total":     total,
        "tenho":     tenho,
        "repetidas": repetidas,
        "faltam":    total - tenho - repetidas,
        "pct":       round((tenho + repetidas) / total * 100, 1) if total > 0 else 0,
        "secoes":    secoes,
    })


@app.route("/api/faltam")
def faltam_lista():
    """Lista das figurinhas que faltam, agrupadas por seção."""
    status_map = get_status_all()
    faltam = []
    for sec in SECTIONS:
        nums_faltando = [
            {"id": s["id"], "label": s["label"], "secao": sec["label"]}
            for s in sec["stickers"]
            if status_map.get(s["id"], 0) == 0
        ]
        if nums_faltando:
            faltam.append({"secao": sec["label"], "emoji": sec["emoji"], "stickers": nums_faltando})
    return jsonify(faltam)


@app.route("/api/repetidas")
def repetidas_lista():
    """Lista das figurinhas repetidas, agrupadas por seção."""
    status_map = get_status_all()
    repetidas = []
    for sec in SECTIONS:
        nums_rep = [
            {"id": s["id"], "label": s["label"], "secao": sec["label"]}
            for s in sec["stickers"]
            if status_map.get(s["id"], 0) == 2
        ]
        if nums_rep:
            repetidas.append({"secao": sec["label"], "emoji": sec["emoji"], "stickers": nums_rep})
    return jsonify(repetidas)


@app.route("/api/reset", methods=["POST"])
def reset():
    """Zera todo o álbum."""
    conn = get_db()
    conn.execute("DELETE FROM figurinhas")
    conn.commit()
    conn.close()
    return jsonify({"ok": True, "message": "Álbum zerado com sucesso"})


# ── Inicialização ─────────────────────────────────────────────────────────────

init_db()

if __name__ == "__main__":
    port  = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
