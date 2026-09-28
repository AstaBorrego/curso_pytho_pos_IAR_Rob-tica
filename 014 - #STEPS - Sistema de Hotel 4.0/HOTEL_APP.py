from HOTEL_FUNCOES import relatorio, remover, cadastrar
from HOTEL_MENU import menu

opcao = ''
while opcao != 's':
    opcao = menu()
    
    if opcao == 'n':
        cadastrar() # Chamamos direto, pois o banco é gerenciado internamente
    elif opcao == 'r':
        relatorio()
    elif opcao == 'd':
        remover()
    elif opcao == 's':
        print('Saindo do sistema...')
    else:
        input('Opção inválida. Enter para tentar novamente...')