import sqlite3
from datetime import datetime

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE_URL"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            email TEXT,
            ihtiyac TEXT,
            teslim_tarihi TEXT,
            tarih TEXT NOT NULL
        )
        """
    )
    mevcut_kolonlar = {
        row["name"] for row in db.execute("PRAGMA table_info(leads)").fetchall()
    }
    yeni_kolonlar = {
        "email": "TEXT",
        "ihtiyac": "TEXT",
        "teslim_tarihi": "TEXT",
    }
    for kolon, kolon_tipi in yeni_kolonlar.items():
        if kolon not in mevcut_kolonlar:
            db.execute(f"ALTER TABLE leads ADD COLUMN {kolon} {kolon_tipi}")
    db.commit()
    app.teardown_appcontext(close_db)


def lead_ekle(isim, telefon, email="", ihtiyac="", teslim_tarihi=""):
    tarih = datetime.utcnow().isoformat(timespec="seconds")
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO leads (isim, telefon, email, ihtiyac, teslim_tarihi, tarih)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (isim, telefon, email, ihtiyac, teslim_tarihi, tarih),
    )
    db.commit()
    return cursor.lastrowid


def tum_leadler():
    db = get_db()
    rows = db.execute(
        """
        SELECT id, isim, telefon, email, ihtiyac, teslim_tarihi, tarih
        FROM leads
        ORDER BY id DESC
        """
    ).fetchall()
    return [dict(row) for row in rows]
