import flet as ft

def main(page: ft.Page):
    """Função principal que configura e executa a aplicação Flet."""

    # --- Configurações Iniciais da Página ---
    page.title = "Minha Lista de Tarefas"
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 400
    page.window_height = 600

    # --- Variáveis de Estado e Funções ---

    # Lista Python para armazenar os *widgets* ft.ListTile de cada tarefa
    tarefas_widgets = []

    # Declaração antecipada das referências aos controles que as funções podem precisar atualizar
    # (Necessário se as funções precisarem acessar controles definidos posteriormente)
    # Neste caso, precisamos de lista_tarefas_view, tarefas_selecionadas_info e campo_nova_tarefa
    lista_tarefas_view = ft.ListView(
        expand=True, spacing=8, padding=10, auto_scroll=True
    )
    tarefas_selecionadas_info = ft.Text(
        value='', size=16, color=ft.colors.WHITE70, italic=True
    )
    campo_nova_tarefa = ft.TextField(
        hint_text="Escreva uma nova tarefa aqui...",
        expand=True,
        border_color=ft.colors.WHITE54,
        focused_border_color=ft.colors.CYAN_ACCENT_400,
        text_style=ft.TextStyle(color=ft.colors.WHITE),
        # on_submit será definido depois que incluir_tarefa for definida
    )


    def selecionar_tarefa(e: ft.ControlEvent):
        """
        Chamada quando o estado de um Checkbox em uma tarefa muda.
        Atualiza o texto que mostra as tarefas selecionadas.
        """
        selecionadas = []
        for tarefa_widget in tarefas_widgets:
            if tarefa_widget.leading.value:
                selecionadas.append(tarefa_widget.title.value)

        if selecionadas:
            tarefas_selecionadas_info.value = "Selecionadas: " + ", ".join(selecionadas)
        else:
            tarefas_selecionadas_info.value = ""

        # É importante atualizar o controle específico que mudou
        tarefas_selecionadas_info.update()
        # page.update() # Usar page.update() se múltiplos controles mudarem

    def atualizar_lista_visivel():
        """
        Limpa a ListView visual e a preenche novamente com os widgets
        da lista Python 'tarefas_widgets'.
        """
        lista_tarefas_view.controls.clear()
        lista_tarefas_view.controls.extend(tarefas_widgets)
        lista_tarefas_view.update()

    def remover_tarefa(tarefa_widget: ft.ListTile):
        """Remove uma tarefa específica da lista."""
        tarefas_widgets.remove(tarefa_widget)
        atualizar_lista_visivel()
        selecionar_tarefa(None)

    def criar_widget_tarefa(texto_tarefa: str) -> ft.ListTile:
        """Cria um widget ft.ListTile para uma nova tarefa."""
        tarefa_widget = ft.ListTile(
            leading=ft.Checkbox(
                on_change=selecionar_tarefa,
                fill_color=ft.colors.ORANGE_400
            ),
            title=ft.Text(value=texto_tarefa, color=ft.colors.WHITE),
            trailing=ft.IconButton(
                icon=ft.icons.DELETE_OUTLINE,
                icon_color=ft.colors.RED_ACCENT_200,
                tooltip="Remover Tarefa",
                on_click=lambda e: remover_tarefa(tarefa_widget)
            )
        )
        return tarefa_widget

    def incluir_tarefa(e: ft.ControlEvent):
        """
        Chamada ao clicar no botão 'Incluir Tarefa' ou pressionar Enter no campo de texto.
        Adiciona a nova tarefa à lista.
        """
        texto_novo = campo_nova_tarefa.value.strip()
        if texto_novo:
            tarefa_widget_novo = criar_widget_tarefa(texto_novo)
            tarefas_widgets.append(tarefa_widget_novo)
            campo_nova_tarefa.value = ""
            # Resetar a dica e a borda caso estivessem em estado de erro
            campo_nova_tarefa.hint_text="Escreva uma nova tarefa aqui..."
            campo_nova_tarefa.border_color=ft.colors.WHITE54
            campo_nova_tarefa.focus()
            atualizar_lista_visivel()
            selecionar_tarefa(None) # Atualiza o texto de selecionadas
            campo_nova_tarefa.update() # Atualiza o campo de texto (valor e hint)
        else:
            campo_nova_tarefa.hint_text = "Por favor, digite algo!"
            campo_nova_tarefa.border_color = ft.colors.RED
            campo_nova_tarefa.update() # Atualiza o campo para mostrar o erro

    # --- Widgets da Interface (Definidos *depois* das funções) ---

    # Agora podemos definir o on_submit aqui, pois incluir_tarefa já existe
    campo_nova_tarefa.on_submit = incluir_tarefa

    # Título principal da aplicação
    titulo = ft.Text(
        value="Minha Lista de Tarefas",
        weight=ft.FontWeight.BOLD,
        size=28,
        color=ft.colors.WHITE
    )

    # Botão para adicionar a tarefa digitada à lista
    # Agora a função incluir_tarefa já está definida e pode ser usada
    btn_incluir_tarefa = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        tooltip="Incluir Tarefa",
        on_click=incluir_tarefa,  # Agora isso funciona!
        bgcolor=ft.colors.CYAN_ACCENT_700
    )

    # --- Layout da Página ---
    page.add(
        titulo,
        ft.Row(
            controls=[
                campo_nova_tarefa,
                btn_incluir_tarefa
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        lista_tarefas_view, # ListView definida antecipadamente
        ft.Divider(height=1, color=ft.colors.WHITE24),
        tarefas_selecionadas_info # Texto definido antecipadamente
    )

    # Atualiza a página inicialmente
    page.update()

# --- Execução da Aplicação ---
ft.app(target=main)