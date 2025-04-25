import psycopg2
from psycopg2 import sql

def conectar():
    try:
        # Tenta conectar ao banco de dados
        conn = psycopg2.connect(
            dbname="postgres",  # Conectar ao banco padrão para criar o novo banco
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True  # Necessário para executar comandos de criação de banco
        cur = conn.cursor()

        # Cria o banco de dados 'psinote' se ele não existir
        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'psinote'")
        if not cur.fetchone():
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('psinote')))
            print("Banco de dados 'psinote' criado com sucesso!")

        # Conecta ao banco de dados 'psinote'
        conn.close()  # Fecha a conexão temporária
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
