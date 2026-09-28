# Criamos uma lista vazia chamada 'nomes' que servirá como nosso depósito.
nomes = []

# Solicitamos ao usuário a quantidade de cadastros e convertemos para número inteiro (int).
quantidade_total = int(input('Quantos nomes você deseja cadastrar? '))

# Criamos uma variável para controlar quantos nomes já foram inseridos, começando em zero.
contador = 0

# O laço 'while' continuará rodando enquanto o nosso contador for menor que a meta definida.
while contador < quantidade_total:
    # Solicitamos o nome para o usuário.
    novo_nome = input(f'Informe o {contador + 1}º nome: ')
    
    # O comando append adiciona o nome digitado dentro da nossa lista 'nomes'.
    nomes.append(novo_nome)
    
    # Aumentamos o contador em 1 para indicar que um cadastro foi concluído.
    contador += 1

# Após sair do laço (quando atingir a meta), exibimos a lista final.
print('\n--- LISTA FINAL DE CADASTRADOS ---')
print(nomes)