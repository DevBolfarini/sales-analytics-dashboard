import streamlit as st
import pandas as pd
from database.crud import inserir_venda, listar_vendas, atualizar_venda, deletar_venda

# Configura a página do Streamlit
st.set_page_config(page_title="CRUD de Vendas", layout="wide")

st.title("📊 Sistema de Registro de Vendas")

# ==== SIDEBAR (Formulário de Entrada) ====
with st.sidebar:
    st.header("Cadastrar Nova Venda")
    
    # Criamos um formulário para o usuário preencher
    with st.form("form_nova_venda"):
        # O Streamlit tem vários tipos de input. 
        # Exemplo: st.date_input(), st.text_input(), st.number_input()
        
        # SEU CÓDIGO AQUI: 
        # Crie os inputs para as 5 variáveis que precisamos!
        # Dica: Para 'quantidade' (inteiro) e 'preco_unitario' (decimal/float), 
        # use st.number_input() passando o parâmetro 'step' (ex: step=1 para inteiros)
        
        produto = st.text_input("Produto")
        quantidade = st.number_input("Quantidade", step=1)
        preco_unitario = st.number_input("Preço Unitário", step=0.01)
        vendedor = st.text_input("Vendedor")


        
        nova_data = st.date_input("Data da Venda")
        # produto = ...
        # quantidade = ...
        # preco_unitario = ...
        # vendedor = ...
        
        # Botão de salvar
        btn_salvar = st.form_submit_button("Salvar Venda")
        
        if btn_salvar:
            # SEU CÓDIGO AQUI:
            # Chame a função inserir_venda() passando as variáveis acima.
            # (Atenção: st.date_input retorna um objeto Data, converta para string usando str(nova_data))

            inserir_venda(str(nova_data), produto, quantidade, preco_unitario, vendedor)
            
            # Depois de inserir, mostramos uma mensagem de sucesso
            st.success("Venda salva com sucesso!")

# ==== PÁGINA PRINCIPAL (Tabela de Exibição) ====
st.subheader("Gerenciamento de Vendas")

# Criamos 3 abas para organizar o nosso CRUD na tela principal
aba_visualizar, aba_atualizar, aba_excluir = st.tabs(["👁️ Visualizar", "✏️ Atualizar", "❌ Excluir"])

# --- ABA 1: VISUALIZAR (READ) ---
with aba_visualizar:
    dados = listar_vendas()
    if len(dados) > 0:
        df = pd.DataFrame(dados, columns=["ID", "Data", "Produto", "Quantidade", "Preço", "Vendedor"])
        
        # Dica de interface: Esconder o ID como índice pro visual ficar mais limpo
        df.set_index('ID', inplace=True)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nenhuma venda cadastrada ainda.")

# --- ABA 2: ATUALIZAR (UPDATE) ---
with aba_atualizar:
    st.write("Digite o ID da venda que deseja corrigir, e os novos valores adequados.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # ATENÇÃO: Pegando o ID
        update_id = st.number_input("ID da Venda para Atualizar", step=1, min_value=1, key="upd_id")
    with col2:
        update_qtd = st.number_input("Nova Quantidade", step=1, key="upd_qtd")
    with col3:
        update_preco = st.number_input("Novo Preço Unitário", step=0.01, key="upd_preco")
        
    if st.button("Atualizar Venda", type="primary"):
        # SEU CÓDIGO AQUI:
        # Chame a função atualizar_venda(...) passando os valores dos inputs acima.
        # atualizar_venda(...)
        
        st.success(f"Venda ID {update_id} atualizada com sucesso! Verifique a aba de Visualizar.")
        # Gambiarra rápida pro Streamlit recarregar a tela:
        st.rerun()

# --- ABA 3: EXCLUIR (DELETE) ---
with aba_excluir:
    st.write("Cuidado: Esta ação não pode ser desfeita.")
    
    delete_id = st.number_input("ID da Venda para Excluir", step=1, min_value=1, key="del_id")
    
    if st.button("Excluir Venda Permanentemente", type="primary"):
        # SEU CÓDIGO AQUI:
        # Chame a função deletar_venda(...) passando o ID do input de excluir.
        # deletar_venda(...)
        
        st.error(f"Venda ID {delete_id} foi excluída.")
        st.rerun()
