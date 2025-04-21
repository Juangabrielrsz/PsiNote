from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Login - PsiFlow")

        layout = QVBoxLayout()

        self.usuario_input = QLineEdit()
        self.usuario_input.setPlaceholderText("Usuário")

        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_btn = QPushButton("Entrar")
        self.login_btn.clicked.connect(self.verificar_login)

        layout.addWidget(QLabel("Bem-vindo ao PsiFlow"))
        layout.addWidget(self.usuario_input)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)

        # Adiciona a funcionalidade de pressionar Enter para logar
        self.senha_input.returnPressed.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.usuario_input.text()
        senha = self.senha_input.text()
        if usuario == "admin" and senha == "123":
            self.stacked_widget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos.")
