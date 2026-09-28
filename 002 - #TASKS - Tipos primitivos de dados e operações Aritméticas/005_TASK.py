# importando a função limpar_teerminal
from limpa_prompt import limpar_terminal
# Agora você chama a função
limpar_terminal()


""" 
 TAREFA 5: A Régua Mágica
 Vamos transformar Metros (grandes) em Centímetros e Milímetros (pequenos).
"""

#  ENTRADA: O tamanho original em Metros.
# Usamos 'float' para permitir medidas como 1.5m ou 2.75m.
medida = float(input('Informe uma distância em metros: '))

#  CONVERSÃO: O "Pulo dos Zeros"
# Imagine que estamos dando passos para a direita na régua:

# Para Centímetros (cm): Multiplicamos por 100 (2 zeros).
# Pense em "Cento" = 100.
cm = medida * 100

# Para Milímetros (mm): Multiplicamos por 1000 (3 zeros).
# Pense em "Mil" = 1000.
mm = medida * 1000

# ---------------------------------------------------------
# EXIBIÇÃO: Mostrando a régua completa
# ---------------------------------------------------------

# DICA VISUAL: {:.0f} remove os números depois da vírgula se você quiser um número inteiro.
# {:.2f} mantém duas casas decimais para ser mais preciso.
print('A medida de {}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida, cm, mm))

