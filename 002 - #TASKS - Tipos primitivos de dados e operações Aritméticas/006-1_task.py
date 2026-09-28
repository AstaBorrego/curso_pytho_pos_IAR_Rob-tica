import os  # Importa o módulo 'os' para interagir com o sistema (limpar a tela)

def limpar_terminal():  # Define a função de limpeza
    os.system("cls" if os.name == "nt" else "clear")  # Comando para limpar (Windows ou Linux/Mac)

limpar_terminal()  # Executa a função para garantir que o terminal esteja limpo

# Pede um número ao usuário e converte o texto digitado em número inteiro
numero = int(input('Digite um número para ver a tabuada: '))

# 
# O comando 'for' cria um loop: ele repetirá o que estiver abaixo 10 vezes
# 'range(1, 11)' gera números de 1 até 10 (o 11 é o limite final não incluso)
for multiplicador in range(1, 11): 
    
    # Dentro do loop, 'multiplicador' assume um valor diferente a cada volta (1, 2, 3...)
    # Usamos o 'f-string' para inserir os valores de forma organizada
    # O ':2' dentro das chaves garante que os números fiquem alinhados (reserva 2 espaços)
    print(f'{numero} x {multiplicador:2} = {numero * multiplicador}')

# A partir daqui, o código finaliza após o loop completar 10 voltas
print('FIM! O cérebro agradece o descanso.')