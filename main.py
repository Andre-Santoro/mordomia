import streamlit as st
from respostas.comandos import verificar_comando
from respostas.respostas_personalizadas import verificar_resposta_personalizada
from respostas.easter_eggs import verificar_easter_eggs
import requests
import json
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega a chave do arquivo .env

# Configurações da página
st.set_page_config(
    page_title="MordomIA",
    page_icon="🤵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Tela de boas-vindas com animação
if "boas_vindas_exibida" not in st.session_state:
    st.session_state.boas_vindas_exibida = True

    placeholder = st.empty()

    placeholder.markdown("""
        <style>
        .fade-in-text {
            font-size: 36px;
            font-weight: bold;
            color: white;
            opacity: 0.2;
            animation: fadein 1.5s forwards;
            text-align: center;
            margin-top: 200px;
        }

        @keyframes fadein {
            0%   { opacity: 0.2; }
            100% { opacity: 1.0; }
        }

        body {
            background-color: #121212;
        }
        </style>

        <div class="fade-in-text">Bem-vindo ao MordomIA</div>
    """, unsafe_allow_html=True)

    sleep(1.5)
    placeholder.empty()

# Estilos
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom, #1f005c, #5b0060, #870160, #ac255e, #ca485c, #e16b5c, #f39060, #ffb56b);
            color: white;
        }

        /* Estilo do input de mensagem */
        input[type="text"] {
            border-radius: 4px !important;
            border: 1px solid #ccc !important;
            box-shadow: none !important;
            outline: none !important;
        }

        input[type="text"]:focus {
            border: 1px solid #ccc !important;
            box-shadow: none !important;
            outline: none !important;
        }

        /* Rodapé fixo na parte inferior da janela */
        .rodape-container {
            width: 100%;
            position: fixed;
            bottom: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.2);
            text-align: center;
            padding: 10px 0;
            font-size: 12px;
            color: white;
            opacity: 0.7;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown(
    "<h1 style='text-align: center; color: white;'>MordomIA</h1>",
    unsafe_allow_html=True
)

# Navegação
pagina = st.sidebar.radio("Navegação", ("Conversa", "Sobre"))

# Função para chamar a API do Groq
def chamar_groq(mensagem_enviada):
    try:
        api_key = "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"
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
        
        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            return f"Erro: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erro ao processar a solicitação: {str(e)}"

# Página de conversa
if pagina == "Conversa":
    if "historico" not in st.session_state:
        st.session_state.historico = []

    # Campo de entrada acima da conversa
    mensagem = st.chat_input("Digite uma mensagem para o MordomIA...")
    if mensagem:
        resposta = (
            verificar_comando(mensagem)
            or verificar_resposta_personalizada(mensagem)
            or verificar_easter_eggs(mensagem)
            or chamar_groq(mensagem)
        )
        st.session_state.historico.append({"role": "user", "content": mensagem})
        st.session_state.historico.append({"role": "assistant", "content": resposta})

    # Exibir histórico após o input
    for msg in st.session_state.historico:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Página "Sobre"
elif pagina == "Sobre":
    st.markdown("""
        <div class="container">
            <p style="color: white; font-size: 16px;">
                O projeto MordomIA nasceu da ideia de criar um assistente virtual que fosse mais do que apenas funcional — eu queria que ele tivesse personalidade, estilo e uma identidade visual marcante.
                A jornada começou com uma interface simples, evoluindo gradualmente para algo que reflete dedicação, criatividade e muito carinho pelo que fazemos.
            </p>
            <p style="color: white; font-size: 16px;">
                Utilizando tecnologias como Streamlit e Python, e integrando com o modelo Gemma via Ollama, busquei oferecer respostas úteis, inteligentes e com um toque de humor e referências da cultura pop.
                Cada detalhe foi ajustado cuidadosamente: desde o gradiente suave do fundo até os easter eggs escondidos que fazem referência a franquias icônicas.
            </p>
            <p style="color: white; font-size: 16px;">
                Meu objetivo com o MordomIA é trazer funcionalidade ao dia a dia, desde fazer coisas que você peça no seu computador, porém essa versão ficará por aqui. Espero que você se sinta bem-vindo por aqui — e saiba que este é apenas o começo.
                Muito obrigado por me acompanhar até aqui!
            </p>
        </div>
        """, unsafe_allow_html=True)

# Rodapé 
st.markdown("""
<div class="rodape-container">
    MordomIA - Versão Streamlit © 2025
</div>
""", unsafe_allow_html=True)
