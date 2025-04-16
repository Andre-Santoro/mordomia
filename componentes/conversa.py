import flet as ft

def container_conversa(botao_copiar, alerta_sem_texto, input_mensagem, botao_enviar_mensagem, lista_mensagens):
    return ft.Container(
        content=ft.Column(
            controls=[
                alerta_sem_texto,
                ft.Row(
                    controls=[botao_copiar, input_mensagem, botao_enviar_mensagem],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(lista_mensagens, height=300),
            ],
            spacing=10
        ),
        border=ft.border.all(1, ft.colors.GREY),
        border_radius=12
    )
