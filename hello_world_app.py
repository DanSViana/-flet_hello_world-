import flet as ft

def main(page: ft.Page):
    page.title = "Olá, mundo!"
    page.scroll = "adaptive"

    # declaraçã de variáveis
    nome = ft.TextField(label="Nome")
    texto = "Meu texto"

    page.add(
        ft.Text("Olá, mundo!", size=30, color="Blue", weight="bold"),
        nome,
        ft.TextButton("Clique aqui"),
        ft.Text(texto)
    )
    page.update()

ft.app(main)