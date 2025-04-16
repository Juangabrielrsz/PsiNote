from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
from styles.styles import apply_button_style, apply_input_style, apply_date_edit_style, apply_label_style
from styles.styles import apply_text_edit_style

import psycopg2

def conectar():
    try:
        conn = psycopg2.connect(
            dbname="psinote",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

class ProntuarioWindow(QWidget):
    def __init__(self, paciente_id, nome_paciente):
        super().__init__()
        self.paciente_id = paciente_id
        self.setWindowTitle(f"Prontuário de {nome_paciente}")
        self.setMinimumSize(500, 400)

        layout = QVBoxLayout()

        self.label = QLabel(f"Prontuário para: {nome_paciente}")
        apply_label_style(self.label)  # Aplicando o estilo ao QLabel

        self.text_edit = QTextEdit()
        apply_text_edit_style(self.text_edit)  # Aplicando o estilo ao QTextEdit

        self.salvar_btn = QPushButton("Salvar Prontuário")
        self.salvar_btn.clicked.connect(self.salvar_prontuario)
        apply_button_style(self.salvar_btn)  # Aplicando o estilo ao QPushButton

        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.salvar_btn)

        self.setLayout(layout)
        self.carregar_prontuario()

    def carregar_prontuario(self):
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT texto FROM prontuarios WHERE paciente_id = %s", (self.paciente_id,))
                resultado = cur.fetchone()
                if resultado:
                    self.text_edit.setText(resultado[0])
                cur.close()
            except Exception as e:
                print(f"Erro ao carregar prontuário: {e}")
            finally:
                conn.close()

    def salvar_prontuario(self):
        texto = self.text_edit.toPlainText()
        conn = conectar()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id FROM prontuarios WHERE paciente_id = %s", (self.paciente_id,))
                if cur.fetchone():
                    cur.execute("UPDATE prontuarios SET texto = %s WHERE paciente_id = %s", (texto, self.paciente_id))
                else:
                    cur.execute("INSERT INTO prontuarios (paciente_id, texto) VALUES (%s, %s)", (self.paciente_id, texto))
                conn.commit()
                QMessageBox.information(self, "Salvo", "Prontuário salvo com sucesso!")
                cur.close()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar prontuário: {e}")
            finally:
                conn.close()
