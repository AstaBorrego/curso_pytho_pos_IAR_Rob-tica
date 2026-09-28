import tkinter as tk #Está biblioteca do python constroe a janela
import os #

# 1. Configuração da Janela
janela = tk.Tk()
janela.title("Calculadora - AvançaTech") # O Tkinter usará o tamanho deste título para calcular o espaço
janela.resizable(False, False) # Bloqueia o redimensionamento

# 2. Lógica de cálculo (precisa vir antes dos botões para a função funcionar)
def calcular():
    try:
        res = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(res))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# 3. Caixa de entrada
entrada = tk.Entry(janela, font=('Arial', 24), justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# 4. Criando Botões
botoes = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', 'C', '=', '+']
linha, coluna = 1, 0
for b in botoes:
    comando = lambda x=b: entrada.insert(tk.END, x) if x not in ['=', 'C'] else (calcular() if x == '=' else entrada.delete(0, tk.END))
    tk.Button(janela, text=b, font=('Arial', 14), command=comando).grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# --- A MÁGICA DO AJUSTE AUTOMÁTICO ---

# Força o Python a "desenhar" a janela na memória para medir o tamanho real
janela.update_idletasks() 

# Pega o tamanho real que a janela pediu (largura e altura dos botões + título)
largura_janela = janela.winfo_reqwidth()
altura_janela = janela.winfo_reqheight()

# Calcula o centro da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Define a geometria baseada no tamanho calculado
janela.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}')

# Ícone (código anterior mantido)
caminho_base = os.path.dirname(os.path.abspath(__file__))
caminho_icone = os.path.join(caminho_base, "img", "logo.ico")
if os.path.exists(caminho_icone):
    janela.iconbitmap(caminho_icone)

# Executa
janela.mainloop()