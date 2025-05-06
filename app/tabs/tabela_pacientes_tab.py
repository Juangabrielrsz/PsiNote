from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QHeaderView, QMessageBox
)
from PyQt6.QtCore import Qt
from tabs.prontuario_window import ProntuarioWindow
from tabs.editar_paciente_window import EditarPacienteWindow
from styles.styles import apply_table_style

import sqlite3


def conectar():
    try:
        conn = sqlite3.connect("psinote.db")  # Cria o arquivo se não existir
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

class TabelaPacientesTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        reload_layout = QHBoxLayout()
        self.reload_btn = QPushButton("Recarregar")
        self.reload_btn.clicked.connect(self.carregar_dados)
        reload_layout.addWidget(self.reload_btn, alignment=Qt.AlignmentFlag.AlignRight)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(8)
        self.tabela.setHorizontalHeaderLabels([
            "Nome", "Nascimento", "CPF", "Telefone",
            "Endereço", "E-mail", "Prontuário", "Editar"
        ])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        apply_table_style(self.tabela)

        layout.addLayout(reload_layout)
        layout.addWidget(self.tabela)
        self.setLayout(layout)

        self.carregar_dados()

    def carregar_dados(self):
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id, nome, nascimento, cpf, telefone, endereco, email FROM pacientes")
                pacientes = cur.fetchall()
                cur.close()
                self.mostrar_dados(pacientes)
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
            finally:
                conn.close()

    def mostrar_dados(self, pacientes):
        self.tabela.setRowCount(len(pacientes))
        for i, paciente in enumerate(pacientes):
            paciente_id = paciente[0]
            for j, dado in enumerate(paciente[1:]):
                item = QTableWidgetItem(str(dado))
                self.tabela.setItem(i, j, item)

            # Botão "Ver Prontuário"
            btn_prontuario = QPushButton("Ver Prontuário")
            btn_prontuario.clicked.connect(lambda _, pid=paciente_id, nome=paciente[1]: self.abrir_prontuario(pid, nome))
            btn_prontuario.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    font-size: 13px;
                    border-radius: 5px;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            self.tabela.setCellWidget(i, 6, btn_prontuario)

            # Botão "Editar"
            btn_editar = QPushButton("Editar")
            btn_editar.clicked.connect(lambda _, pid=paciente_id: self.abrir_editar_paciente(pid))
            btn_editar.setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    font-size: 13px;
                    border-radius: 5px;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
            """)
            self.tabela.setCellWidget(i, 7, btn_editar)

    def abrir_prontuario(self, paciente_id, nome_paciente):
        self.prontuario_window = ProntuarioWindow(paciente_id, nome_paciente)
        self.prontuario_window.show()

    def abrir_editar_paciente(self, paciente_id):
        self.editar_window = EditarPacienteWindow(paciente_id, self)
        self.editar_window.show()

    def excluir_paciente(self, paciente_id):
        reply = QMessageBox.question(
            self, "Confirmar Exclusão",
            "Tem certeza que deseja excluir este paciente?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            conn = conectar()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM pacientes WHERE id = %s", (paciente_id,))
                    conn.commit()
                    cur.close()
                    self.carregar_dados()
                    QMessageBox.information(self, "Sucesso", "Paciente excluído com sucesso!")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir: {e}")
                finally:
                    conn.close()
