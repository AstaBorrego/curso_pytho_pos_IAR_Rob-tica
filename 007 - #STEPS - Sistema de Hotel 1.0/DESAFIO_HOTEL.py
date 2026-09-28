# SISTEMA DE HOTEL: Criando nossa agenda inteligente de quartos!
quartos_reservados = (
    {}
)  # Cria uma "caixa" vazia chamada dicionário para guardar quartos e nomes.
opcao = ""  # Prepara uma variável vazia para começar nossa conversa com o computador.

print("Bem-vindo ao Hotel Python!")  # Exibe uma mensagem de boas-vindas na tela.

# 🔄 O LOOP: Enquanto a opção NÃO for 's', o programa continua rodando sem parar.
while opcao != "s":  # Inicia o laço de repetição que mantém o programa vivo.
    print(
        """       # Inicia a exibição do menu de opções.
    =-=-=-= MENU DO HOTEL =-=-=-= # Título do menu.
    [N] = Nova reserva    # Opção para reservar.
    [D] = Deletar reserva # Opção para cancelar.
    [R] = Relatório       # Opção para listar tudo.
    [S] = Sair            # Opção para fechar.
    """
    )  # Fecha a exibição do menu.

    # Pede uma letra ao usuário e o .lower() garante que mesmo maiúscula, ela vire minúscula.
    opcao = input("Escolha uma opção: ").lower()

    # 🟢 NOVA RESERVA: Verifica se a letra digitada foi 'n'.
    if opcao == "n":
        quarto = int(
            input("Número do quarto: ")
        )  # Pergunta qual quarto ele quer, transformando em número.
        if quarto in quartos_reservados:  # Checa se o quarto já tem alguém reservado.
            print(
                "🫨 Opa! Este quarto já está ocupado. Tente outro."
            )  # Avisa que já tem dono.
        else:  # Se o quarto estiver livre:
            hospede = input("Nome do hóspede: ")  # Pede o nome da pessoa.
            quartos_reservados[quarto] = (
                hospede  # Guarda o nome dentro do dicionário naquele quarto.
            )
            print("🥳🥳 Reserva feita com sucesso!")  # Comemora o sucesso da operação.

    # 🔴 REMOVER RESERVA: Verifica se a letra foi 'd'.
    elif opcao == "d":
        quarto = int(
            input("Qual quarto liberar? ")
        )  # Pede o número do quarto para apagar.
        if quarto in quartos_reservados:  # Verifica se o quarto existe na nossa lista.
            del quartos_reservados[quarto]  # Deleta o par quarto/hospede do dicionário.
            print("🗑️ Reserva cancelada!")  # Confirma que foi deletado.
        else:  # Se o quarto não estiver na lista:
            print("🤨 Quarto não encontrado.")  # Avisa que não tinha reserva ali.

    # 📊 RELATÓRIO: Verifica se a letra foi 'r'.
    elif opcao == "r":
        print("\n--- Lista de Hóspedes ---")  # Imprime um título de cabeçalho.
        for (
            quarto,
            hospede,
        ) in quartos_reservados.items():  # Percorre todo o dicionário um por um.
            print(
                f"Quarto {quarto}: {hospede.upper()}"
            )  # Mostra o quarto e o nome em letras maiúsculas.

    # 🛑 SAÍDA: Verifica se a letra foi 's'.
    elif opcao == "s":
        print("Encerrando sistema... Tchau!")  # Dá tchauzinho para o usuário.

    # ⚠️ OPÇÃO INVÁLIDA: Caso o usuário digite algo que não existe.
    else:
        print(
            "❓ Opção inválida. Tente N, D, R ou S."
        )  # Avisa sobre o erro de digitação.
