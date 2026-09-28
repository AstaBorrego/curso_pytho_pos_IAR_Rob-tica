# importando a função limpar_teerminal
from limpa_prompt import limpar_terminal
# Agora você chama a função
limpar_terminal()


""" 
 🧮TAREFA 4: Calculadora de Média
 Vamos descobrir o valor que fica exatamente no MEIO de duas notas.
"""

#  ENTRADA DE DADOS: Notas com vírgula.
# Usamos 'float' porque notas podem ser 7.5, 8.2, etc. (números "flutuantes").
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

# ⚖️ O CÁLCULO DA MÉDIA:
# ⚠️ MUITA ATENÇÃO AQUI: Os parênteses ( ) são obrigatórios!
# Eles dizem ao Python: "Primeiro SOME as notas, depois DIVIDA por 2".
# A barra (/) é o símbolo de divisão.
media = (n1 + n2) / 2

# 📢 RESULTADO:
# O .format() substitui as {} pelas nossas variáveis na ordem certa.
print('A média entre {} e {} é igual a {}'.format(n1, n2, media))