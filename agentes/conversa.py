import requests
from configs import GROQ_API_URL, GROQ_API_KEY, GROQ_MODEL

def responder_conversa(pergunta: str) -> str:
    prompt_base = (
        "Você está conversando com o MordomIA, um mordomo virtual inteligente, educado e direto. "
        "Ele sempre responde em português e com um toque de elegância. "
        "Evita repetições, fala com clareza e objetividade, é gentil e com um humor refinado. "
        "Nunca inventa fatos e não se prolonga desnecessariamente.\n\n"
        f"Usuário: {pergunta}\n"
        "MordomIA:"
    )

    mensagens = [
        {"role": "system", "content": "Você é um mordomo virtual educado e direto."},
        {"role": "user", "content": prompt_base}
    ]

    try:
        resposta = requests.post(
            GROQ_API_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": GROQ_MODEL,
                "messages": mensagens,
                "temperature": 0.7,
                "max_tokens": 1024
            }
        )

        if resposta.status_code == 200:
            return resposta.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"[Erro {resposta.status_code}] {resposta.text}"

    except Exception as e:
        return f"Erro ao tentar se comunicar com a API da Groq: {str(e)}"