# Autor: Profº Astarote

from datetime import date  # Importa a ferramenta que sabe que dia é hoje

anoAtual = date.today().year  # Pega apenas o ano atual (ex: 2026) e guarda na variável

anoNascimento = int(
    input("Informe o ano que você nasceu:")
)  # Pede o ano ao usuário e o converte para número inteiro
idade = (
    anoAtual - anoNascimento
)  # Faz a conta matemática para descobrir a idade aproximada

#
# O fluxo abaixo decide qual mensagem mostrar baseando-se na idade calculada
if idade == 18:  # Verifica se a idade é exatamente igual a 18
    print("Você tem que se alistar esse ANO!")  # Mostra a mensagem se for igual
elif idade < 18:  # Caso não seja 18, verifica se é menor que 18
    falta = 18 - idade  # Calcula quantos anos faltam para chegar nos 18
    print(f"Você deve se alistar em {falta} anos")  # Mostra a previsão do alistamento
else:  # Se a idade não é 18 e não é menor, então só pode ser maior
    falta = idade - 18  # Calcula quantos anos já passaram dos 18
    print(
        f"Você deveria ter se alistado há {falta} anos."  # Mostra quanto tempo passou
        f"Você já foi dispensado?"
    )  # Pergunta de acompanhamento para o usuário
