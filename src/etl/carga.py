import sys
import os
import logging
import pandas as pd

# Adiciona o diretório 'src' ao path para permitir a importação de módulos internos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.crud import conectar

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def rodar_etl_carga() -> None:
    """
    Executa o processo de Carga (ETL) utilizando inserção em massa (Bulk Insert)
    para otimizar a performance em produção.
    """
    caminho_csv = "data/vendas_historico.csv"
    logging.info("Iniciando o processo de ETL (Bulk Insert)...")
    
    try:
        # === 1. EXTRAIR (Extract) ===
        df_vendas_historico = pd.read_csv(caminho_csv)
        logging.info(f"Extração: {len(df_vendas_historico)} registros lidos do arquivo CSV.")
        
        # === 2. TRANSFORMAR (Transform) ===
        # Tratamento de dados nulos (Missing Values)
        df_vendas_historico['Quantidade'] = df_vendas_historico['Quantidade'].fillna(1)
        df_vendas_historico['Vendedor Nome'] = df_vendas_historico['Vendedor Nome'].fillna("Desconhecido")
        
        # Padronizando colunas para o formato exato esperado pela tabela SQL
        df_vendas_historico.rename(columns={
            'Data da Venda': 'data_venda',
            'Produto': 'produto',
            'Quantidade': 'quantidade',
            'Preco Unitario': 'preco_unitario',
            'Vendedor Nome': 'vendedor'
        }, inplace=True)

        logging.info("Transformação concluída: dados limpos e colunas padronizadas.")
        
        # === 3. CARREGAR (Load) ===
        # Utilizando .to_sql com a conexão isolada para altíssima performance
        with conectar() as conn:
            df_vendas_historico.to_sql(
                name='vendas_brutas',
                con=conn,
                if_exists='append',
                index=False
            )
            
        logging.info(f"Carga Concluída! {len(df_vendas_historico)} registros inseridos com sucesso.")

    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {caminho_csv}")
    except Exception as e:
        logging.error(f"Erro inesperado durante a execução do ETL: {e}")


if __name__ == "__main__":
    rodar_etl_carga()
