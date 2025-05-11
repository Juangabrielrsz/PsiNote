import os
import shutil
import sqlite3

# Caminhos
INSTALL_DB_PATH = os.path.join(os.path.dirname(__file__), 'psinote.db')
APPDATA_DIR = os.path.join(os.getenv("APPDATA"), "PsiNote")
USER_DB_PATH = os.path.join(APPDATA_DIR, "psinote.db")

# Garante que o banco seja copiado para o AppData, se ainda não estiver lá
def ensure_database_exists():
    if not os.path.exists(APPDATA_DIR):
        os.makedirs(APPDATA_DIR)
    if not os.path.exists(USER_DB_PATH):
        shutil.copy(INSTALL_DB_PATH, USER_DB_PATH)

# Função de conexão centralizada
def get_connection():
    ensure_database_exists()
    try:
        return sqlite3.connect(USER_DB_PATH)
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
