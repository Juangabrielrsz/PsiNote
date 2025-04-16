from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QTabWidget, QVBoxLayout
from windows.login_window import LoginWindow
from tabs.cadastro_paciente_tab import CadastroPacienteTab
from tabs.calendario_tab import ModernCalendar
from tabs.tabela_pacientes_tab import TabelaPacientesTab

def apply_modern_style(widget):
    """Aplica um tema moderno e consistente para todos os widgets"""
    widget.setStyleSheet("""
        /* Estilos base */
        QWidget {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 13px;
            color: white;  /* Texto branco para contraste */
        }

        /* Estilo para botões */
        QPushButton {
            background-color: #4a6fa5;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            min-width: 100px;
            transition: background-color 0.3s ease;
        }

        QPushButton:hover {
            background-color: #5a8fd8;
        }

        QPushButton:pressed {
            background-color: #3a5a80;
        }

        QPushButton:disabled {
            background-color: #cccccc;
            color: #666666;
        }

        /* Estilo para campos de entrada */
        QLineEdit, QDateEdit, QTextEdit {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            padding: 10px 15px;
            border-radius: 6px;
            selection-background-color: #4a6fa5;
            selection-color: white;
            color: #333333;  /* Texto escuro para contraste */
        }

        QLineEdit:focus, QDateEdit:focus, QTextEdit:focus {
            border: 1px solid #4a6fa5;
            box-shadow: 0 0 0 2px rgba(74, 111, 165, 0.2);
        }

        /* Estilo para labels */
        QLabel {
            color: white;  /* Texto branco */
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 5px;
        }

        /* Estilo para tabelas */
        QTableWidget {
            background-color: #333333;  /* Cor escura de fundo */
            border: 1px solid #d1d1d1;
            border-radius: 6px;
            gridline-color: #eaeaea;
            font-size: 13px;
            color: white;  /* Texto branco */
        }

        QTableWidget::item {
            padding: 8px 12px;
            border-bottom: 1px solid #eaeaea;
            color: white;  /* Texto branco */
        }

        QTableWidget::item:selected {
            background-color: #4a6fa5;
            color: white;  /* Texto branco quando selecionado */
        }

        QHeaderView::section {
            background-color: #4a6fa5;
            color: white;
            padding: 10px;
            font-weight: 500;
            border: none;
        }

        QScrollBar:vertical {
            border: none;
            background: #f5f5f5;
            width: 10px;
        }

        QScrollBar::handle:vertical {
            background: #c1c1c1;
            min-height: 20px;
            border-radius: 5px;
        }
    """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiFlow")
        self.setMinimumSize(800, 600)

        # Configuração do StackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Tela de login
        self.login_window = LoginWindow(self.stacked_widget)
        self.stacked_widget.addWidget(self.login_window)

        # Tela principal do aplicativo
        self.main_app_widget = QWidget()
        main_layout = QVBoxLayout()

        # Adicionando as abas ao QTabWidget
        self.tabs = QTabWidget()
        self.tabs.addTab(ModernCalendar(), "Agenda")  
        self.tabs.addTab(CadastroPacienteTab(), "Cadastro de Pacientes")
        self.tabs.addTab(TabelaPacientesTab(), "Pacientes Cadastrados")

        # Aplicando estilo moderno aos widgets
        apply_modern_style(self.tabs)
        apply_modern_style(self.main_app_widget)

        # Layout da tela principal
        main_layout.addWidget(self.tabs)
        self.main_app_widget.setLayout(main_layout)

        # Adiciona a tela principal ao StackedWidget
        self.stacked_widget.addWidget(self.main_app_widget)
