from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QCalendarWidget, QPushButton, QDialog,
    QFormLayout, QLineEdit, QDialogButtonBox, QTimeEdit, QDateEdit,
    QMessageBox, QListWidget, QHBoxLayout, QComboBox, QStyle
)
from PyQt6.QtGui import QTextCharFormat, QColor, QIcon
from PyQt6.QtCore import QDate, QTime
from database import get_connection 

def conectar():
    try:
        conn = get_connection()
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

class ModernCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.eventos_por_data = {}

        self.layout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.clicked.connect(self.exibir_eventos_do_dia)

        self.apply_calendar_style(self.calendar)

        self.consulta_btn = QPushButton(" Adicionar Consulta")
        self.consulta_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder))
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

        self.eventos_lista = QListWidget()
        self.eventos_lista.itemClicked.connect(self.editar_ou_excluir_evento)

        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.consulta_btn)
        self.layout.addWidget(self.eventos_lista)
        self.setLayout(self.layout)

        self.carregar_consultas_do_banco()

    def apply_calendar_style(self, calendar_widget):
        calendar_widget.setStyleSheet("""
            QCalendarWidget {
                background-color: #ffffff;
                border: none;
                border-radius: 12px;
            }
            QCalendarWidget QToolButton {
                background-color: #4682B4;
                color: white;
                padding: 6px;
                margin: 4px;
                border-radius: 6px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #5F9EA0;
            }
            QCalendarWidget::item {
                color: #333333;
                padding: 8px;
                border-radius: 4px;
            }
            QCalendarWidget::item:selected {
                background-color: #1E90FF;
                color: white;
            }
        """)

    def carregar_consultas_do_banco(self):
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT nome_paciente, data, hora FROM consultas")
                for nome, data_str, hora_str in cur.fetchall():
                    qdate = QDate.fromString(data_str, "yyyy-MM-dd")
                    evento = f"{nome} às {hora_str}"
                    if qdate not in self.eventos_por_data:
                        self.eventos_por_data[qdate] = []
                    self.eventos_por_data[qdate].append(evento)
                    self.formatar_evento(qdate)
                self.exibir_eventos_do_dia(QDate.currentDate())
            except Exception as e:
                print(f"Erro ao carregar consultas: {e}")
            finally:
                conn.close()

    def adicionar_consulta(self):
        dialog = AdicionarConsultaDialog(self)
        if dialog.exec():
            nome_paciente = dialog.nome_paciente
            paciente_id = dialog.paciente_id
            data = dialog.data
            hora = dialog.hora

            evento = f"{nome_paciente} às {hora.toString('HH:mm')}"

            conn = conectar()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute("""
                        INSERT INTO consultas (paciente_id, nome_paciente, data, hora)
                        VALUES (?, ?, ?, ?)
                    """, (paciente_id, nome_paciente, data.toString("yyyy-MM-dd"), hora.toString("HH:mm")))
                    conn.commit()
                    QMessageBox.information(self, "Consulta Adicionada", f"Consulta para {nome_paciente} adicionada.")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao salvar no banco de dados: {e}")
                finally:
                    conn.close()

            if data not in self.eventos_por_data:
                self.eventos_por_data[data] = []
            self.eventos_por_data[data].append(evento)
            self.formatar_evento(data)
            self.exibir_eventos_do_dia(data)

    def formatar_evento(self, data):
        format = QTextCharFormat()
        format.setBackground(QColor("#87CEFA"))
        format.setForeground(QColor("#000000"))
        self.calendar.setDateTextFormat(data, format)

    def exibir_eventos_do_dia(self, data):
        self.eventos_lista.clear()
        eventos = self.eventos_por_data.get(data, [])
        if eventos:
            self.eventos_lista.addItems(eventos)
        else:
            self.eventos_lista.addItem("Nenhuma consulta agendada.")

    def editar_ou_excluir_evento(self, item):
        data = self.calendar.selectedDate()
        eventos = self.eventos_por_data.get(data, [])
        evento_str = item.text()
        if evento_str not in eventos:
            return

        nome, hora_str = evento_str.split(" às ")
        dialog = EditarConsultaDialog(nome, hora_str)
        if dialog.exec():
            if dialog.deletar:
                eventos.remove(evento_str)
            else:
                novo_evento = f"{dialog.nome_editado} às {dialog.hora_editada.toString('HH:mm')}"
                eventos[eventos.index(evento_str)] = novo_evento

            if not eventos:
                self.calendar.setDateTextFormat(data, QTextCharFormat())
                del self.eventos_por_data[data]

            self.exibir_eventos_do_dia(data)

class AdicionarConsultaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Consulta")
        self.layout = QFormLayout()

        self.pacientes_combo = QComboBox()
        self.pacientes = self.carregar_pacientes()
        for nome in self.pacientes:
            self.pacientes_combo.addItem(nome)
        self.layout.addRow("Paciente:", self.pacientes_combo)

        self.data_input = QDateEdit()
        self.data_input.setCalendarPopup(True)
        self.data_input.setDate(QDate.currentDate())
        self.layout.addRow("Data da consulta:", self.data_input)

        self.hora_input = QTimeEdit()
        self.layout.addRow("Hora da consulta:", self.hora_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    def carregar_pacientes(self):
        conn = conectar()
        pacientes = {}
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id, nome FROM pacientes")
                for paciente_id, nome in cur.fetchall():
                    pacientes[nome] = paciente_id
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao carregar pacientes: {e}")
            finally:
                conn.close()
        return pacientes

    def accept(self):
        nome = self.pacientes_combo.currentText()
        if not nome:
            QMessageBox.warning(self, "Campo obrigatório", "Por favor, selecione um paciente.")
            return
        self.nome_paciente = nome
        self.paciente_id = self.pacientes[nome]
        self.data = self.data_input.date()
        self.hora = self.hora_input.time()
        super().accept()

class EditarConsultaDialog(QDialog):
    def __init__(self, nome_paciente, hora_str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Consulta")
        self.setMinimumWidth(300)
        self.deletar = False

        layout = QFormLayout()

        self.nome_input = QLineEdit(nome_paciente)
        layout.addRow("Nome do paciente:", self.nome_input)

        self.hora_input = QTimeEdit()
        self.hora_input.setTime(QTime.fromString(hora_str, "HH:mm"))
        layout.addRow("Hora da consulta:", self.hora_input)

        botoes_layout = QHBoxLayout()
        self.salvar_btn = QPushButton(" Salvar")
        self.salvar_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))
        self.excluir_btn = QPushButton(" Excluir")
        self.excluir_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon))

        botoes_layout.addWidget(self.salvar_btn)
        botoes_layout.addWidget(self.excluir_btn)
        layout.addRow(botoes_layout)

        self.setLayout(layout)

        self.salvar_btn.clicked.connect(self.salvar)
        self.excluir_btn.clicked.connect(self.excluir)

    def salvar(self):
        self.nome_editado = self.nome_input.text()
        self.hora_editada = self.hora_input.time()
        if not self.nome_editado:
            QMessageBox.warning(self, "Campo obrigatório", "Por favor, insira o nome do paciente.")
            return
        self.accept()

    def excluir(self):
        confirm = QMessageBox.question(
            self, "Excluir Consulta",
            "Tem certeza que deseja excluir esta consulta?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.deletar = True
            self.accept()
