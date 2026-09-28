import sqlite3

# Conecta ao seu banco
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

# Pede todos os dados da tabela
cursor.execute("SELECT * FROM hospedes")
dados = cursor.fetchall()

print("Dados encontrados no banco:")
for linha in dados:
    print(linha) # Isso vai imprimir uma lista com os dados (ex: (101, 'João', 30, 'SP'))

conn.close()