# Autor: Profº Astarote

# Criamos uma "Tupla" (uma lista que não muda), onde cada posição guarda um nome.
# A posição 0 é o "Inválido", e as posições 1 a 7 são os dias da semana.
# O computador começa a contar do 0, por isso o "Inválido" ocupa esse lugar.
diasSemana = (
    "Inválido",
    "domingo",
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
)

# Pedimos ao usuário um número e transformamos o texto digitado em número inteiro (int).
dia = int(input("INFORME UM NÚMERO DE 1 - 7: "))


# O 'if' faz uma checagem de segurança:
# Se o número for menor ou igual a 0 OU maior que 7, o usuário errou a digitação.
if dia <= 0 or dia > 7:
    # Se o erro aconteceu, imprimimos a posição 0 (a palavra "Inválido").
    print(diasSemana[0])
else:
    # Se o número estiver entre 1 e 7, usamos o próprio número como índice
    # para buscar o dia correspondente dentro da nossa tupla.
    # Exemplo: Se o usuário digitou 2, ele busca 'diasSemana[2]', que é "segunda".
    print(diasSemana[dia])
