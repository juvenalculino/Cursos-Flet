import flet as ft
import random
import os
import base64

# Lista de cores de fundo possíveis para os cards
BACKGROUND_COLORS = [
    ft.Colors.RED_ACCENT_700,
    ft.Colors.GREEN_ACCENT_700,
    ft.Colors.YELLOW_ACCENT_700,
    ft.Colors.PINK_ACCENT_700,
    ft.Colors.ORANGE_ACCENT_700,
    ft.Colors.PURPLE_ACCENT_700,
    ft.Colors.BLUE_ACCENT_700,
]

# Função para criar o widget de card de produto
def criar_produto_widget(nome: str, preco: str, descricao: str, bgcolor: str, nome_imagem: str) -> ft.Container:
    imagem_path = os.path.join(os.path.dirname(__file__), "assets", nome_imagem)
    imagem_base64 = None
    try:
        with open(imagem_path, "rb") as image_file:
            imagem_bytes = image_file.read()
            imagem_base64 = base64.b64encode(imagem_bytes).decode('utf-8')
    except FileNotFoundError:
        print(f"Arquivo de imagem não encontrado: {imagem_path}")

    """Cria e retorna um widget ft.Container estilizado para exibir um produto."""
    return ft.Container(
        # Coluna para empilhar os elementos dentro do card
        content=ft.Column(
            [
                ft.Image(
                    src_base64=imagem_base64,
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                    error_content=ft.Text("Imagem não encontrada", color=ft.Colors.RED)
                ) if imagem_base64 else ft.Container(width=150, height=150, bgcolor=ft.Colors.GREY_300, content=ft.Text("Sem Imagem", color=ft.Colors.BLACK, size=10, text_align=ft.TextAlign.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER, alignment=ft.alignment.center)),
                # Nome do Produto
                ft.Text(
                    nome,
                    size=18,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD
                ),
                # Preço do Produto
                ft.Text(
                    preco,
                    size=16,
                    color=ft.Colors.WHITE70
                ),
                # Container interno para o rótulo "Descrição"
                ft.Container(
                    padding=ft.padding.only(top=5, bottom=5),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                'Descrição:',
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            )
                        ],
                    )
                ),
                # Texto da Descrição
                ft.Text(
                    descricao,
                    size=13,
                    color=ft.Colors.WHITE,
                    italic=True,
                    text_align=ft.TextAlign.CENTER
                ),
                # Botão de Ação
                ft.ElevatedButton(
                    text="Comprar Agora",
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.CYAN_700,
                    icon=ft.Icons.SHOPPING_CART_OUTLINED,
                    on_click=lambda e: print(f"Botão Comprar clicado para {nome}!"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        # Estilização do Container principal do card
        bgcolor=bgcolor,
        padding=15,
        border_radius=10,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(2, 2),
        )
        
    )

# Função principal da aplicação Flet
def main(page: ft.Page):
    # --- Configurações Iniciais da Página ---
    page.title = "Galeria de Produtos"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START
    # Habilitar a rolagem vertical da página
    page.scroll = True

    # --- Dados dos Produtos (Exemplo) ---
    dados_produtos = [
        {"nome": "Smartphone XYZ", "preco": "R$ 1.499,90", "descricao": "Ótimo celular com câmera de 48MP.", "imagem": "smartphone.png"},
        {"nome": "Notebook ABC", "preco": "R$ 3.299,00", "descricao": "Leve e potente para trabalho e estudo.", "imagem": "notebook.png"},
        {"nome": "Fone Bluetooth Q", "preco": "R$ 199,90", "descricao": "Som imersivo com cancelamento de ruído.", "imagem": "fone.png"},
        {"nome": "Smartwatch Fit", "preco": "R$ 450,00", "descricao": "Monitore sua saúde e atividades físicas.", "imagem": "smartwatch.png"},
        {"nome": "Tablet Read", "preco": "R$ 899,00", "descricao": "Perfeito para leitura e entretenimento.", "imagem": "tablet.png"},
        {"nome": "Produto Extra 1", "preco": "R$ 99,99", "descricao": "Descrição do produto extra 1.", "imagem": "smartphone.png"},
        {"nome": "Produto Extra 2", "preco": "R$ 199,99", "descricao": "Descrição do produto extra 2.", "imagem": "notebook.png"},
        {"nome": "Produto Extra 3", "preco": "R$ 299,99", "descricao": "Descrição do produto extra 3.", "imagem": "fone.png"},
        {"nome": "Produto Extra 4", "preco": "R$ 399,99", "descricao": "Descrição do produto extra 4.", "imagem": "smartwatch.png"},
        {"nome": "Produto Extra 5", "preco": "R$ 499,99", "descricao": "Descrição do produto extra 5.", "imagem": "tablet.png"},
    ]

    # --- Layout Responsivo para os Produtos ---
    # Cria uma linha responsiva que organiza os itens em colunas
    # de acordo com o tamanho da tela.
    galeria_responsiva = ft.ResponsiveRow(
        # Cria os widgets de produto usando um loop (list comprehension)
        # e define como eles se comportam em diferentes tamanhos de tela.
        controls=[
            # Para cada produto nos dados, cria um widget e o coloca em uma coluna
            # O 'col={"sm": 12, "md": 6, "lg": 4, "xl": 3}' significa:
            # - Telas pequenas (sm): ocupa 12 de 12 colunas (largura total)
            # - Telas médias (md): ocupa 6 de 12 colunas (meia largura)
            # - Telas grandes (lg): ocupa 4 de 12 colunas (um terço da largura)
            # - Telas extra grandes (xl): ocupa 3 de 12 colunas (um quarto da largura)
            ft.Column(
                col={"sm": 12, "md": 6, "lg": 4, "xl": 3},
                controls=[
                    criar_produto_widget(
                        p["nome"], p["preco"], p["descricao"], random.choice(BACKGROUND_COLORS), p["imagem"]
                    )
                ]
            )
            for p in dados_produtos # Itera sobre a lista de dicionários de produtos
        ],
        # Espaçamento entre as linhas e colunas da grade responsiva
        run_spacing=15,
        spacing=15,
        # Alinha os itens ao topo dentro de suas células
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    # --- Adiciona os Controles à Página ---
    page.add(
        ft.Text("Galeria de Produtos", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.Colors.BLACK12),
        galeria_responsiva
    )

    # page.update() # Geralmente não necessário após o primeiro page.add

# --- Execução da Aplicação ---
ft.app(target=main)