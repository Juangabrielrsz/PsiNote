import sqlite3
import os

def conectar():
    try:
        # Caminho absoluto para o banco dentro da pasta app
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "psinote.db")
        conn = sqlite3.connect(db_path)
        print("✅ Conectado ao banco com sucesso!")

        # Verifica se a tabela 'pacientes' existe
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pacientes'")
        if cursor.fetchone() is None:
            print("⚠️ Tabela 'pacientes' não encontrada. Criando tabelas...")
            criar_tabelas(conn)
        else:
            print("✅ Tabela 'pacientes' encontrada.")
        return conn

    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabelas(conn):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sql_path = os.path.join(base_dir, "..", "installer", "criar_tabelas.sql")

        with open(sql_path, "r", encoding="utf-8") as f:
            script = f.read()
            cursor = conn.cursor()
            cursor.executescript(script)
            conn.commit()
            print("✅ Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")
