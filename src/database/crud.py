import sqlite3
import logging
from typing import List, Tuple, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def conectar() -> sqlite3.Connection:
    """Retorna uma conexão com o banco de dados principal."""
    return sqlite3.connect("data/vendas.db")


def inserir_venda(
    data_venda: str,
    produto: str,
    quantidade: int,
    preco_unitario: float,
    vendedor: str
) -> bool:
    """
    Insere uma nova venda no banco de dados.
    Retorna True se for bem sucedido, False em caso de erro.
    """
    query = """
        INSERT INTO vendas_brutas (data_venda, produto, quantidade, preco_unitario, vendedor)
        VALUES (?, ?, ?, ?, ?)
    """
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (data_venda, produto, quantidade, preco_unitario, vendedor))
            conn.commit()
            return True
    except sqlite3.Error as e:
        logging.error(f"Erro ao inserir venda: {e}")
        return False


def listar_vendas() -> List[Tuple[Any, ...]]:
    """
    Lê todas as vendas do banco e retorna como uma lista de tuplas.
    Retorna lista vazia se houver falha.
    """
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas_brutas")
            return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Erro ao listar vendas: {e}")
        return []


def atualizar_venda(id_venda: int, nova_quantidade: int, novo_preco: float) -> bool:
    """
    Atualiza a quantidade e o preço unitário de um registro com base no ID.
    Retorna True se for bem sucedido, False em caso de erro.
    """
    query = """
        UPDATE vendas_brutas SET quantidade = ?, preco_unitario = ? WHERE id = ?
    """
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nova_quantidade, novo_preco, id_venda))
            conn.commit()
            return True
    except sqlite3.Error as e:
        logging.error(f"Erro ao atualizar venda ID {id_venda}: {e}")
        return False


def deletar_venda(id_venda: int) -> bool:
    """
    Exclui permanentemente um registro do banco de dados com base no ID.
    Retorna True se for bem sucedido, False caso de erro.
    """
    query = """
        DELETE FROM vendas_brutas WHERE id = ?
    """
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id_venda,))
            conn.commit()
            return True
    except sqlite3.Error as e:
        logging.error(f"Erro ao deletar venda ID {id_venda}: {e}")
        return False


def atualizar_venda(id_venda, nova_quantidade, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    
    # SEU CÓDIGO AQUI:
    # 1. Escreva a query SQL de UPDATE.
    # Queremos atualizar a tabela `vendas_brutas`.
    # Defina (SET) a `quantidade` e o `preco_unitario` onde (`WHERE`) o `id` for igual ao id da venda passado.
    # Lembre-se de usar os placeholders (?) para evitar Injeção de SQL!
    query = """
        UPDATE vendas_brutas SET quantidade = ?, preco_unitario = ? WHERE id = ?
    """
    
    # 2. Execute a query passando a tupla de valores: (nova_quantidade, novo_preco, id_venda)
    cursor.execute(query, (nova_quantidade, novo_preco, id_venda))
    
    conn.commit()
    conn.close()


def deletar_venda(id_venda):
    conn = conectar()
    cursor = conn.cursor()
    
    # SEU CÓDIGO AQUI:
    # 1. Escreva a query SQL de DELETE.
    # Queremos deletar da tabela `vendas_brutas` o registro onde (`WHERE`) o `id` for igual ao id passado.
    query = """
        DELETE FROM vendas_brutas WHERE id = ?
    """
    
    # 2. Execute a query passando a tupla de valores contendo apenas o id_venda.
    # Lembrete Python: uma tupla com 1 elemento precisa de vírgula no final, assim: (id_venda,)
    cursor.execute(query, (id_venda,))
    
    conn.commit()
    conn.close()
