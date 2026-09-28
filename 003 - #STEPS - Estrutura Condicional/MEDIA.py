# Autor: Profº Astarote

# Solicita a primeira nota e converte para decimal (float)
nota1 = float(input('Nota 1: '))
# Solicita a segunda nota e converte para decimal (float)
nota2 = float(input('Nota 2: '))
# Solicita a terceira nota e converte para decimal (float)
nota3 = float(input('Nota 3: '))

# Soma as três notas e divide o resultado total por 3
media = (nota1 + nota2 + nota3) / 3
# Exibe a média final arredondada para apenas uma casa decimal (: .1f)
print(f'A sua média é {media:.1f}')



# Verifica se a nota é 7 ou maior para aprovação
if media >= 7:
    # Caso a condição acima seja verdadeira, imprime "APROVADO!"
    print('APROVADO!')
# Se não for 7, verifica se a nota está entre 5 e 6.9
elif media < 7 and media >= 5:
    # Caso a condição esteja no intervalo, imprime "RECUPERAÇÃO!"
    print('RECUPERAÇÃO!')
# Se a média for menor que 5, cai no caminho final (else)
else:
    # Imprime "REPROVADO!" caso nenhuma das anteriores seja atendida
    print('REPROVADO!')