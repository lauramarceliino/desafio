import pandas as pd
import os

# --- Configurações dos Caminhos ---
caminho_entrada = r'C:\Users\Laura\documents\desafio\data\raw'
caminho_saida = r'C:\Users\Laura\documents\desafio\data\processed'

# Garante que o diretório de saída exista, caso contrário, cria
if not os.path.exists(caminho_saida):
    os.makedirs(caminho_saida)
    print(f"Diretório criado: {caminho_saida}")

# --- Leitura do Arquivo de Referência (NCM.csv) ---
# O arquivo NCM é lido apenas uma vez para ser usado em todas as junções
try:
    df_ncm = pd.read_csv(os.path.join(caminho_entrada, 'NCM.csv'), sep=';', encoding='latin1')
    print("Arquivo NCM.csv carregado com sucesso.")
except FileNotFoundError:
    print(f"Erro: O arquivo 'NCM.csv' não foi encontrado em {caminho_entrada}")
    exit()

# --- Processamento dos Arquivos EXP e IMP ---
# Lista atualizada de arquivos que precisam ser processados
arquivos_a_processar = ['EXP_2020.csv', 'EXP_2021.csv', 'IMP_2020.csv', 'IMP_2021.csv']

# Loop para processar cada arquivo na lista
for nome_arquivo in arquivos_a_processar:
    print(f"\nIniciando processamento de: {nome_arquivo}")
    
    try:
        # Carrega o arquivo de exportação ou importação
        caminho_arquivo_entrada = os.path.join(caminho_entrada, nome_arquivo)
        df_exp_imp = pd.read_csv(caminho_arquivo_entrada, sep=';', encoding='utf-8')

        # Junta os dados com o dataframe do NCM
        df_merged = pd.merge(df_exp_imp, df_ncm[['CO_NCM', 'NO_NCM_POR']], on='CO_NCM', how='left')

        # Define o nome e caminho do arquivo de saída
        nome_arquivo_saida = nome_arquivo.replace('.csv', '_com_descricao.csv')
        caminho_arquivo_saida = os.path.join(caminho_saida, nome_arquivo_saida)

        # Salva o arquivo processado
        df_merged.to_csv(caminho_arquivo_saida, sep=';', index=False)
        print(f"-> Processamento concluído. Arquivo salvo em: {caminho_arquivo_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado em {caminho_entrada}. Pulando para o próximo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar '{nome_arquivo}': {e}")