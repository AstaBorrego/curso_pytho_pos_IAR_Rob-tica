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
 TAREFA 8: Operação Saldão!
 Vamos dar aquela "facada" de 5% de desconto no preço original.
"""

# ENTRADA: O preço na etiqueta.
# 'float' é obrigatório porque dinheiro adora uma vírgula (centavos!).
preco = float(input('Qual é o preço do produto? R$'))

# 📉 O CÁLCULO DO DESCONTO:
# Pense nisso como duas etapas em uma linha só.
# 1. (preco * 5 / 100) -> O Python calcula quanto vale o "cupom" de 5%.
# 2. preco - (...) -> Ele subtrai esse valor do total. É o dinheiro voltando pro bolso!
novo = preco - (preco * 5 / 100)

# ---------------------------------------------------------
# 📢 O ANÚNCIO: Mostrando a economia
# ---------------------------------------------------------

# Lembra do {:.2f}? Ele é o nosso "esteticista". 
# Ele apara as pontas do número para ficar com cara de dinheiro real (2 casas decimais).
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(preco, novo))