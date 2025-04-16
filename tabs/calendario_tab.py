from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QDateEdit, QTimeEdit, QDialog, QFormLayout, QDialogButtonBox, QMessageBox
from PyQt6.QtGui import QTextCharFormat, QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QPushButton, QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QTimeEdit

class ModernCalendar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # Cria o QCalendarWidget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)  # Corrigido
        self.calendar.setNavigationBarVisible(True)

        self.apply_calendar_style(self.calendar)

        # Cria o botão para adicionar consulta
        self.consulta_btn = QPushButton("Adicionar Consulta")
        self.consulta_btn.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border: none;
                padding: 10px;
                font-size: 12pt;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)
        self.consulta_btn.clicked.connect(self.adicionar_consulta)

        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.consulta_btn)

        self.setLayout(self.layout)

    def apply_calendar_style(self, calendar_widget):
        calendar_widget.setStyleSheet("""
            QCalendarWidget {
                background-color: #ffffff;
                border: none;
                border-radius: 12px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }

            QCalendarWidget QToolButton {
                background-color: #4682B4;
                color: white;
                padding: 10px;
                border-radius: 6px;
            }

            QCalendarWidget QToolButton:hover {
                background-color: #5F9EA0;
            }

            QCalendarWidget::item {
                color: #333333;
                padding: 10px;
                border-radius: 6px;
            }

            QCalendarWidget::item:selected {
                background-color: #1E90FF;
                color: white;
            }

            QCalendarWidget::weekNumber {
                background-color: #f0f0f0;
                color: #4682B4;
            }
        """)

    def adicionar_consulta(self):
        dialog = AdicionarConsultaDialog(self)
        if dialog.exec():
            nome_paciente = dialog.nome_paciente
            data = dialog.data
            hora = dialog.hora

            evento = f"Consulta: {nome_paciente} às {hora.toString('HH:mm')}"
            self.formatar_evento(data, evento)
            QMessageBox.information(self, "Consulta Adicionada", f"Consulta para {nome_paciente} adicionada em {data.toString('dd/MM/yyyy')} às {hora.toString('HH:mm')}.")

    def formatar_evento(self, data, evento):
        format = QTextCharFormat()
        format.setBackground(QColor("#87CEFA"))  # Light blue
        format.setForeground(QColor("#000000"))  # Black text
        self.calendar.setDateTextFormat(data, format)  # Marca o dia no QCalendarWidget

class AdicionarConsultaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Consulta")
        self.layout = QFormLayout()

        self.nome_paciente_input = QLineEdit(self)
        self.layout.addRow("Nome do paciente:", self.nome_paciente_input)

        self.data_input = QDateEdit(self)
        self.layout.addRow("Data da consulta:", self.data_input)

        self.hora_input = QTimeEdit(self)
        self.layout.addRow("Hora da consulta:", self.hora_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def accept(self):
        self.nome_paciente = self.nome_paciente_input.text()
        self.data = self.data_input.date()  # Usando QDate
        self.hora = self.hora_input.time()
        super().accept()
