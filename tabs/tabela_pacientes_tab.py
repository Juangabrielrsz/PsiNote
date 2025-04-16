from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QHBoxLayout
from PyQt6.QtCore import Qt
from tabs.prontuario_window import ProntuarioWindow
from styles.styles import apply_table_style  # Supondo que você ainda queira usar esse estilo para a tabela

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


class TabelaPacientesTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        reload_layout = QHBoxLayout()
        self.reload_btn = QPushButton("Recarregar")
        self.reload_btn.clicked.connect(self.carregar_dados)
        reload_layout.addWidget(self.reload_btn, alignment=Qt.AlignmentFlag.AlignRight)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)  # Adicionando uma coluna extra para os botões
        self.tabela.setHorizontalHeaderLabels(["Nome", "Data de Nascimento", "CPF", "Telefone", "Endereço", "E-mail", "Ações"])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Aplicando o estilo à tabela
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
                print(f"Erro ao carregar os dados: {e}")
            finally:
                conn.close()

    def mostrar_dados(self, pacientes):
        self.tabela.setRowCount(len(pacientes))
        for i, paciente in enumerate(pacientes):
            paciente_id = paciente[0]
            for j, dado in enumerate(paciente[1:]):
                item = QTableWidgetItem(str(dado))
                self.tabela.setItem(i, j, item)

            # Botão "Ver Prontuário" na última coluna da tabela (ao lado dos dados)
            btn_prontuario = QPushButton("Ver Prontuário")
            btn_prontuario.clicked.connect(lambda _, pid=paciente_id, nome=paciente[1]: self.abrir_prontuario(pid, nome))

            # Garantir que o botão preencha toda a célula
            btn_prontuario.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;  /* Cor de fundo verde */
                    color: white;               /* Cor do texto */
                    border-radius: 5px;         /* Bordas arredondadas */
                    padding: 0px;               /* Padding ajustado para ocupar toda a célula */
                    font-size: 14px;            /* Tamanho da fonte */
                    border: none;
                    height: 100%;               /* Garantir que o botão ocupe toda a altura da célula */
                    width: 100%;                /* Garantir que o botão ocupe toda a largura da célula */
                }
                QPushButton:hover {
                    background-color: #45a049;  /* Cor de fundo quando passar o mouse */
                }
                QPushButton:pressed {
                    background-color: #388e3c;  /* Cor de fundo quando pressionado */
                }
            """)

            # Colocando o botão ao lado da última coluna da tabela e fazendo-o preencher a célula
            self.tabela.setCellWidget(i, 6, btn_prontuario)

    def abrir_prontuario(self, paciente_id, nome_paciente):
        self.prontuario_window = ProntuarioWindow(paciente_id, nome_paciente)
        self.prontuario_window.show()
