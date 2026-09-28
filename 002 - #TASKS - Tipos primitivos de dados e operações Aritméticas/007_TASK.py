# Limpa o terminal antes de executar o código
import os

# Limpa o terminal antes de executar o código
def limpar_terminal():
    # 'nt' é o nome interno para Windows, caso contrário assume-se Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

""" 
 TAREFA 7: Operação Viagem para a Disney
 Vamos ver se o seu dinheiro em Reais aguenta o tranco do Dólar!
"""

#  ENTRADA: O que temos no bolso agora.
# 'float' é essencial aqui, porque ninguém tem apenas valores inteiros (cadê os centavos?).
real = float(input('Quanto dinheiro você tem na carteira? R$'))

# A CONVERSÃO: O momento da verdade.
# Imagine que o Dólar é um "pedágio" caro. 
# Para saber quantos dólares cabem no seu real, a gente DIVIDE (/) pelo preço dele.
# Usamos 4.10 porque é o valor fixo que o exercício deu (quem dera fosse esse hoje em dia!).
dolar = real / 4.10

# ---------------------------------------------------------
#  CASA DE CÂMBIO: Mostrando o resultado
# ---------------------------------------------------------

# O {:.2f} é o seu melhor amigo aqui! 
# Ele esconde aquele monte de números infinitos e deixa o dinheiro bonitinho com 2 casas.
# Ex: 10.3333333 virá 10.33. Bem mais limpo para o cérebro, né?
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))