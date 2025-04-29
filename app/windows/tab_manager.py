from PyQt6.QtWidgets import QTabWidget
from tabs.cadastro_paciente_tab import CadastroPacienteTab
from tabs.calendario_tab import ModernCalendar
from tabs.tabela_pacientes_tab import TabelaPacientesTab

class TabManager(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(False)  # Se quiser permitir fechar abas, mude para True

    def carregar_abas(self):
        """Adiciona as abas depois que o usuário loga."""
        self.addTab(ModernCalendar(), "Agenda")
        self.addTab(CadastroPacienteTab(), "Cadastro de Pacientes")
        self.addTab(TabelaPacientesTab(), "Pacientes Cadastrados")
