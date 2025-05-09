import os 
import requests
import json

def fallback(mensagem_enviada):
    try:
        api_key = os.getenv("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1"

        prompt = (
            "Você é MordomIA, um assistente educado, direto e sempre responde em português. "
            "Fale como um mordomo moderno, mas amigável. "
            "Evite repetir informações. Seja claro e útil. "
            f"O Usuário disse: {mensagem_enviada}"
        )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "Você é um mordomo virtual educado e direto."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        response = requests.post(f"{base_url}/chat/completions", headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            return f"Erro: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erro ao processar a solicitação: {str(e)}"
