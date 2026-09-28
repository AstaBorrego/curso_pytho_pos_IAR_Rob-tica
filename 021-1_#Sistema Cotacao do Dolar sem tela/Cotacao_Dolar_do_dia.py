import os
import requests

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
        print(f"Ops! Deu erro ao buscar a cotação: {e}")
        return None

# --- Fluxo Principal ---

limpar_terminal()

cotacao = obter_cotacao_dolar()

if cotacao:
    try:
        # Adicionada a conversão para float e tratamento de erro de digitação
        entrada = input("Quanto você tem em Dólar (US$)? ")
        valor_em_dolar = float(entrada.replace(',', '.')) # Permite usar vírgula ou ponto
        
        valor_em_real = valor_em_dolar * cotacao
        
        print("-💸-" * 15)
        print(f"Cotação do Dólar hoje: R$ {cotacao:.2f}")
        print(f"US$ {valor_em_dolar:.2f} equivalem a R$ {valor_em_real:.2f}")
        print("-💸-" * 15)
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (ex: 10.50).")
else:
    print("Não foi possível realizar a conversão no momento.")