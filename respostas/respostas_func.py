from respostas.comandos import verificar_comando
from respostas.respostas_personalizadas import verificar_resposta_personalizada
from respostas.easter_eggs import verificar_easter_eggs
from respostas.fallback import fallback
from agentes.supervisor import supervisor

def gerar_resposta(mensagem: str) -> str:
    return (
        verificar_comando(mensagem)
        or verificar_resposta_personalizada(mensagem)
        or verificar_easter_eggs(mensagem)
        or supervisor(mensagem)
        or fallback(mensagem)
    )