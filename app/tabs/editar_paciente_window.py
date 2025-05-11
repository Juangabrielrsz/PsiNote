from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFormLayout
)
from PyQt6.QtCore import Qt
from database import get_connection 

def conectar():
    try:
        conn = get_connection()
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

class EditarPacienteWindow(QWidget):
    def __init__(self, paciente_id, tabela_pacientes_tab):
        super().__init__()
        self.paciente_id = paciente_id
        self.tabela_pacientes_tab = tabela_pacientes_tab
        self.setWindowTitle("Editar Paciente")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.nome_input = QLineEdit()
        self.nascimento_input = QLineEdit()
        self.cpf_input = QLineEdit()
        self.telefone_input = QLineEdit()
        self.endereco_input = QLineEdit()
        self.email_input = QLineEdit()

        form_layout.addRow(QLabel("Nome:"), self.nome_input)
        form_layout.addRow(QLabel("Nascimento:"), self.nascimento_input)
        form_layout.addRow(QLabel("CPF:"), self.cpf_input)
        form_layout.addRow(QLabel("Telefone:"), self.telefone_input)
        form_layout.addRow(QLabel("Endereço:"), self.endereco_input)
        form_layout.addRow(QLabel("E-mail:"), self.email_input)

        layout.addLayout(form_layout)

        btn_layout = QVBoxLayout()

        self.salvar_btn = QPushButton("Salvar Alterações")
        self.salvar_btn.clicked.connect(self.salvar_alteracoes)
        self.salvar_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        btn_layout.addWidget(self.salvar_btn)

        self.excluir_btn = QPushButton("Excluir Paciente")
        self.excluir_btn.clicked.connect(self.excluir_paciente)
        self.excluir_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        btn_layout.addWidget(self.excluir_btn)

        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.carregar_dados()

    def carregar_dados(self):
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("""
                    SELECT nome, nascimento, cpf, telefone, endereco, email
                    FROM pacientes
                    WHERE id = ?
                """, (self.paciente_id,))
                paciente = cur.fetchone()
                if paciente:
                    self.nome_input.setText(paciente[0])
                    self.nascimento_input.setText(str(paciente[1]))
                    self.cpf_input.setText(paciente[2])
                    self.telefone_input.setText(paciente[3])
                    self.endereco_input.setText(paciente[4])
                    self.email_input.setText(paciente[5])
                cur.close()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
            finally:
                conn.close()

    def salvar_alteracoes(self):
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("""
                    UPDATE pacientes
                    SET nome = ?, nascimento = ?, cpf = ?, telefone = ?, endereco = ?, email = ?
                    WHERE id = ?
                """, (
                    self.nome_input.text(),
                    self.nascimento_input.text(),
                    self.cpf_input.text(),
                    self.telefone_input.text(),
                    self.endereco_input.text(),
                    self.email_input.text(),
                    self.paciente_id
                ))
                conn.commit()
                cur.close()
                QMessageBox.information(self, "Sucesso", "Paciente atualizado com sucesso!")
                self.tabela_pacientes_tab.carregar_dados()
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar alterações: {e}")
            finally:
                conn.close()

    def excluir_paciente(self):
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
                    cur.execute("DELETE FROM pacientes WHERE id = ?", (self.paciente_id,))
                    conn.commit()
                    cur.close()
                    QMessageBox.information(self, "Sucesso", "Paciente excluído com sucesso!")
                    self.tabela_pacientes_tab.carregar_dados()
                    self.close()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir: {e}")
                finally:
                    conn.close()
