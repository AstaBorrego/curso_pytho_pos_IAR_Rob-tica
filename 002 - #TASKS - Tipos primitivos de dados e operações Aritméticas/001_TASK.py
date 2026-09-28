# Limpa o terminal antes de executar o código
import os

# Limpa o terminal antes de executar o código
def limpar_terminal():
    # 'nt' é o nome interno para Windows, caso contrário assume-se Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

# 3. CHAMA A FUNÇÃO
limpar_terminal()
# fim

"""
TASK 1

 OBJETIVO: 
 Criar uma "Calculadora de Soma". 
 O programa vai pedir dois números, juntar os dois e mostrar o resultado.
"""

#  ENTRADA: O programa para e espera você digitar algo.
# Usamos 'int' porque estamos avisando ao Python: "Ei, isso é um NÚMERO inteiro!"
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

# ⚙️ PROCESSAMENTO: Onde a mágica acontece.
# O sinal de '+' faz o trabalho de somar o que guardamos em n1 e n2.
s = n1 + n2

#  SAÍDA: Mostra o resultado final na tela.
# Os '{}' são como "caixas vazias" que serão preenchidas por n1, n2 e s, na ordem.
print("A soma entre {} e {} é igual a {}!".format(n1, n2, s))
