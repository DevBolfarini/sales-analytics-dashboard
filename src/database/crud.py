import sqlite3

# Função utilitária para conectar ao banco
def conectar():
    return sqlite3.connect("data/vendas.db")

def inserir_venda(data_venda, produto, quantidade, preco_unitario, vendedor):
    conn = conectar()
    cursor = conn.cursor()
    
    # SEU CÓDIGO AQUI: 
    # Qual é o comando SQL para INSERIR os dados na tabela 'vendas_brutas'?
    # DICA DE SEGURANÇA (Boa Prática): O SQLite permite o uso de interrogações (?) 
    # chamadas de "placeholders". Isso previne ataques de SQL Injection!
    # Lembre-se que as colunas são: data_venda, produto, quantidade, preco_unitario, vendedor
    query = """
        INSERT INTO vendas_brutas (data_venda, produto, quantidade, preco_unitario, vendedor)
        VALUES (?, ?, ?, ?, ?)
    """
    
    # Executamos a query substituindo as interrogações pelas variáveis (na mesma ordem!)
    cursor.execute(query, (data_venda, produto, quantidade, preco_unitario, vendedor))
    
    conn.commit()
    conn.close()

def listar_vendas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas_brutas")
    
    # O fetchall() "pesca" todos os resultados da query para o Python (como uma lista)
    resultados = cursor.fetchall() 
    
    conn.close()
    return resultados


def atualizar_venda(id_venda, nova_quantidade, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    
    # SEU CÓDIGO AQUI:
    # 1. Escreva a query SQL de UPDATE.
    # Queremos atualizar a tabela `vendas_brutas`.
    # Defina (SET) a `quantidade` e o `preco_unitario` onde (`WHERE`) o `id` for igual ao id da venda passado.
    # Lembre-se de usar os placeholders (?) para evitar Injeção de SQL!
    query = """
    
    """
    
    # 2. Execute a query passando a tupla de valores: (nova_quantidade, novo_preco, id_venda)
    # cursor.execute(query, (...))
    
    conn.commit()
    conn.close()


def deletar_venda(id_venda):
    conn = conectar()
    cursor = conn.cursor()
    
    # SEU CÓDIGO AQUI:
    # 1. Escreva a query SQL de DELETE.
    # Queremos deletar da tabela `vendas_brutas` o registro onde (`WHERE`) o `id` for igual ao id passado.
    query = """
    
    """
    
    # 2. Execute a query passando a tupla de valores contendo apenas o id_venda.
    # Lembrete Python: uma tupla com 1 elemento precisa de vírgula no final, assim: (id_venda,)
    # cursor.execute(query, (...))
    
    conn.commit()
    conn.close()
