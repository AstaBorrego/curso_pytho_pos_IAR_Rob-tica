# importando a função limpar_teerminal
from limpa_prompt import limpar_terminal
# Agora você chama a função
limpar_terminal()

"""
 TAREFA 2: Vizinhos Numéricos
 Vamos descobrir quem vem antes (passado) e quem vem depois (futuro) de um número.
"""

#  PONTO DE PARTIDA: Precisamos de um número para começar.
# 'int' garante que o Python entenda que estamos falando de números (1, 2, 3...) e não de letras.
numero = int(input('Digite um número: '))

# ⬅️ ANTECESSOR (O que vem antes)
# Imagine dar UM PASSO PARA TRÁS na linha numérica. Subtraímos 1.
antecessor = numero - 1

# ➡️ SUCESSOR (O que vem depois)
# Imagine dar UM PASSO PARA FRENTE. Somamos 1.
sucessor = numero + 1

#  RESULTADO FINAL (Método Organizado)
# Usamos as "gavetas" (variáveis) que criamos acima para mostrar a resposta.
print('De acordo com o numero {}, seu antecessor é {} e o sucessor é {}'.format(numero, antecessor, sucessor))

# 🥷🏽 JEITO NINJA (Sem usar gavetas extras)
# Aqui o Python faz a conta "de cabeça" direto dentro do print.
# ⚠️ Atenção: No seu código original havia um pequeno erro (+2). Corrigi para +1 aqui!
print('Atalho: Do número {}, o antecessor é {} e o sucessor é {}'.format(numero, (numero - 1), (numero + 1)))