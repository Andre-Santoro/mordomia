import csv
import os

CAMINHO_PASTA = os.path.dirname(__file__)

def carregar_respostas_csv(nome_arquivo):
    respostas = []
    caminho_completo = os.path.join(CAMINHO_PASTA, nome_arquivo)
    try:
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                mensagem = linha["mensagem"].strip().lower()
                resposta = linha["resposta"].strip()
                respostas.append((mensagem, resposta))
    except Exception as e:
        print(f"Erro ao carregar {nome_arquivo}: {e}")
    return respostas

respostas_personalizadas = carregar_respostas_csv("easter_eggs.csv")

def verificar_easter_eggs(mensagem_usuario):
    mensagem_usuario = mensagem_usuario.strip().lower()
    for chave, resposta in respostas_personalizadas:
        if chave == mensagem_usuario:
            return resposta
    return None