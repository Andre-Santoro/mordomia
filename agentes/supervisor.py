from .conversa import responder_conversa
from .assistencia import responder_assistencia

def supervisor(mensagem):
    mensagem_lower = mensagem.lower()

    if any(palavra in mensagem_lower for palavra in ["abrir", "executar", "iniciar"]):
        resposta = responder_assistencia(mensagem)
        if resposta:
            return resposta

    return responder_conversa(mensagem)