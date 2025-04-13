import flet as ft
from openpyxl import Workbook
from datetime import datetime

def main(page: ft.Page):
    # Configurações iniciais da página
    page.bgcolor = ft.colors.CYAN_300  # Define uma cor de fundo suave (ciano claro)
    page.title = "DataTable em Flet com Excel"  # Título exibido na janela da aplicação
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza os elementos horizontalmente

    # Título da aplicação
    titulo = ft.Text(
        value="DataTable", 
        size=24, 
        color=ft.colors.WHITE, 
        weight=ft.FontWeight.BOLD  # Negrito para destacar o título
    )

    # Criação da DataTable com estilos personalizados
    data_table = ft.DataTable(
        bgcolor=ft.colors.WHITE,  # Fundo branco para contraste com a página
        border=ft.border.all(width=2, color=ft.colors.BLACK26),  # Borda ao redor da tabela
        border_radius=10,  # Cantos arredondados para um visual mais moderno
        vertical_lines=ft.border.BorderSide(width=2, color=ft.colors.BLACK26),  # Linhas verticais entre colunas
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),  # Coluna ID em negrito
            ft.DataColumn(ft.Text("Nome", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),  # Coluna Nome em negrito
            ft.DataColumn(ft.Text("Idade", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),  # Coluna Idade em negrito
        ],
        rows=[],  # Inicialmente a tabela está vazia
    )

    # Campos de entrada para nome e idade com estilos aprimorados
    nome_input = ft.TextField(
        label="Nome",
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_radius=5,  # Cantos arredondados para um visual mais suave
        width=200,  # Largura fixa para melhor alinhamento
    )
    idade_input = ft.TextField(
        label="Idade",
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_radius=5,
        width=100,  # Largura menor, adequada para números
    )

    # Função para adicionar uma nova linha à tabela
    def adicionar_fila(e):
        # Verifica se ambos os campos estão vazios
        if not nome_input.value and not idade_input.value:
            # Cria uma mensagem de erro
            snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha pelo menos um dos campos: Nome ou Idade.", color=ft.colors.RED),
            )
            # Adiciona a mensagem à página e exibe
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        else:
            # Adiciona a nova linha se pelo menos um campo estiver preenchido
            nova_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(len(data_table.rows) + 1), color=ft.colors.BLACK)),
                    ft.DataCell(ft.Text(nome_input.value, color=ft.colors.BLACK)),
                    ft.DataCell(ft.Text(idade_input.value, color=ft.colors.BLACK)),
                ]
            )
            data_table.rows.append(nova_fila)
            # Limpa os campos após adicionar
            nome_input.value = ""
            idade_input.value = ""
            # Atualiza a tabela para mostrar a nova linha
            page.update()

    # Função para salvar os dados em um arquivo Excel
    def salvar_em_excel(e):
        wb = Workbook()  # Cria um novo arquivo Excel
        ws = wb.active  # Seleciona a planilha ativa
        ws.title = "Dados da tabela"  # Define o nome da planilha
        ws.append(["ID", "Nome", "Idade"])  # Adiciona o cabeçalho ao Excel
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])  # Adiciona cada linha da tabela ao Excel
        hora = datetime.now().strftime("%d%m%Y_%H:%M")  # Gera um timestamp para o nome do arquivo
        nome_arquivo = f"Dados_tabela_{hora}.xlsx"  # Nome único para o arquivo baseado na data e hora
        wb.save(nome_arquivo)  # Salva o arquivo Excel
        # Exibe uma mensagem de sucesso
        snack_bar = ft.SnackBar(
            content=ft.Text(f"Arquivo salvo com sucesso em {nome_arquivo}", color=ft.colors.GREEN),
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True  # Mostra a mensagem na tela
        page.update()  # Atualiza a interface

    # Botões estilizados para interação
    btn_adicionar = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_fila,  # Chama a função adicionar_fila ao clicar
        color=ft.colors.WHITE,
        bgcolor=ft.colors.CYAN_700,  # Cor de fundo ciano escuro
        elevation=5,  # Sombra para dar profundidade
    )
    btn_salvar = ft.ElevatedButton(
        text="Salvar em Excel",
        on_click=salvar_em_excel,  # Chama a função salvar_em_excel ao clicar
        color=ft.colors.WHITE,
        bgcolor=ft.colors.GREEN,  # Cor verde para indicar salvamento
        elevation=5,
    )

    # Container para organizar os campos de entrada e botões
    input_container = ft.Row(
        controls=[
            nome_input,
            idade_input,
            btn_adicionar,
            btn_salvar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os elementos no container
        spacing=20,  # Espaçamento entre os elementos para evitar aglomeração
    )

    # Adiciona todos os elementos à página
    page.add(
        titulo,
        input_container,
        data_table,
    )

# Inicia a aplicação
ft.app(target=main)