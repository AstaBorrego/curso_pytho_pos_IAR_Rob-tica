# Exibe um título na tela para o usuário saber que o programa começou.
print("--- Cadastro de Filmes ---") 

# Criamos uma 'Tupla' chamada 'filmes'. 
# Pense nela como uma gaveta com divisórias numeradas que não pode ser alterada depois de preenchida.
filmes = (
    # O comando input faz o computador parar e esperar o usuário digitar algo.
    # O que for digitado no 1º input vai para a posição 0 da nossa 'gaveta'.
    input('Informe o primeiro filme: '),
    
    # O que for digitado aqui vai para a posição 1.
    input('Informe o segundo filme: '),
    
    # O que for digitado aqui vai para a posição 2.
    input('Informe o terceiro filme: ')
)

# Criamos uma variável chamada 'indice' começando em 0.
# Em programação, quase sempre começamos a contar do zero, não do um.
indice = 0

# O 'while' é um laço de repetição. Ele diz: "Enquanto o indice for menor que o tamanho da lista..."
# len(filmes) conta quantos itens existem na nossa tupla (neste caso, 3).
while indice < len(filmes): 
    
    # Exibe a frase na tela. 
    # O 'f' antes das aspas permite que o Python coloque os valores das variáveis direto no texto.
    # filmes[indice] acessa exatamente o conteúdo que guardamos naquela 'divisória' específica.
    print(f'Na posição {indice} está o filme {filmes[indice]}')
    
    # Somamos 1 ao valor atual do indice. 
    # Isso é fundamental para que o computador passe para o próximo filme e o ciclo não seja infinito.
    indice += 1