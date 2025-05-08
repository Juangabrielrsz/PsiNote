import sqlite3
import os

def conectar():
    try:
        # Caminho absoluto para o banco existente na raiz do projeto
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.abspath(os.path.join(base_dir, "..", "psinote.db"))

        if not os.path.exists(db_path):
            print(f"❌ Banco de dados não encontrado em {db_path}")
            return None

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
