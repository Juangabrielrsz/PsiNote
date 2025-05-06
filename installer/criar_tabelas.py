import sqlite3
import os

def criar_tabelas():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(os.path.dirname(base_dir), "psinote.db")  # salva fora da pasta installer
    sql_path = os.path.join(base_dir, "criar_tabelas.sql")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(sql_path, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
