import sqlite3

def criar_banco():
    # 1. Definimos o caminho onde o arquivo do banco será salvo. 
    # Como vamos rodar o código da raiz do projeto, o caminho é relativo à raiz.
    caminho_banco = "data/vendas.db"
    
    # 2. Conectando ao banco (se o arquivo não existir, o SQLite cria para a gente!)
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()
    
    # 3. A query SQL para criar a tabela. 
    # DICA INTRODUTÓRIA: O id precisa ser INTEGER PRIMARY KEY AUTOINCREMENT
    query = """
    CREATE TABLE IF NOT EXISTS vendas_brutas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda TEXT,
        produto TEXT,
        quantidade INTEGER,
        preco_unitario REAL,
        vendedor TEXT
    )
    """
    
    # 4. Executa a query
    cursor.execute(query)
    
    # 5. Salva e fecha
    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso na pasta 'data'!")

if __name__ == "__main__":
    criar_banco()
