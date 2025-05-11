import os
import sqlite3

def get_connection():
    # Caminho do banco no diretório de dados do usuário
    appdata_dir = os.path.join(os.getenv("APPDATA"), "PsiNote")
    db_path = os.path.join(appdata_dir, "psinote.db")

    # Garante que o diretório existe
    if not os.path.exists(appdata_dir):
        os.makedirs(appdata_dir)

    # Se o banco não existe, copie o banco da instalação
    install_db_path = os.path.join(os.path.dirname(__file__), 'psinote.db')
    if not os.path.exists(db_path):
        if os.path.exists(install_db_path):
            import shutil
            shutil.copy(install_db_path, db_path)
        else:
            raise FileNotFoundError(f"Banco original não encontrado: {install_db_path}")

    # Retorna a conexão com o banco do AppData
    return sqlite3.connect(db_path)
