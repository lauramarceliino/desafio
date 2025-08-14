import pandas as pd
import sqlite3
import os

# --- Configurações dos Caminhos ---
caminho_processado = r'C:\Users\Laura\documents\desafio\data\processed'
caminho_db = r'C:\Users\Laura\documents\desafio\data\database\dados_comercio_exterior1.db'

# --- Carregar os Arquivos CSV Unificados ---
try:
    df_exp_unificado = pd.read_csv(os.path.join(caminho_processado, 'EXP_dados_unificados.csv'), sep=';', encoding='utf-8')
    df_imp_unificado = pd.read_csv(os.path.join(caminho_processado, 'IMP_dados_unificados.csv'), sep=';', encoding='utf-8')
    print("Arquivos CSV unificados carregados com sucesso.")
except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado em '{caminho_processado}'. Erro: {e}")
    exit()

# --- Conectar ao Banco de Dados SQLite e Salvar ---
try:
    # Conecta ou cria o banco de dados
    conn = sqlite3.connect(caminho_db)
    
    # Salva o DataFrame de exportação na tabela 'exportacao'
    df_exp_unificado.to_sql('exportacao', conn, if_exists='replace', index=False)
    print("Dados de exportação salvos na tabela 'exportacao'.")
    
    # Salva o DataFrame de importação na tabela 'importacao'
    df_imp_unificado.to_sql('importacao', conn, if_exists='replace', index=False)
    print("Dados de importação salvos na tabela 'importacao'.")
    
    # Fecha a conexão
    conn.close()
    
    print("\nProcesso concluído. O arquivo 'dados_comercio_exterior1.db' foi criado.")

except Exception as e:
    print(f"Ocorreu um erro ao conectar ou salvar no banco de dados: {e}")