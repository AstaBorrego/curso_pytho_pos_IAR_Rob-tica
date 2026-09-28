# importando a função limpar_teerminal
from limpa_prompt import limpar_terminal
# Agora você chama a função
limpar_terminal()

""" 
 TAREFA 3: O Transformador de Números
 Vamos pegar um número e descobrir o dobro, o triplo e a raiz dele.
"""

# 📥 ENTRADA: O ponto de partida.
# 'n' é a nossa "caixa" principal que guarda o número que você digitar.
n = int(input('Digite um número: '))

# ➕ MULTIPLICAÇÃO (Dobro e Triplo)
# No Python, o asterisco (*) é o sinal de "vezes".
dobro = n * 2
triplo = n * 3

# 📐 RAIZ QUADRADA (O nível avançado)
# Dois asteriscos (**) significam "potência". 
# Elevar a (1/2) é o truque matemático para achar a raiz quadrada!
raizQuadrada = n ** (1/2)

# ---------------------------------------------------------
# RESULTADOS: Mostrando o que descobrimos
# ---------------------------------------------------------

# O .format() coloca os valores dentro das {} na ordem em que aparecem.
print('O dobro de {} vale {}.'.format(n, dobro))
print('O triplo de {} vale {}.'.format(n, triplo))

# DICA: Use ":.2f" dentro das chaves se quiser apenas 2 casas decimais na raiz!
print('A raiz quadrada de {} é {:.2f}.'.format(n, raizQuadrada))8
