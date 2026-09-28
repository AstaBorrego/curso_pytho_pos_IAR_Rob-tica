# Limpa o terminal antes de executar o código
import os

# Limpa o terminal antes de executar o código
def limpar_terminal():
    # 'nt' é o nome interno para Windows, caso contrário assume-se Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

""" 
 TAREFA 6: A Máquina de Tabuada Infin""ita
 Por que sofrer decorando se o Python faz isso em milissegundos? 🚀
"""

#  O INPUT: Aqui você escolhe sua "vítima". 
# O número que você digitar vai ser multiplicado até não aguentar mais.
numero = int(input('Digite um número para ver a tabuada: '))

#  A SEQUÊNCIA: Prepare-se para o "Copy-Paste" da alegria!
# DICA TDAH: Repare que o código é quase IDÊNTICO em todas as linhas.
# Só mudamos o multiplicador (1, 2, 3...) e o Python faz a conta no final.

# O truque do '{:2}': Isso diz ao Python "Ei, reserve 2 espaços para esse número".
# Isso serve para o '1' e o '10' ficarem alinhados e seu cérebro não bugar com a bagunça!

print('{} x {:2} = {}'.format(numero, 1, numero * 1))  # Começo leve...
print('{} x {:2} = {}'.format(numero, 2, numero * 2))
print('{} x {:2} = {}'.format(numero, 3, numero * 3))
print('{} x {:2} = {}'.format(numero, 4, numero * 4))  # Já chegamos aqui? Rápido, né?
print('{} x {:2} = {}'.format(numero, 5, numero * 5))
print('{} x {:2} = {}'.format(numero, 6, numero * 6))
print('{} x {:2} = {}'.format(numero, 7, numero * 7))  # A tabuada do 7 é a pior, sorte que o PC faz sozinho.
print('{} x {:2} = {}'.format(numero, 8, numero * 8))
print('{} x {:2} = {}'.format(numero, 9, numero * 9))
print('{} x {:2} = {}'.format(numero, 10, numero * 10)) # FIM! O cérebro agradece o descanso.

