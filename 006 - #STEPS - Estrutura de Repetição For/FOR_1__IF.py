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



# Explicando o código abaixo
# O objetivo é encontrar e mostrar apenas números pares.

# --- INÍCIO DO LOOP ---
# range(início, fim, passo) -> Começa em 0, vai até 50, pula de 2 em 2
for numero in range(0, 51, 2):
    
    # --- VERIFICAÇÃO ---
    # O operador % (módulo) verifica se o resto da divisão por 2 é zero
    if numero % 2 == 0:
        
        # --- SAÍDA ---
        # Exibe o número no console se ele for par
        print(numero)

# DICA: Note que o 'range' com passo 2 já garante números pares, 
# tornando o 'if' uma camada extra de segurança técnica.


"""
# explicanco o código

in Lógica Visual :

O in é o endereço: Ele indica o conjunto de dados (a fonte) onde o Python vai trabalhar.
Sem o in, o for não saberia de onde tirar as informações.

Pertencimento: Você pode dizer aos alunos que o in verifica a existência. No for, 
ele garante que a variável (no caso, numero) assuma, um por um, todos os valores que estão 
dentro daquele intervalo ou lista.

Analogia da Fila: * O for é o segurança da porta.

O in é a fila de pessoas.

A variável é o nome de "quem está entrando agora".
"""