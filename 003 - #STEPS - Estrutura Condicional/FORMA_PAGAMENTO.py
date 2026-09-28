# Autor: Profº Astarote

# Pede ao usuário o valor da compra e converte para decimal (float) para permitir centavos
preco = float(input("Informe o valor da compra R$ "))

# Exibe o menu de opções na tela usando três aspas para manter a formatação do texto
print(
    """FORMAS DE PAGAMENTO
        [1] - à vista dinheiro/cheque
        [2] - à vista no cartão
        [3] - 2x no cartão
        [4] - 3x ou mais no cartão
"""
)

# Captura a escolha do aluno e converte para número inteiro (int)
opcao = int(input("Opção:"))

# O bloco de decisão abaixo direciona o computador para a conta matemática correta

if opcao == 1:  # Se a opção for 1, calcula 10% de desconto
    total = preco - (preco * 10 / 100)  # Subtrai 10% do valor total
elif opcao == 2:  # Se a opção for 2, calcula 5% de desconto
    total = preco - (preco * 5 / 100)  # Subtrai 5% do valor total
elif opcao == 3:  # Se a opção for 3, o preço fica igual e divide por 2
    total = preco  # Atribui o preço original ao total
    parcela = total / 2  # Divide o valor total em duas partes iguais
    # Mostra o valor de cada parcela formatando com 2 casas decimais (: .2f)
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!")
elif opcao == 4:  # Se a opção for 4, adiciona 20% de juros
    total = preco + (preco * 20 / 100)  # Soma 20% ao preço original
    qtdeParcelas = int(input("Quantas parcelas?"))  # Pergunta o número de vezes
    valorParcela = total / qtdeParcelas  # Divide o valor com juros pelas parcelas
    # Exibe o resultado das parcelas e o valor final já com juros
    print(
        f"Sua compra será parcelada em {qtdeParcelas}x de R${valorParcela:.2f} e o total é {total}"
    )
else:  # Se o usuário digitar um número fora do menu
    total = preco  # Mantém o preço original sem alterações
    print("Opção de pagamento inválida! Tente novamente!")  # Feedback de erro

# Exibe o resumo final comparando o preço inicial com o preço calculado
print(f"Sua compra de R${preco:.2f} vai custar no final R${total:.2f}")
