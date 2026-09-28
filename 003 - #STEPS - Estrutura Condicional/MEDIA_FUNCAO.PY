# Autor: Profº Astarote

# Cria uma lista vazia que servirá como uma "sacola" para guardar as notas
notas = []

# O 'for i in range(1, 4)' cria um ciclo repetitivo.
# O 'i' começa valendo 1, na próxima volta vale 2, depois 3.
# O 'range(1, 4)' diz ao computador para parar ANTES de chegar no 4.
for i in range(1, 4):
    # Pede a nota ao usuário e a guarda na variável 'valor'
    valor = float(input(f"Digite a nota {i}: "))
    # O 'append' pega o valor digitado e o coloca dentro da nossa "sacola" (lista)
    notas.append(valor)

# A função 'sum' soma todos os valores da lista, e 'len' conta quantos valores existem.
# Dividimos a soma pela quantidade para obter a média.
media = sum(notas) / len(notas)

# Mostra a média formatada com apenas uma casa decimal
print(f"A sua média é {media:.1f}")


# Agora sim, o bloco de decisão completo para classificar o aluno:
if media >= 7:  # Se a nota for 7 ou mais, o aluno está aprovado
    print("APROVADO!")
elif media >= 5:  # Se não for 7, mas for 5 ou mais, está na recuperação
    print("RECUPERAÇÃO!")
else:  # Se a nota for menor que 5, o aluno está reprovado
    print("REPROVADO!")
