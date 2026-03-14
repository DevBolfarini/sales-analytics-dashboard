import sqlite3
import logging
from pathlib import Path

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def criar_banco() -> None:
    """
    Cria o banco de dados SQLite e a tabela 'vendas_brutas' se não existirem.
    
    A função utiliza pathlib para garantir portabilidade entre sistemas operacionais
    e um bloco try-except para captura e registro de falhas.
    """
    # Usando pathlib para tratar caminhos de forma segura em qualquer OS
    caminho_banco = Path("data/vendas.db")
    caminho_banco.parent.mkdir(parents=True, exist_ok=True)
    
    query = """
    CREATE TABLE IF NOT EXISTS vendas_brutas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda TEXT NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        vendedor TEXT NOT NULL
    )
    """
    
    try:
        # Usando context manager (with) para garantir o fechamento da conexão
        with sqlite3.connect(caminho_banco) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            logging.info(f"Banco de dados e tabela garantidos em '{caminho_banco}'.")
            
    except sqlite3.Error as e:
        logging.error(f"Erro ao inicializar o banco de dados: {e}")


if __name__ == "__main__":
    criar_banco()
