import streamlit as st
from pagina.pagina_config import configuração_pagina
from pagina.pagina_rodape import rodape
from pagina.pagina_sobre import pagina_sobre
from respostas.respostas_func import gerar_resposta
from time import sleep

configuração_pagina()

def main():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


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
        sleep(3)
        placeholder.empty()

    st.markdown('<div class="titulo_pagina">MordomIA</div>', unsafe_allow_html=True)
    
    # Navegação personalizada na barra lateral
    with st.sidebar:
        st.markdown('<div class="sidebar-title">Navegação</div>', unsafe_allow_html=True)
        st.sidebar.divider()

        conversa = st.button("Conversa")
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        sobre = st.button("Sobre")

    pagina = "Conversa" if st.session_state.get("pagina", "Conversa") == "Conversa" else "Sobre"
    if conversa:
        st.session_state.pagina = "Conversa"
    if sobre:
        st.session_state.pagina = "Sobre"

    # Conteúdo da página selecionada
    if st.session_state.get("pagina", "Conversa") == "Conversa":

        if "historico" not in st.session_state:
            st.session_state.historico = []

        mensagem = st.chat_input("Digite uma mensagem para o MordomIA...")

        if mensagem:
            resposta = gerar_resposta(mensagem)

            st.session_state.historico.append({"role": "user", "content": mensagem})
            st.session_state.historico.append({"role": "assistant", "content": resposta})

        for msg in st.session_state.historico:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    else:
        pagina_sobre()
    rodape()

if __name__ == "__main__":
    main()