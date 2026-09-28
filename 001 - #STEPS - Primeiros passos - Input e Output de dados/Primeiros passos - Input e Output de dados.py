# Autor: Profº Astarote
# Inicío do códgio que limpa o terminal

import os  # Importa a biblioteca que conversa com o sistema operacional
import platform  # Importa a biblioteca para saber qual sistema você está usando

# Definimos uma função para organizar a limpeza do terminal
def limpar_terminal():
    # O comando 'cls' funciona no Windows. O comando 'clear' funciona no Linux/Mac.
    # Esta linha escolhe o comando certo dependendo do sistema detectado.
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    
    # O comando 'os.system' envia essa instrução para o prompt do sistema.
    os.system(comando)

# Agora, toda vez que você quiser limpar a tela, basta chamar a função abaixo:
limpar_terminal()
print("O terminal foi limpo com sucesso!")
# Fim de código que limpa o terminal

# -*- Algoritimo e Linguagem de Programação -*-
"""
    Primeiros passos - Input e Output de dados
    Prof. Astarote
"""

# Imprime o texto padrão na tela. O print é a forma do Python "falar" com o usuário.
print('Hello, World! Com aspas simples')

#imprime texto com as duplas
print("Hello, World! Com aspas duplas")


# O comentário abaixo explica que textos entre aspas triplas não aparecem no terminal.
"""
  Comentário com mais de uma linha!
"""

# Mostra que podemos misturar aspas duplas dentro de simples e vice-versa.
print('É "Hello World!" que fala?')
print("É 'Hello World!' que fala?")

# Imprime o texto com aspas duplas. O resultado na tela é o mesmo da linha com aspas simples.
print("Hello, World! Com aspas duplas")

# Cria uma "caixa" chamada 'mensagem' e guarda o texto nela.
mensagem = "Hello, World! Armazenado em uma variável"
print(mensagem)  # Mostra o conteúdo da variável na tela.

# Substitui o valor anterior da variável 'mensagem' por um novo texto.
mensagem = "Hello, World! Modificado..."
print(mensagem)

# O 'input' para o programa e espera o usuário escrever algo. O que ele escrever vai para a variável.
mensagem = input("Digite a mensagem: ")
print(mensagem)

# Imprime uma linha em branco para organizar o visual do terminal.
print()

# O '\n' é um código especial que significa "pule uma linha" antes de imprimir.
print("\n", mensagem)

# --- Métodos de Concatenação (Juntar textos e variáveis) ---

# 1. Usa o '+' para somar o texto da variável com um texto novo.
print()
print(mensagem + " Enviado por input")

# 2. Usa a vírgula para separar e o '\n' para pular linha.
print("\nMensagem Enviada por input: ", mensagem)

# 3. Usa o .format(), que coloca o valor da variável dentro das chaves {}.
print("{} > Mensagem enviada com input.".format(mensagem))

# 4. O 'f' (f-string) é o modo mais moderno e fácil de incluir variáveis dentro de textos.
print(f"{mensagem}. *Enviada com input.")

#

### TASK 1
nome = input("Diga o seu nome: ")  # Captura o nome do usuário
print(f"Bem Vindo {nome}!")  # Usa o 'f-string' para exibir o nome capturado

### TASK 2
# Pede as informações de data separadamente
dia = input("Diga apenas o dia do mês que você nasceu: ")
mes = input("Agora diga o mês que você nasceu: ")
ano = input("E por fim, diga o ano que você nasceu: ")
# Exibe todas as informações juntas em uma única frase formatada
print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")
