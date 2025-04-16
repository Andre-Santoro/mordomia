import flet as ft
import subprocess
import sys
import pyautogui as py
from componentes.conversa import container_conversa
from respostas.respostas_personalizadas import verificar_resposta_personalizada
from respostas.comandos import verificar_comando
from respostas.easter_eggs import verificar_easter_eggs
from time import sleep


def chamar_ollama(mensagem_enviada):
    try:
        prompt = (
            "Você é MordomIA, um assistente educado, direto e sempre responde em português. "
            "Fale como um mordomo moderno, mas amigável. "
            "Evite repetir informações. Seja claro e útil. "
            f"O Usuário disse: {mensagem_enviada}"
        )
        resultado = subprocess.run(
            f'echo "{prompt}" | ollama run gemma:2b',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        )
        resposta = resultado.stdout.decode().strip()
        if not resposta:
            resposta = "Desculpe, não consegui obter uma resposta."
        return resposta
    except Exception as e:
        return f"Erro ao acessar IA: {e}"


# -------------------------------------------- #


def main(pagina: ft.Page):

    pagina.title = "MordomIA"
    pagina.window.center() 
    pagina.bgcolor="#5b0060"

    def handle_window_event(evento):
        if evento.data == "close":
            pagina.open(alerta_de_saida)

    def botao_sim(evento):
        pagina.window.destroy()

    def botao_nao(evento):
        pagina.close(alerta_de_saida)

    alerta_de_saida = ft.AlertDialog(
    modal=True,
    bgcolor="#5b0060",  # tom escuro do gradiente
    title=ft.Text(
        "Confirme:",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",  # texto branco para contraste
        text_align=ft.TextAlign.CENTER
    ),
    content=ft.Text(
        "Você quer realmente fechar o MordomIA?",
        color="white"
    ),
    actions=[
        ft.ElevatedButton("Sim", on_click=botao_sim, bgcolor="#ca485c", color="white"),
        ft.OutlinedButton("Não", on_click=botao_nao, style=ft.ButtonStyle(color="white"))
    ],
    actions_alignment=ft.MainAxisAlignment.CENTER,
)



    pagina.window.prevent_close = True
    pagina.window.on_event = handle_window_event
    pagina.window.visible = True

    titulo_introducao = ft.Container(
    content=ft.Text(
        "Bem-vindo ao MordomIA!",
        size=28,
        color="white",
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD
    ),
    alignment=ft.alignment.center,
    padding=30,
    bgcolor="#5b0F60",  # Cor intermediária do gradiente
    border_radius=20
)

    pagina.add(
    ft.Container(
        content=ft.Column(
            controls=[titulo_introducao],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=300,
        expand=True,  # Faz o container ocupar toda a tela
        alignment=ft.alignment.center  # Centraliza o conteúdo
    )
)
    pagina.update()
    sleep(2.5)
    pagina.controls.clear()

    pagina.window.maximized = True

    # -----------------------------------------------------------------------------------------------------------#

    mensagens = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    historico_conversa = ft.TextField(
        label="Histórico da conversa",
        multiline=True,
        read_only=True,
        visible=False,
        min_lines=4,
        max_lines=10,
        width=500
    )

    alerta_sem_texto = ft.Container(
    content=ft.Text(
        "Por favor, digite uma mensagem antes de enviar.",
        opacity=0,
        color="white",
    ),
    alignment=ft.alignment.center,
    padding=20,
)

    input_mensagem = ft.TextField(
        label="Digite uma mensagem para o MordomIA",
        width=500,
        on_submit=lambda e: enviar_mensagem(),
        color="black",
        border_radius=10,
        filled=True,
    )

    botao_enviar_mensagem = ft.ElevatedButton(
        "Enviar mensagem",
        on_click=lambda e: enviar_mensagem(),
        bgcolor="red",
        color="white",
    )

    botao_copiar = ft.ElevatedButton(
        "Copiar conversa",
        on_click=lambda e: pagina.set_clipboard(historico_conversa.value),
        bgcolor="red",
        color="white",
    )



    titulo_conversa = ft.Container(
    content=ft.Text(
        "Converse com o MordomIA",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="white"
    ),
    alignment=ft.alignment.center,
)
    titulo_app = ft.Container(
    content = ft.Text(
        "MORDOMIA",
        style=ft.TextThemeStyle.HEADLINE_LARGE,  # Título maior
        color="white",
        text_align=ft.TextAlign.CENTER,
        ),
        padding=ft.padding.only(bottom=20)
    )


    conteudo_conversa = ft.Column(
        controls=[
            titulo_conversa,
            container_conversa(botao_copiar, alerta_sem_texto, input_mensagem, botao_enviar_mensagem, mensagens),
            historico_conversa,
        ],
    )

    conteudo_sobre = ft.Column(
        controls=[
            ft.Text("\n\n   O projeto MordomIA nasceu da ideia de criar um assistente virtual que fosse mais do que apenas funcional — eu queria que ele tivesse personalidade, estilo e uma identidade visual marcante."
                    " A jornada começou com uma interface simples, evoluindo gradualmente para algo que reflete dedicação, criatividade e muito carinho pelo que fazemos.\n\n"
                    "   Utilizando tecnologias como Flet e Python, e integrando com o modelo Gemma via Ollama, busquei oferecer respostas úteis, inteligentes e com um toque de humor e referências da cultura pop."
                    " Cada detalhe foi ajustado cuidadosamente: desde o gradiente suave do fundo até os easter eggs escondidos que fazem referência a franquias icônicas.\n\n"
                    "   Meu objetivo com o MordomIA é trazer funcionalidade ao dia a dia, desde trazer fazer coisas que você peça no seu computador, porém essa versão ficará por aqui. Espero que você se sinta bem-vindo por aqui — e saiba que este é apenas o começo."
                    " Muito obrigado por me acompanhar até aqui!",
                    color="white", size=16,),
            
        ],
        visible=False
    )

    def exibir_conversa(e):
        conteudo_conversa.visible = True
        conteudo_sobre.visible = False
        botao_conversa.style = ft.ButtonStyle(bgcolor="pink", color="white")
        botao_sobre.style = None
        pagina.update()

    def exibir_sobre(e):
        conteudo_conversa.visible = False
        conteudo_sobre.visible = True
        botao_sobre.style = ft.ButtonStyle(bgcolor="pink", color="white")
        botao_conversa.style = None
        pagina.update()

    def enviar_mensagem():
        mensagem = input_mensagem.value.strip().lower()

        if not mensagem:
            alerta_sem_texto.content.opacity = 1
        else:
            mensagens.controls.append(
                ft.Container(
                    ft.Text(f"Você: {mensagem}", color="white"),
                    padding=10,
                    border_radius=8,
                    bgcolor="transparent"  # Ou use uma cor de fundo suave, se quiser diferenciar
                )
            )

            alerta_sem_texto.opacity = 0

            resposta = verificar_comando(mensagem, pagina, mensagens, historico_conversa)
            if not resposta:
                resposta = verificar_resposta_personalizada(mensagem)
            if not resposta:
                resposta = verificar_easter_eggs(mensagem)
            if not resposta:
                resposta = chamar_ollama(mensagem)

            
            mensagens.controls.append(
                ft.Container(
                    ft.Text(f"MordomIA: {resposta}", color="white"),
                    padding=10,
                    border_radius=8,
                    bgcolor="transparent"
                )
            )

            historico_conversa.value += f"Você: {mensagem}\nMordomIA: {resposta}\n\n"

        input_mensagem.value = ""
        pagina.update()

    botao_conversa = ft.ElevatedButton(
        "Conversa",
        on_click=exibir_conversa,
        color="black"
        )
    botao_sobre = ft.ElevatedButton(
        "Sobre", 
        on_click=exibir_sobre,
        color="black"
        )

    botao_conversa.style = ft.ButtonStyle(bgcolor="pink", color="white")  # Padrão ativo



    conteudo = ft.Container(
        expand=True,
        padding=50,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                "0xff1f005c",
                "0xff5b0060",
                "0xff870160",
                "0xffac255e",
                "0xffca485c",
                "0xffe16b5c",
                "0xfff39060",
                "0xffffb56b",
            ]
        ),
        content=ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo_app,
                ft.Row(
                    controls=[botao_conversa, botao_sobre],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                conteudo_conversa,
                conteudo_sobre,
            ]
        )
    )
    pagina.add(conteudo)

ft.app(target=main)
