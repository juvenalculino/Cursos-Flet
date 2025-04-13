import flet as ft

def main(page: ft.Page):
    # --- Configurações Iniciais da Página ---
    page.title = "Notas Adesivas (Sticky Notes)" # Título da janela/aba
    page.padding = 20                         # Espaçamento interno da página
    page.theme_mode = ft.ThemeMode.LIGHT      # Define o tema como claro (LIGHT, DARK, SYSTEM)
    # page.bgcolor = ft.Colors.BLUE_GREY_800 # Removido para usar o fundo padrão do tema claro

    # --- Funções ---

    def delete_note(note_container: ft.Container):
        """
        Remove um widget de nota (o Container) da GridView.
        Args:
            note_container: O widget ft.Container que representa a nota a ser removida.
        """
        if note_container in grid.controls: # Verifica se a nota ainda está na grid
            grid.controls.remove(note_container)
            grid.update() # Atualiza apenas a grid na interface
            # page.update() # page.update() também funcionaria, mas grid.update() é mais específico

    def criar_nota_widget(text: str = "Nova Nota") -> ft.Container:
        """
        Cria o widget visual completo para uma nota adesiva.
        Args:
            text: O texto inicial a ser exibido na nota. Default é "Nova Nota".
        Returns:
            Um ft.Container estilizado representando a nota.
        """
        # Cria o campo de texto editável dentro da nota
        note_content = ft.TextField(
            value=text,
            multiline=True,          # Permite múltiplas linhas
            border=ft.InputBorder.NONE, # Remove a borda padrão do TextField
            text_style=ft.TextStyle(color=ft.colors.BLACK87), # Cor do texto
            bgcolor=ft.colors.TRANSPARENT, # Fundo transparente para usar o do Container
            min_lines=3,             # Altura mínima inicial
            max_lines=6              # Altura máxima
        )

        # Cria o container principal da nota, que será adicionado à grid
        note_container = ft.Container(
            # Conteúdo do container: uma coluna com o texto e o botão de deletar
            content=ft.Column(
                [
                    note_content, # O campo de texto editável
                    # Botão para deletar a nota, alinhado à direita
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.DELETE_OUTLINE,
                                tooltip="Deletar Nota",
                                icon_color=ft.colors.RED_400,
                                icon_size=18,
                                # A função lambda captura o 'note_container' atual
                                # para que saibamos qual nota deletar quando o botão for clicado.
                                # O argumento '_' do lambda é ignorado (representa o evento de clique).
                                on_click=lambda _: delete_note(note_container)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END # Alinha o botão à direita
                    )
                ],
                spacing=5 # Espaçamento entre o texto e o botão
            ),
            bgcolor=ft.colors.AMBER_200, # Cor de fundo amarela, típica de nota adesiva
            padding=10,                  # Espaçamento interno da nota
            border_radius=ft.border_radius.all(8), # Bordas arredondadas
            # Adiciona uma leve sombra para dar profundidade
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                offset=ft.Offset(2, 2),
            )
        )
        return note_container # Retorna o Container da nota pronto

    def add_new_note_click(e):
        """
        Função chamada ao clicar no botão 'Adicionar Nota'.
        Cria uma nova nota e a adiciona à grid.
        """
        nova_nota = criar_nota_widget() # Cria o widget da nova nota com texto padrão
        grid.controls.append(nova_nota) # Adiciona a nova nota aos controles da grid
        grid.update()                   # Atualiza a grid na interface para mostrar a nova nota

    # --- Widgets Principais ---

    # Botão para adicionar novas notas
    add_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        text="Adicionar Nota",
        tooltip="Criar uma nova nota adesiva",
        on_click=add_new_note_click
    )

    # GridView para organizar as notas
    grid = ft.GridView(
        expand=True,             # Faz a grid ocupar o espaço vertical/horizontal disponível
        max_extent=220,          # Largura máxima de cada "célula" da grid (cada nota)
        child_aspect_ratio=1.0,  # Proporção largura/altura (1.0 = quadrado)
        spacing=10,              # Espaçamento horizontal entre as notas
        run_spacing=10           # Espaçamento vertical entre as linhas de notas
    )

    # --- Lógica Inicial ---

    # Cria uma lista inicial de widgets de nota (usando a função corrigida)
    # Esta lista contém os *widgets* ft.Container prontos.
    initial_notes_widgets = [
        criar_nota_widget("Comprar pão"),
        criar_nota_widget("Ligar para o cliente X"),
        criar_nota_widget("Estudar Flet - GridView"),
        criar_nota_widget("Lavar o carro"),
        criar_nota_widget("Reunião às 15h"),
    ]

    # **CORREÇÃO:** Adiciona os widgets de nota iniciais *diretamente* aos controles da grid
    # Itera sobre a lista de widgets já criados.
    for note_widget in initial_notes_widgets:
        grid.controls.append(note_widget) # Adiciona o widget Container à grid

    # --- Layout da Página ---
    # Adiciona os controles à página na ordem desejada

    # **CORREÇÃO:** Adiciona a grid à página *depois* do loop, apenas uma vez.
    page.add(
        ft.Row([ft.Text("Minhas Notas", size=24, weight=ft.FontWeight.BOLD)]), # Título
        grid,        # A GridView já populada com as notas iniciais
        add_button   # O botão flutuante para adicionar novas notas
    )

    # Atualiza a página para exibir os controles adicionados
    # (geralmente não é estritamente necessário após page.add, mas garante a exibição)
    page.update()

# --- Execução da Aplicação ---
# Inicializa e roda a aplicação Flet, chamando a função 'main'
ft.app(target=main)