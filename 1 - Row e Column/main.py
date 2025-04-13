import flet as ft

def main(page: ft.Page):
    page.title = "Flet Row e Column Example"
    page.bgcolor = ft.Colors.AMBER_50
    texto1 =  ft.Text(value="Texto 1", color=ft.Colors.BLACK, size=24, weight=ft.FontWeight.W_100)
    texto2 = ft.Text(value="Texto 2", color=ft.Colors.BLUE_900, size=24)
    texto3 = ft.Text(value="Texto 3", color=ft.Colors.BROWN_900, size=24)
    
    # Criando uma Row
    row = ft.Row(
        controls=[texto1, texto2, texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )
    page.add(row)
    
    def texto_click(e):
        texto1.value = "Texto 1 clicado!"
        texto1.size = 10
        page.update()
        
    btn1 = ft.ElevatedButton(text="Botão 1", bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=texto_click)
    btn2 = ft.ElevatedButton(text="Botão 2", bgcolor=ft.colors.AMBER, color=ft.colors.BLACK)
    btn3 = ft.ElevatedButton(text="Botão 3", bgcolor=ft.colors.AMBER, color=ft.colors.BLACK)
    # Criando Row dos botões
    row2 = ft.Row(
        controls=[btn1, btn2, btn3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )
    page.add(row2)
    
    
    # Columns de textos
    txt_columns1 = [
        ft.Text(value=f"Culuna 1", color=ft.Colors.BLACK, size=18),
        ft.Text(value=f"Culuna 1", color=ft.Colors.BLACK, size=18),
        ft.Text(value=f"Culuna 1", color=ft.Colors.BLACK, size=18),
    ]
    # Criando Column
    column = ft.Column(
        controls=txt_columns1,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )
    page.add(column)

    # Columns de textos
    txt_columns2 = [
        ft.Text(value=f"Coluna 2", color=ft.Colors.BLACK, size=18),
        ft.Text(value=f"Coluna 2", color=ft.Colors.BLACK, size=18),
        ft.Text(value=f"Coluna 2", color=ft.Colors.BLACK, size=18),
    ]
    # Criando Column
    column2 = ft.Column(
        controls=txt_columns2,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )
    row_colunas = ft.Row(
        controls=[column, column2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )
    page.add(row_colunas)
ft.app(target=main)