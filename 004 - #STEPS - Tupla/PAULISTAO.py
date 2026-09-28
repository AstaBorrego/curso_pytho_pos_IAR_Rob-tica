# Limpa o terminal antes de executar o código
import os

# Limpa o terminal antes de executar o código
def limpar_terminal():
    # 'nt' é o nome interno para Windows, caso contrário assume-se Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

# 3. CHAMA A FUNÇÃO
limpar_terminal()
# fim


# Tupla com os times (agora com 10 posições)
times = ('Santo André', 'Palmeiras', 'São Paulo', 'Red Bull Bragantino',
         'Mirassol', 'Guarani', 'Novorizontino', 'Santos', 'Inter de Limeira', 'Corinthians')

# Fatiamento da tupla: pega do índice 0 até o 4 (o 5 é ignorado)
print(f'Os 5 primeiros são: {times[0:5]}')

# Fatiamento negativo: pega os últimos 4 itens da lista
print(f'Os 4 últimos colocados: {times[-4:]}')

# Organização: gera uma nova lista em ordem alfabética
print(f'Times em Ordem alfabética: {sorted(times)}')

# Input com tratamento: .strip() remove espaços e .title() padroniza as maiúsculas
solicacao = input('Informe o no do time que você quer saber a posição: ').strip().title()

# Estrutura de segurança: Tenta buscar o time, se não encontrar, avisa sem dar erro
try:
    posicao = times.index(solicacao) + 1
    print(f'O time {solitacao} está na {posicao}º posição do campeonato!')
except ValueError:
    print(f'Ops! O time "{solicacao}" não foi encontrado. Verifique se escreveu corretamente.')
    
    