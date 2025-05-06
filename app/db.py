import sqlite3
import os

def conectar():
    try:
        # Garante que o diretório do banco existe
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_banco = os.path.join(base_dir, "psinote.db")

        # Conecta ao banco SQLite
        conn = sqlite3.connect(caminho_banco)

        # Cria as tabelas se ainda não existirem
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nascimento DATE,
                telefone TEXT,
                email TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prontuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                texto TEXT,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_paciente TEXT NOT NULL,
                data DATE NOT NULL,
                hora TIME NOT NULL
            )
        """)
        conn.commit()

        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco SQLite: {e}")
        return None
