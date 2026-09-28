import sqlite3
'''
DB Browser for SQLite: É um programa gratuito e muito fácil de usar.

Baixe em: sqlitebrowser.org

Como usar: Após instalar, abra o programa, clique em "Abrir Banco de Dados" e selecione o arquivo .db que o seu Python gerou (o escola.db do exemplo anterior).

Ele mostrará as abas "Dados da Tabela", onde você verá exatamente o que o INSERT salvou.
'''
banco = sqlite3.connect('banco.db')
sql = banco.cursor()

# id = input('ID do aluno: ')
# novaNota = int(input('Nova nota: '))

# ID -> IDentity (identificador, númerico ou hash e único)
# PK -> Primary Key (Chave-Primária = garantir que o id seja único)
# AI -> Auto Increment (Distribuí o ID)

# Atualiza registros.
# sql.execute(f"UPDATE alunos SET nota = {novaNota} WHERE id = {id}")
# banco.commit()
# print('NOTA ATUALIZADA!')

# Remover registros.
# alunoId = int(input('ID do aluno para remover: '))
# sql.execute(f"DELETE FROM alunos WHERE id = {alunoId}")
# banco.commit()
# print('ALUNO REMOVIDO!')

nome = input('Nome: ')
idade = int(input('Idade: '))
cidade = input('Cidade: ')
curso = input('Curso: ')
nota = int(input('Nota: '))

# Criando uma tabela dentro do SQLITE3


# Conecta ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('escola.db') 
sql = conn.cursor()

# COMANDO FUNDAMENTAL: Cria a tabela se ela ainda não existir
sql.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        cidade TEXT,
        curso TEXT,
        nota REAL
    )
''')

conn.commit() # Salva a criação da tabela no banco
sql.execute(f"INSERT INTO alunos "
            f"(nome, idade, cidade, curso, nota)"
            f"VALUES('{nome}', {idade}, '{cidade}', '{curso}', {nota})")
banco.commit()
print('ALUNO CADASTRADO!')
