from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from database import get_connection  
import os
import shutil
# Caminho original (dentro da pasta do app instalado)
INSTALL_DB_PATH = os.path.join(os.path.dirname(__file__), 'app', 'psinote.db')

# Caminho do banco no AppData
APPDATA_DIR = os.path.join(os.getenv("APPDATA"), "PsiNote")
USER_DB_PATH = os.path.join(APPDATA_DIR, "psinote.db")

# Cria a pasta no AppData se não existir
if not os.path.exists(APPDATA_DIR):
    os.makedirs(APPDATA_DIR)

# Copia o banco se ele ainda não estiver lá
if not os.path.exists(USER_DB_PATH):
    print("Copiando banco para o AppData...")
    shutil.copy(INSTALL_DB_PATH, USER_DB_PATH)
else:
    print("Banco já existe no AppData.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiNote")
        
        conn = get_connection()  # Isso agora cuida da cópia e conexão do banco
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        layout = QVBoxLayout()
        label = QLabel(f"Tabelas no banco:\n{tables}")
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
