import sqlite3
import os

def conectar():
    try:
        # Caminho absoluto para o banco dentro da pasta app
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "psinote.db")
        conn = sqlite3.connect(db_path)
        print("✅ Conectado ao banco com sucesso!")
        return conn

    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None
