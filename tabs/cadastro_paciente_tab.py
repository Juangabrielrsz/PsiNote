from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QMessageBox, QDateEdit, QFormLayout)
from PyQt6.QtCore import Qt, QDate, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from db import conectar
from styles.styles import apply_button_style, apply_input_style, apply_date_edit_style, apply_label_style


class CadastroPacienteTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_validators()
        self.setup_connections()

    def setup_ui(self):
        """Configura a interface do usuário"""
        self.layout_principal = QVBoxLayout()
        self.form_layout = QFormLayout()
        
        # Configuração de margens e espaçamento
        self.layout_principal.setContentsMargins(30, 20, 30, 20)
        self.layout_principal.setSpacing(15)
        self.form_layout.setSpacing(10)
        
        # Título
        self.titulo = QLabel("Cadastro de Paciente")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        apply_label_style(self.titulo)
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # Campos de entrada
        self.criar_campos()
        
        # Botões
        self.criar_botoes()
        
        # Adicionando widgets ao layout
        self.layout_principal.addWidget(self.titulo)
        self.layout_principal.addLayout(self.form_layout)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.salvar_btn)
        self.layout_principal.addWidget(self.limpar_btn)
        
        self.setLayout(self.layout_principal)

    def criar_campos(self):
        """Cria e configura os campos de entrada"""
        # Nome
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Digite o nome completo")
        apply_input_style(self.nome_input)
        self.form_layout.addRow("Nome completo:", self.nome_input)
        
        # Data de Nascimento
        self.nascimento_input = QDateEdit()
        self.nascimento_input.setCalendarPopup(True)
        self.nascimento_input.setDisplayFormat("dd/MM/yyyy")
        self.nascimento_input.setDate(QDate.currentDate())
        apply_date_edit_style(self.nascimento_input)
        self.form_layout.addRow("Data de Nascimento:", self.nascimento_input)
        
        # CPF
        self.cpf_input = QLineEdit()
        self.cpf_input.setPlaceholderText("000.000.000-00")
        apply_input_style(self.cpf_input)
        self.form_layout.addRow("CPF:", self.cpf_input)
        
        # Telefone
        self.telefone_input = QLineEdit()
        self.telefone_input.setPlaceholderText("(00) 00000-0000")
        apply_input_style(self.telefone_input)
        self.form_layout.addRow("Telefone:", self.telefone_input)
        
        # Endereço
        self.endereco_input = QLineEdit()
        self.endereco_input.setPlaceholderText("Rua, Número, Bairro, Cidade")
        apply_input_style(self.endereco_input)
        self.form_layout.addRow("Endereço:", self.endereco_input)
        
        # E-mail
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("exemplo@email.com")
        apply_input_style(self.email_input)
        self.form_layout.addRow("E-mail:", self.email_input)

    def criar_botoes(self):
        """Cria e configura os botões"""
        # Botão Salvar
        self.salvar_btn = QPushButton("Salvar Paciente")
        apply_button_style(self.salvar_btn)
        self.salvar_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Botão Limpar
        self.limpar_btn = QPushButton("Limpar Campos")
        apply_button_style(self.limpar_btn)
        self.limpar_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border: 1px solid #ccc;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
        self.limpar_btn.setCursor(Qt.CursorShape.PointingHandCursor)

    def setup_validators(self):
        """Configura validadores para os campos"""
        # Validador para CPF (aceita apenas números e formata automaticamente)
        cpf_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"), self.cpf_input)
        self.cpf_input.setValidator(cpf_validator)
        self.cpf_input.textEdited.connect(self.formatar_cpf)
        
        # Validador para Telefone
        telefone_validator = QRegularExpressionValidator(
            QRegularExpression(r"^\(\d{2}\) \d{4,5}-\d{4}$"), self.telefone_input)
        self.telefone_input.setValidator(telefone_validator)
        self.telefone_input.textEdited.connect(self.formatar_telefone)
        
        # Validador para E-mail
        email_validator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"), 
            self.email_input)
        self.email_input.setValidator(email_validator)

    def setup_connections(self):
        """Configura as conexões de sinais e slots"""
        self.salvar_btn.clicked.connect(self.salvar_paciente)
        self.limpar_btn.clicked.connect(self.limpar_campos)

    def formatar_cpf(self, text):
        """Formata o CPF automaticamente durante a digitação"""
        text = text.replace(".", "").replace("-", "")[:11]
        formatted = ""
        
        for i, char in enumerate(text):
            if i in (3, 6):
                formatted += "."
            if i == 9:
                formatted += "-"
            formatted += char
        
        self.cpf_input.setText(formatted)
        self.cpf_input.setCursorPosition(len(formatted))

    def formatar_telefone(self, text):
        """Formata o telefone automaticamente durante a digitação"""
        text = text.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")[:11]
        formatted = ""
        
        if len(text) >= 2:
            formatted = f"({text[:2]}) "
            text = text[2:]
        
        if len(text) >= 5:
            formatted += f"{text[:5]}-{text[5:]}"
        else:
            formatted += text
        
        self.telefone_input.setText(formatted)
        self.telefone_input.setCursorPosition(len(formatted))

    def validar_campos(self):
        """Valida todos os campos antes do cadastro"""
        campos = {
            "nome": self.nome_input.text().strip(),
            "cpf": self.cpf_input.text().strip(),
            "telefone": self.telefone_input.text().strip(),
            "email": self.email_input.text().strip()
        }
        
        if not campos["nome"]:
            QMessageBox.warning(self, "Aviso", "Por favor, informe o nome do paciente.")
            self.nome_input.setFocus()
            return False
        
        if len(campos["cpf"].replace(".", "").replace("-", "")) != 11:
            QMessageBox.warning(self, "Aviso", "CPF inválido. Deve conter 11 dígitos.")
            self.cpf_input.setFocus()
            return False
        
        if campos["email"] and not self.email_input.hasAcceptableInput():
            QMessageBox.warning(self, "Aviso", "Por favor, informe um e-mail válido.")
            self.email_input.setFocus()
            return False
        
        return True

    def salvar_paciente(self):
        """Salva o paciente no banco de dados"""
        if not self.validar_campos():
            return
        
        dados = {
            "nome": self.nome_input.text().strip(),
            "nascimento": self.nascimento_input.date().toString("yyyy-MM-dd"),
            "cpf": self.cpf_input.text().replace(".", "").replace("-", ""),
            "telefone": self.telefone_input.text().replace("(", "").replace(")", "").replace(" ", "").replace("-", ""),
            "endereco": self.endereco_input.text().strip(),
            "email": self.email_input.text().strip()
        }
        
        conn = None
        try:
            conn = conectar()
            if conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO pacientes (nome, nascimento, cpf, telefone, endereco, email)
                        VALUES (%(nome)s, %(nascimento)s, %(cpf)s, %(telefone)s, %(endereco)s, %(email)s)
                    """, dados)
                    conn.commit()
                
                QMessageBox.information(
                    self, 
                    "Cadastro", 
                    "Paciente cadastrado com sucesso!",
                    QMessageBox.StandardButton.Ok
                )
                self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Erro", 
                f"Não foi possível salvar o paciente:\n{str(e)}",
                QMessageBox.StandardButton.Ok
            )
        finally:
            if conn:
                conn.close()

    def limpar_campos(self):
        """Limpa todos os campos do formulário"""
        self.nome_input.clear()
        self.nascimento_input.setDate(QDate.currentDate())
        self.cpf_input.clear()
        self.telefone_input.clear()
        self.endereco_input.clear()
        self.email_input.clear()
        self.nome_input.setFocus()
