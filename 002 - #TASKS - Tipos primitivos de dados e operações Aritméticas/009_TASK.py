import os
import requests  # Importações sempre no topo do arquivo

# --- Funções ---

def limpar_terminal():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def obter_cotacao_dolar():
    """Busca a cotação do dólar na API."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return float(dados["USDBRL"]["bid"])
    except Exception as e:
        print(f"Ops! Deu erro: {e}")
        return None

# --- Fluxo Principal ---

limpar_terminal()  # Limpa a tela antes de mostrar qualquer resultado

cotacao = obter_cotacao_dolar()

if cotacao:
    valor_em_dolar = 1.50
    valor_em_real = valor_em_dolar * cotacao
    
    print(f"Cotação do Dólar: R$ {cotacao:.2f}")
    print(f"US$ {valor_em_dolar} equivale a R$ {valor_em_real:.2f}")
else:
    print("Não consegui pegar o preço agora.")