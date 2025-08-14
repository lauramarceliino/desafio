import pandas as pd
import os

# Caminho local onde os arquivos estão armazenados
caminho = r'C:\Users\Laura\documents\desafio\data\raw'  # ajuste "SeuUsuario" para o seu usuário do Windows

# Lista de arquivos
arquivos = ['EXP_2020.csv', 'EXP_2021.csv', 'IMP_2020.csv', 'IMP_2021.csv']

# Função para verificar qualidade
def verificar_qualidade(df, nome_arquivo):
    print(f"\n--- Analisando {nome_arquivo} ---")
    print(f"Dimensões: {df.shape}")
    print("\nTipos de dados:")
    print(df.dtypes)
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())
    print("\nDuplicatas:")
    print(df.duplicated().sum())
    print("\nEstatísticas básicas (numéricas):")
    print(df.describe())

# Loop pelos arquivos
for arquivo in arquivos:
    caminho_arquivo = os.path.join(caminho, arquivo)
    df = pd.read_csv(caminho_arquivo)
    verificar_qualidade(df, arquivo)
