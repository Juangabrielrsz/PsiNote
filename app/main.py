import os
import shutil
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# Caminho do banco dentro do instalador
INSTALL_DB_PATH = os.path.join(os.path.dirname(__file__), 'app', 'psinote.db')

# Caminho seguro no AppData para uso com escrita
APPDATA_DIR = os.path.join(os.getenv("APPDATA"), "PsiNote")
USER_DB_PATH = os.path.join(APPDATA_DIR, "psinote.db")

# Cria a pasta se necessário
if not os.path.exists(APPDATA_DIR):
    os.makedirs(APPDATA_DIR)

# Copia o banco apenas se ainda não existir no AppData
if not os.path.exists(USER_DB_PATH):
    shutil.copy(INSTALL_DB_PATH, USER_DB_PATH)

# Conecta ao banco de dados com permissão de escrita
conn = sqlite3.connect(USER_DB_PATH)

# Exemplo simples de janela (substitua com seu código real)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiNote")
        layout = QVBoxLayout()
        label = QLabel(f"Banco carregado de:\n{USER_DB_PATH}")
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
