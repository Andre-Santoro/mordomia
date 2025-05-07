import csv
import os

CAMINHO_PASTA = os.path.dirname(__file__)

def carregar_respostas_csv(nome_arquivo):
    comandos = []
    caminho_completo = os.path.join(CAMINHO_PASTA, nome_arquivo)
    try:
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                comando = linha["mensagem"].strip().lower()
                resposta = linha["resposta"].strip()
                comandos.append((comando, resposta))
    except Exception as e:
        print(f"Erro ao carregar {nome_arquivo}: {e}")
    return comandos

comandos_disponiveis = carregar_respostas_csv("comandos.csv")

def verificar_comando(mensagem_usuario):
    mensagem_usuario = mensagem_usuario.strip().lower()

    for chave, resposta in comandos_disponiveis:
        if chave == mensagem_usuario:
            return resposta

    return None
