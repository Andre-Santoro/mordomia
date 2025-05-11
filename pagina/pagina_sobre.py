import streamlit as st

def pagina_sobre():
   st.markdown(""" <div class="container_sobre">
        <p>
            O projeto <strong>MordomIA</strong> nasceu da ideia de criar um assistente virtual que fosse mais do que apenas funcional — eu queria que ele tivesse personalidade, estilo e uma identidade visual marcante.
            A jornada começou com uma interface simples, evoluindo gradualmente para algo que reflete dedicação, criatividade e muito carinho pelo que fazemos.
        </p>
        <p>
            Utilizando tecnologias como <strong>Streamlit</strong> e agentes para a I.A, integrando com o modelo <strong>LLaMA 3 70B via Groq</strong>, MordomIA oferece respostas úteis, inteligentes e (em alguns casos) com um toque de humor e referências.
            Foi dado muito amor a esse mini-projeto (que irá crescer com o decorrer do meu aprendizado!).
        </p>
        <p>
            Meu objetivo com o MordomIA é trazer funcionalidade ao dia a dia, desde fazer coisas que você peça no seu computador, porém essa versão ficará por aqui.
            Espero que você se sinta bem-vindo por aqui — e saiba que este é apenas o começo.
            Muito obrigado por me acompanhar até aqui!
        </p>
    </div> """, unsafe_allow_html=True)