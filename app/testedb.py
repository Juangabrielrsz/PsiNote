from database import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabelas = cursor.fetchall()
print("Tabelas no banco:", tabelas)
cursor.close()
conn.close()