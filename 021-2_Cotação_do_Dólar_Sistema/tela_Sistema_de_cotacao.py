import tkinter as tk                # Importa a biblioteca da interface gráfica
from tkinter import messagebox      # Importa o módulo para caixas de mensagem
import requests                     # Importa a biblioteca para requisições web
from PIL import Image, ImageTk      # Importa o Pillow para processar imagens
import os                           # Importa biblioteca para gerenciar arquivos

# --- FUNÇÕES ---

def obter_cotacao_dolar():          # Define função que busca o dólar na web
    url = "https://economia.awesomeapi.com.br/last/USD-BRL" # API do dólar
    try:                            # Inicia bloco de segurança
        resposta = requests.get(url) # Faz a conexão com a API
        dados = resposta.json()      # Converte a resposta para dicionário
        return float(dados["USDBRL"]["bid"]) # Retorna o valor como número
    except:                         # Caso ocorra qualquer erro
        return None                 # Retorna nada se falhar

def converter(event=None):          # Define a função de cálculo
    if cotacao_atual is None:       # Verifica se temos a cotação
        messagebox.showerror("Erro", "Não foi possível obter a cotação.")
        return                      # Encerra se não houver cotação

    try:                            # Tenta converter o texto em número
        valor_dolar = float(entry_valor.get().replace(',', '.')) # Troca vírgula por ponto
        valor_real = valor_dolar * cotacao_atual # Faz a multiplicação
        lbl_resultado.config(text=f"Total: R$ {valor_real:.2f}", fg="green") # Exibe resultado
    except ValueError:              # Caso o usuário digite letras
        messagebox.showwarning("Atenção", "Digite apenas números.") # Exibe alerta

def limpar_tela():                  # Define a função de limpar campos
    entry_valor.delete(0, "end")    # Limpa a caixa de entrada
    entry_valor.insert(0, "Ex: 12.50") # Devolve a dica (placeholder)
    entry_valor.config(fg="gray")   # Coloca a cor da letra como cinza
    lbl_resultado.config(text="Resultado aparece aqui", fg="black") # Reseta o texto do rótulo

def limpar_placeholder(event):      # Limpa a caixa quando clicada
    if entry_valor.get() == "Ex: 12.50": # Se o texto for a dica
        entry_valor.delete(0, "end")     # Apaga o texto
        entry_valor.config(fg="black")   # Muda a letra para preto

def colocar_placeholder(event):     # Devolve a dica se vazia
    if entry_valor.get() == "":     # Se nada foi escrito
        entry_valor.insert(0, "Ex: 12.50") # Coloca o texto de exemplo
        entry_valor.config(fg="gray")    # Muda a letra para cinza

# --- JANELA ---
janela = tk.Tk()                    # Cria a janela principal
janela.title("💰 Cotação do Dólar") # Define o título
janela.resizable(False, False)      # Bloqueia redimensionamento

# Tenta carregar o ícone na pasta img/logo.ico
try:
    caminho_logo = os.path.join("img", "logo.ico") # Cria o caminho do arquivo
    imagem_aberta = Image.open(caminho_logo)       # Abre a imagem com PIL
    img_logo = ImageTk.PhotoImage(imagem_aberta)   # Converte para formato Tkinter
    janela.iconphoto(False, img_logo)              # Aplica o ícone na janela
except Exception as e:              # Se falhar, mostra o motivo no terminal
    print(f"Aviso: Ícone não carregado. Erro: {e}")

# Lógica para centralizar a janela em 25% da tela
largura_tela = janela.winfo_screenwidth()  # Pega largura total
altura_tela = janela.winfo_screenheight()  # Pega altura total
largura_janela = int(largura_tela * 0.25)  # Calcula 25% da largura
altura_janela = int(altura_tela * 0.25)    # Calcula 25% da altura
pos_x = (largura_tela // 2) - (largura_janela // 2) # Calcula X central
pos_y = (altura_tela // 2) - (altura_janela // 2)   # Calcula Y central
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}") # Aplica tamanho e posição

# --- ELEMENTOS ---
cotacao_atual = obter_cotacao_dolar() # Pega cotação ao abrir
texto_cot = f"Cotação hoje: R$ {cotacao_atual:.2f}" if cotacao_atual else "Erro ao buscar cotação"
tk.Label(janela, text=texto_cot, font=("Arial", 12, "bold")).pack(pady=10) # Rótulo do valor

entry_valor = tk.Entry(janela, fg="gray", justify="center") # Campo de entrada
entry_valor.insert(0, "Ex: 12.50") # Valor inicial
entry_valor.bind("<FocusIn>", limpar_placeholder)  # Evento ao clicar dentro
entry_valor.bind("<FocusOut>", colocar_placeholder) # Evento ao clicar fora
entry_valor.pack(pady=5)            # Exibe com margem

btn_frame = tk.Frame(janela)        # Cria grupo de botões
btn_frame.pack(pady=10)             # Exibe grupo

tk.Button(btn_frame, text="Converter", command=converter).pack(side="left", padx=5) # Botão Converter
tk.Button(btn_frame, text="Limpar", command=limpar_tela).pack(side="left", padx=5) # Botão Limpar

lbl_resultado = tk.Label(janela, text="Resultado aparece aqui", font=("Arial", 12)) # Rótulo de resposta
lbl_resultado.pack()                # Exibe o rótulo

janela.bind('<Return>', converter)  # Permite usar Enter para converter
janela.mainloop()                   # Inicia o loop do programa