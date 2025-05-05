from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QTabWidget, QVBoxLayout
from windows.login_window import LoginWindow
from tabs.cadastro_paciente_tab import CadastroPacienteTab
from tabs.calendario_tab import ModernCalendar
from tabs.tabela_pacientes_tab import TabelaPacientesTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiNote")
        self.setMinimumSize(800, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Tela de login
        self.login_window = LoginWindow(self.stacked_widget, self)
        self.stacked_widget.addWidget(self.login_window)

        # Placeholder para a tela principal
        self.main_app_widget = None

    def carregar_abas_pos_login(self):
        """Cria as abas somente após login com segurança"""
        if self.main_app_widget is None:
            self.main_app_widget = QWidget()
            main_layout = QVBoxLayout()

            self.tabs = QTabWidget()
            self.tabs.addTab(ModernCalendar(), "Agenda")
            self.tabs.addTab(CadastroPacienteTab(), "Cadastro de Pacientes")
            self.tabs.addTab(TabelaPacientesTab(), "Pacientes Cadastrados")

            main_layout.addWidget(self.tabs)
            self.main_app_widget.setLayout(main_layout)

            self.stacked_widget.addWidget(self.main_app_widget)

        # Troca para a tela principal
        self.stacked_widget.setCurrentWidget(self.main_app_widget)
