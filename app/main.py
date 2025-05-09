import sys
from PyQt6.QtWidgets import QApplication
from windows.main_window import MainWindow
from db import conectar

def verificar_ou_criar_tabelas():
    conn = conectar()
    if conn is None:
        print("Erro ao conectar ao banco.")
        return
    cursor = conn.cursor()

    try:
        # Tenta acessar a tabela 'pacientes'
        cursor.execute("SELECT 1 FROM pacientes LIMIT 1;")
    except Exception as e:
        print("⚠️ Tabela 'pacientes' não encontrada. Criando tabelas...")
        try:
            from app.db import criar_tabelas
            criar_tabelas(conn)
        except Exception as erro_sql:
            print(f"❌ Erro ao criar tabelas: {erro_sql}")
    finally:
        conn.commit()
        conn.close()

if __name__ == "__main__":
    verificar_ou_criar_tabelas()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
