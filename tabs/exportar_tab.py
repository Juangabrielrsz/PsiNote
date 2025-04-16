from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from utils.pdf_generator import exportar_pacientes_pdf

class ExportarPacientesTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.exportar_btn = QPushButton("Exportar para PDF")
        self.exportar_btn.clicked.connect(lambda: exportar_pacientes_pdf(self))

        layout.addWidget(self.exportar_btn)
        self.setLayout(layout)
