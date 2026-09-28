# > DESAFIO 2 - PARTE 1
# Solicita que o usuário digite o nome e armazena na variável 'nome'
nome = input("Informe o seu nome completo: ")

# Exibe uma mensagem de introdução no console
print("Algumas informações interessantes sobre o seu nome completo")
# Pula uma linha em branco para melhorar a organização visual
print()

# Conta e exibe o número total de caracteres, incluindo os espaços
print("Quantidade de Letras com espaço: ", len(nome))
# Remove os espaços usando .replace() e conta o que sobrou (apenas as letras)
print("Quantidade de Letras sem espaço: ", len(nome.replace(" ", "")))
# Converte todas as letras para minúsculas e exibe
print("Nome em minuscula:", nome.lower())
# Converte todas as letras para maiúsculas e exibe
print("Nome em maiscula:", nome.upper())

# Corta a string nos espaços e cria uma lista com cada palavra separada
lista = nome.split(" ")
# Exibe apenas o primeiro item da lista (índice 0), que é o primeiro nome
print(lista[0])

# Localiza a posição do primeiro espaço com .find()
# Usa esse número para fatiar a string do início (0) até o espaço
print(nome[0 : nome.find(" ")])
