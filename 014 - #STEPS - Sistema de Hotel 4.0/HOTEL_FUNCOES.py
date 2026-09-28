import sqlite3 # Importa o módulo para conversar com o banco de dados

# Função para conectar e criar a tabela se ela não existir
def conectar():
    conn = sqlite3.connect('hotel.db') # Cria ou abre o arquivo 'hotel.db'
    cursor = conn.cursor() # Cria o 'cursor', o objeto que executa comandos SQL
    # Cria a tabela de hóspedes com campos específicos
    cursor.execute('''CREATE TABLE IF NOT EXISTS hospedes 
                      (quarto INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, cidade TEXT)''')
    conn.commit() # Salva as alterações no arquivo
    return conn, cursor # Retorna a conexão e o cursor para uso

def cadastrar():
    conn, cursor = conectar() # Abre a conexão com o banco
    try:
        quarto = int(input('Informe o número do quarto: '))
        nome = input('Nome do hóspede: ')
        idade = int(input('Idade: '))
        cidade = input('Cidade: ')
        
        # INSERT insere os dados na tabela. O '?' protege contra erros e ataques
        cursor.execute("INSERT INTO hospedes VALUES (?, ?, ?, ?)", (quarto, nome, idade, cidade))
        conn.commit() # Confirma a inserção no banco
        print('Cadastro realizado com sucesso!')
    except sqlite3.IntegrityError:
        print('Erro: Este número de quarto já está ocupado!')
    finally:
        conn.close() # Sempre fecha o banco para evitar corrupção de dados
    input('Enter para continuar...')

def relatorio():
    conn, cursor = conectar()
    cursor.execute("SELECT * FROM hospedes") # Busca todos os dados da tabela
    hospedes = cursor.fetchall() # Pega todos os resultados encontrados
    
    print('=-=-=-=-= RELATÓRIO DOS QUARTOS =-=-=-=-=')
    if not hospedes:
        print("Nenhum quarto reservado.")
    for h in hospedes:
        # h[0] é quarto, h[1] é nome. Extraímos as colunas pelo índice
        print(f"QUARTO Nº {h[0]} = {h[1].upper()}")
    conn.close()
    input('Enter para continuar...')

def remover():
    conn, cursor = conectar()
    quarto = int(input('Informe o número do quarto para liberar: '))
    # DELETE remove a linha onde o quarto for o número digitado
    cursor.execute("DELETE FROM hospedes WHERE quarto = ?", (quarto,))
    
    # rowcount verifica se algo foi realmente deletado
    if cursor.rowcount > 0:
        print('Quarto liberado com sucesso!')
    else:
        print('Esse quarto já estava disponível.')
    conn.commit()
    conn.close()
    input('Enter para continuar...')