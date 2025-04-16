from fpdf import FPDF
from PyQt6.QtWidgets import QMessageBox
from db import conectar

def exportar_pacientes_pdf(parent=None):
    conn = conectar()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT nome, nascimento, cpf, telefone, endereco, email FROM pacientes")
            pacientes = cur.fetchall()
            cur.close()

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt="Lista de Pacientes", ln=True, align="C")
            pdf.ln(5)

            for paciente in pacientes:
                linha = (
                    f"Nome: {paciente[0]}, "
                    f"Nascimento: {paciente[1]}, "
                    f"CPF: {paciente[2]}, "
                    f"Telefone: {paciente[3]}, "
                    f"Endereço: {paciente[4]}, "
                    f"E-mail: {paciente[5]}"
                )
                pdf.multi_cell(0, 10, linha)
                pdf.ln(1)

            pdf.output("pacientes.pdf")
            QMessageBox.information(parent, "Exportação", "Pacientes exportados com sucesso para PDF!")

        except Exception as e:
            QMessageBox.critical(parent, "Erro", f"Erro ao exportar pacientes: {e}")
        finally:
            conn.close()
    else:
        QMessageBox.critical(parent, "Erro", "Não foi possível conectar ao banco de dados.")
