import pandas as pd
import streamlit as st
from typing import List, Tuple, Any
from database.crud import (
    listar_vendas,
    inserir_venda,
    atualizar_venda,
    deletar_venda
)

# Configuração da página Streamlit (deve ser o primeiro comando)
st.set_page_config(
    page_title="CRUD de Vendas",
    page_icon="📊",
    layout="wide"
)


def render_sidebar() -> None:
    """Renderiza o formulário de cadastro de vendas na barra lateral."""
    st.sidebar.header("Cadastrar Nova Venda")
    with st.sidebar.form(key="form_cadastro"):
        produto = st.text_input("Produto")
        quantidade = st.number_input("Quantidade", min_value=1, step=1)
        preco_unitario = st.number_input("Preço Unitário", min_value=0.01, step=0.01, format="%.2f")
        vendedor = st.text_input("Vendedor")
        nova_data = st.date_input("Data da Venda")
        
        btn_salvar = st.form_submit_button("Salvar Venda")
        
        if btn_salvar:
            if not produto or not vendedor:
                st.error("Preencha todos os campos obrigatórios (Produto e Vendedor).")
            else:
                sucesso = inserir_venda(str(nova_data), produto, quantidade, preco_unitario, vendedor)
                if sucesso:
                    st.success("Venda salva com sucesso!")
                else:
                    st.error("Erro ao salvar no banco de dados.")


def render_dashboard(dados: List[Tuple[Any, ...]]) -> None:
    """Renderiza a aba de Dashboard gerencial agrupando vendas usando Pandas."""
    if not dados:
        st.info("Nenhuma venda cadastrada ainda para gerar o Dashboard.")
        return

    df_dash = pd.DataFrame(dados, columns=["ID", "Data", "Produto", "Quantidade", "Preço", "Vendedor"])
    df_dash['Faturamento'] = df_dash['Quantidade'] * df_dash['Preço']
    
    faturamento_total = df_dash['Faturamento'].sum()
    st.metric(
        label="Faturamento Total (R$)",
        value=f"{faturamento_total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    )
    
    st.divider()
    faturamento_por_vendedor = df_dash.groupby('Vendedor')['Faturamento'].sum().sort_values(ascending=False)
    
    st.subheader("Faturamento por Vendedor")
    st.bar_chart(faturamento_por_vendedor)


def render_carga() -> None:
    """Renderiza a aba para Upload (ETL Dinâmico via GUI)."""
    st.write("Faça o upload de um arquivo CSV de Vendas para importar automaticamente.")
    
    arquivo_csv = st.file_uploader("Selecione o arquivo CSV", type=['csv'])
    
    if arquivo_csv is not None:
        if st.button("Iniciar Importação (ETL)", type="primary"):
            with st.spinner('Processando ETL...'):
                try:
                    df_upload = pd.read_csv(arquivo_csv)
                    
                    if 'Quantidade' in df_upload.columns:
                        df_upload['Quantidade'] = df_upload['Quantidade'].fillna(1)
                    if 'Vendedor Nome' in df_upload.columns:
                        df_upload['Vendedor Nome'] = df_upload['Vendedor Nome'].fillna("Desconhecido")
                    
                    linhas_inseridas = 0
                    for _, linha in df_upload.iterrows():
                        inserir_venda(
                            str(linha.get('Data da Venda', '')),
                            str(linha.get('Produto', '')),
                            int(linha.get('Quantidade', 1)),
                            float(linha.get('Preco Unitario', 0.0)),
                            str(linha.get('Vendedor Nome', ''))
                        )
                        linhas_inseridas += 1
                        
                    st.success(f"ETL Concluído! {linhas_inseridas} linhas importadas.")
                except Exception as e:
                    st.error(f"Falha na importação. Verifique o arquivo. Erro: {e}")


def render_visualizar(dados: List[Tuple[Any, ...]]) -> None:
    """Renderiza a aba de listagem do CRUD em formato de tabela."""
    if not dados:
        st.info("Nenhuma venda registrada.")
        return
        
    df = pd.DataFrame(dados, columns=["ID", "Data", "Produto", "Quantidade", "Preço", "Vendedor"])
    st.dataframe(
        df,
        hide_index=True,
        column_config={
            "Quantidade": st.column_config.NumberColumn(format="%d"),
            "Preço": st.column_config.NumberColumn(format="R$ %.2f")
        }
    )


def render_atualizar() -> None:
    """Renderiza a aba de Atualização de registro do CRUD."""
    st.write("Digite o ID da venda que deseja atualizar:")
    with st.form(key="form_atualizar"):
        id_atualizar = st.number_input("ID da Venda", min_value=1, step=1)
        nova_qtde = st.number_input("Nova Quantidade", min_value=1, step=1)
        novo_preco = st.number_input("Novo Preço Unitário", min_value=0.01, step=0.01)
        
        if st.form_submit_button("Atualizar Registro"):
            sucesso = atualizar_venda(id_atualizar, nova_qtde, novo_preco)
            if sucesso:
                st.success(f"Venda ID {id_atualizar} atualizada!")
            else:
                st.error("Erro ao atualizar base de dados.")


def render_excluir() -> None:
    """Renderiza a aba de Exclusão de registro do CRUD."""
    st.write("Digite o ID da venda que deseja excluir permanentemente:")
    with st.form(key="form_excluir"):
        id_excluir = st.number_input("ID da Venda para Excluir", min_value=1, step=1)
        
        if st.form_submit_button("Atenção: Excluir Registro"):
            sucesso = deletar_venda(id_excluir)
            if sucesso:
                st.warning(f"Venda ID {id_excluir} excluída!")
            else:
                st.error("Erro ao excluir. O ID existe?")


def main() -> None:
    """Função orquestradora da aplicação Streamlit."""
    st.title("📊 Sistema Corporativo de Vendas")
    
    render_sidebar()
    
    st.subheader("Painel de Controle")
    abas = st.tabs(["📈 Dashboard", "📥 Carga de Dados", "👁️ Visualizar", "✏️ Atualizar", "❌ Excluir"])
    
    # Cache do banco para não puxar os dados múltiplas vezes atoa em abas paralisadas
    dados_banco = listar_vendas()
    
    with abas[0]: render_dashboard(dados_banco)
    with abas[1]: render_carga()
    with abas[2]: render_visualizar(dados_banco)
    with abas[3]: render_atualizar()
    with abas[4]: render_excluir()


if __name__ == "__main__":
    main()
