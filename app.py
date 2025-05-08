import streamlit as st
from pagina.pagina_config import configuração_pagina
from pagina.pagina_estilo import estilo_pagina
from pagina.pagina_rodape import rodape
from pagina.pagina_sobre import sobre
from fallback import fallback
from respostas.comandos import verificar_comando
from respostas.respostas_personalizadas import verificar_resposta_personalizada
from respostas.easter_eggs import verificar_easter_eggs
from agentes.supervisor import supervisor
from time import sleep

def main():
    configuração_pagina()
    estilo_pagina()

    if "boas_vindas_exibida" not in st.session_state:
        st.session_state.boas_vindas_exibida = True
        placeholder = st.empty()
        placeholder.markdown(""" ... """, unsafe_allow_html=True)  # Pode manter seu HTML animado aqui
        sleep(1.5)
        placeholder.empty()

    st.markdown("<h1 style='text-align: center; color: white;'>MordomIA</h1>", unsafe_allow_html=True)
    pagina = st.sidebar.radio("Navegação", ("Conversa", "Sobre"))

    if pagina == "Conversa":
        if "historico" not in st.session_state:
            st.session_state.historico = []

        mensagem = st.chat_input("Digite uma mensagem para o MordomIA...")
        if mensagem:
            resposta = (
                verificar_comando(mensagem)
                or verificar_resposta_personalizada(mensagem)
                or verificar_easter_eggs(mensagem)
                or supervisor(mensagem)
                or fallback(mensagem) 
            )
            st.session_state.historico.append({"role": "user", "content": mensagem})
            st.session_state.historico.append({"role": "assistant", "content": resposta})

        for msg in st.session_state.historico:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    elif pagina == "Sobre":
        sobre()
    rodape()

if __name__ == "__main__":
    main()
