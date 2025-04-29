from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self, stacked_widget, main_window):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_usuario = QLabel("Usuário:")
        self.input_usuario = QLineEdit()

        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.botao_login = QPushButton("Entrar")
        self.botao_login.clicked.connect(self.verificar_login)

        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.botao_login)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)
        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        if usuario == "admin" and senha == "1234":
            self.login_sucesso()
        else:
            self.exibir_erro_login()

    def exibir_erro_login(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Erro de Login")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Usuário ou senha inválidos.")
        msg.setInformativeText("Por favor, verifique suas credenciais e tente novamente.")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def login_sucesso(self):
        self.main_window.carregar_abas_pos_login()
