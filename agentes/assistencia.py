from configs import GROQ_API_URL, CHAVE_API_GROQ, GROQ_MODEL
import requests

def responder_assistencia(pergunta: str) -> str:
    prompt = f"Você é um assistente prático. Execute ou oriente sobre a tarefa:\n{pergunta}"
    
    mensagens = [{"role": "user", "content": prompt}]
    
    resposta = requests.post(
        GROQ_API_URL,
        headers={
            "Authorization": f"Bearer {CHAVE_API_GROQ}",
            "Content-Type": "application/json"
        },
        json={
            "model": GROQ_MODEL,
            "messages": mensagens,
            "temperature": 0.4
        }
    )

    return resposta.json()["choices"][0]["message"]["content"]