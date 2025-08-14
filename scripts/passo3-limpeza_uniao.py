import pandas as pd
import os

# --- Configurações dos Caminhos ---
caminho_entrada = r'C:\Users\Laura\documents\desafio\data\processed'
caminho_saida = r'C:\Users\Laura\documents\desafio\data\processed'

# Dicionário de mapeamento para renomear as colunas
novos_nomes = {
    'CO_ANO': 'Ano',
    'CO_MES': 'Mês',
    'CO_NCM': 'código NCM',
    'CO_UNID': 'código da unidade estatística',
    'SG_UF_NCM': 'Estado',
    'QT_ESTAT': 'quantidade estatística',
    'KG_LIQUIDO': 'quilograma líquido',
    'VL_FOB': 'valor dólar FOB (US$)',
    'NO_NCM_POR': 'Produto'
}

# Lista de colunas a serem mantidas no arquivo final
colunas_finais = list(novos_nomes.values())


# --- Processamento dos arquivos de EXPORTAÇÃO ---
print("\n--- Processando arquivos de Exportação ---")
exp_files = ['EXP_2020_com_descricao.csv', 'EXP_2021_com_descricao.csv']
exp_dfs = []

for file in exp_files:
    try:
        df = pd.read_csv(os.path.join(caminho_entrada, file), sep=';', encoding='utf-8')
        df.rename(columns=novos_nomes, inplace=True)
        # Filtra apenas as colunas desejadas após a renomeação
        df_filtrado = df[colunas_finais]
        exp_dfs.append(df_filtrado)
    except FileNotFoundError:
        print(f"Aviso: Arquivo '{file}' não encontrado. Pulando.")
    except Exception as e:
        print(f"Erro ao ler o arquivo {file}: {e}")

if exp_dfs:
    df_exp_concatenado = pd.concat(exp_dfs, ignore_index=True)
    caminho_saida_exp = os.path.join(caminho_saida, 'EXP_dados_unificados.csv')
    df_exp_concatenado.to_csv(caminho_saida_exp, sep=';', index=False, encoding='utf-8')
    print(f"Arquivo de Exportação unificado e salvo em: {caminho_saida_exp}")
else:
    print("Nenhum arquivo de Exportação foi encontrado para processamento.")


# --- Processamento dos arquivos de IMPORTAÇÃO ---
print("\n--- Processando arquivos de Importação ---")
imp_files = ['IMP_2020_com_descricao.csv', 'IMP_2021_com_descricao.csv']
imp_dfs = []

for file in imp_files:
    try:
        df = pd.read_csv(os.path.join(caminho_entrada, file), sep=';', encoding='utf-8')
        df.rename(columns=novos_nomes, inplace=True)
        # Filtra apenas as colunas desejadas após a renomeação
        df_filtrado = df[colunas_finais]
        imp_dfs.append(df_filtrado)
    except FileNotFoundError:
        print(f"Aviso: Arquivo '{file}' não encontrado. Pulando.")
    except Exception as e:
        print(f"Erro ao ler o arquivo {file}: {e}")

if imp_dfs:
    df_imp_concatenado = pd.concat(imp_dfs, ignore_index=True)
    caminho_saida_imp = os.path.join(caminho_saida, 'IMP_dados_unificados.csv')
    df_imp_concatenado.to_csv(caminho_saida_imp, sep=';', index=False, encoding='utf-8')
    print(f"Arquivo de Importação unificado e salvo em: {caminho_saida_imp}")
else:
    print("Nenhum arquivo de Importação foi encontrado para processamento.")

print("\nProcessamento concluído.")