# Limpa o terminal
import os  # Sobe ccom todas as funções do Sistema Operacional


# Criando função para limpar o terminal do VSCode
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

    """
    Pegando o valor em real e convertendo para dólar
    """
    real = float(input("Quanto você tem em REAL?"))
    # cotação do dólar 13/03 R$ 5.33
    dolar = real / 5.33

    # O {:.2f} - Converte a casa decimal para dois digitos
    # Exemplo 10.33333333 virá 10.33.

    print("com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
    """
    O .format(real, dolar) pega o valor das variáveis real e dolar e 
    as "encaixa" dentro das chaves {} que estão no texto, na ordem em que elas aparecem.
    """