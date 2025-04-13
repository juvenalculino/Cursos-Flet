import  flet as ft


def main(page: ft.Page):
    page.title = "DataTable"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(font_family="Roboto")
    



ft.app(target=main)