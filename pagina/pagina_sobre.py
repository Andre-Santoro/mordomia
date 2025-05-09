import streamlit as st

def pagina_sobre():
   st.markdown(""" <div class="container">
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
            </div> """, unsafe_allow_html=True)