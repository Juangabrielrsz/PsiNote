from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,
    QMessageBox, QHBoxLayout, QFileDialog
)
from styles.styles import (
    apply_button_style, apply_label_style, apply_text_edit_style
)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

import sqlite3


def conectar():
    try:
        conn = sqlite3.connect("psinote.db")  # Cria o arquivo se não existir
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

class ProntuarioWindow(QWidget):
    def __init__(self, paciente_id, nome_paciente):
        super().__init__()
        self.paciente_id = paciente_id
        self.nome_paciente = nome_paciente
        self.setWindowTitle(f"Prontuário de {nome_paciente}")
        self.setMinimumSize(500, 400)

        layout = QVBoxLayout()

        self.label = QLabel(f"Prontuário para: {nome_paciente}")
        apply_label_style(self.label)

        self.text_edit = QTextEdit()
        apply_text_edit_style(self.text_edit)

        # Botões
        button_layout = QHBoxLayout()

        self.salvar_btn = QPushButton("Salvar Prontuário")
        self.salvar_btn.clicked.connect(self.salvar_prontuario)
        apply_button_style(self.salvar_btn)

        self.exportar_btn = QPushButton("Exportar PDF")
        self.exportar_btn.clicked.connect(self.exportar_para_pdf)
        apply_button_style(self.exportar_btn)

        button_layout.addWidget(self.salvar_btn)
        button_layout.addWidget(self.exportar_btn)

        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addLayout(button_layout)

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

    def exportar_para_pdf(self):
        texto = self.text_edit.toPlainText()
        if not texto.strip():
            QMessageBox.warning(self, "Vazio", "O prontuário está vazio.")
            return

        # Selecionar local para salvar o arquivo
        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self, "Salvar PDF", f"prontuario_{self.nome_paciente.replace(' ', '_')}.pdf", "PDF Files (*.pdf)"
        )
        if not nome_arquivo:
            return

        try:
            c = canvas.Canvas(nome_arquivo, pagesize=A4)
            width, height = A4
            y = height - 50
            page_number = 1

            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, f"Prontuário de {self.nome_paciente}")
            y -= 30

            c.setFont("Helvetica", 11)
            for linha in texto.split("\n"):
                if y < 100:
                    self._adicionar_rodape(c, width, page_number)
                    c.showPage()
                    y = height - 50
                    page_number += 1
                    c.setFont("Helvetica", 11)
                c.drawString(50, y, linha)
                y -= 20

            # Rodapé da última página
            self._adicionar_rodape(c, width, page_number)
            c.save()

            QMessageBox.information(self, "Exportado", f"Prontuário exportado como:\n{nome_arquivo}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao exportar PDF: {e}")

    def _adicionar_rodape(self, c, width, page_number):
        data = datetime.now().strftime("%d/%m/%Y")
        c.setFont("Helvetica-Oblique", 9)
        c.drawString(50, 30, f"Data de exportação: {data}")
        c.drawRightString(width - 50, 30, f"Página {page_number}")
