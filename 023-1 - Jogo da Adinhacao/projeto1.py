import random  # Importa biblioteca para gerar números aleatórios

def definir_nivel():
    """Define o limite numérico baseado na dificuldade escolhida."""
    print("\nNíveis de Dificuldade:")
    print("1 - Iniciante (1 a 15)\n2 - Intermediário (1 a 35)\n3 - Avançado (1 a 70)")
    
    try:
        escolha = int(input('Em qual nível deseja jogar? : '))
        # Uso do match-case (disponível no Python 3.10+)
        match escolha:
            case 1: return 15
            case 2: return 35
            case 3: return 70
            case _: 
                print("Opção inválida! Nível 1 selecionado por padrão.")
                return 15
    except ValueError:
        print("Entrada inválida! Usando nível padrão (1 a 15).")
        return 15

def jogar():
    print('='*40)
    print('Este é um jogo produzido pela Nutendo corp.')
    print('='*40)

    jogando = True
    while jogando:
        limite = definir_nivel()                # Chama a função de nível
        alvo = random.randint(1, limite)        # Gera o número secreto aleatório
        tentativas = 0
        palpite = 0

        print(f'\nTente adivinhar meu pensamento! (1 a {limite})')

        while palpite != alvo:
            try:
                palpite = int(input(f'Escolha um número: '))
                tentativas += 1                 # Incremento simplificado

                if palpite < alvo:
                    print('Chutou baixo, tente novamente!')
                elif palpite > alvo:
                    print('Chutou alto, tente novamente!')
                else:
                    print(f'✨ Parabéns! Você acertou em {tentativas} tentativas.')
            except ValueError:
                print("⚠️ Por favor, digite apenas números inteiros!")

        # Verificação de continuidade
        continuar = input('\nDeseja continuar? (s/n): ').strip().lower()
        if continuar != 's':
            print('Que pena, quem sabe em uma próxima. Até logo!')
            jogando = False

# Ponto de entrada do script
if __name__ == "__main__":
    jogar()