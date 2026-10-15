import pandas as pd
import numpy as np

def executar_limpeza():
    print("Iniciando limpeza dos dados")
    
    caminho_csv = 'data/bruto/oncological_panel_datasus.csv'
    caminho_salvamento = 'data/tratado/oncological_panel_limpo.csv'

    df = pd.read_csv(caminho_csv)
    print(f"Dataset carregado: {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # Limpando a coluna de tempo de tratamento
    df['TEMPO_TRAT'] = pd.to_numeric(df['TEMPO_TRAT'], errors='coerce')
    df.loc[df['TEMPO_TRAT'] > 5000, 'TEMPO_TRAT'] = np.nan
    
    # Removendo linhas sem informação de tempo de tratamento
    df = df.dropna(subset=['TEMPO_TRAT']).copy()
    print(f"Registros após remover nulos e erros de TEMPO_TRAT: {len(df)}")

    # Criação da variável-alvo ATRASO_60_DIAS
    df['ATRASO_60_DIAS'] = (df['TEMPO_TRAT'] > 60).astype(int)

    # Conversão das datas para o tipo datetime
    df['DT_DIAG'] = pd.to_datetime(df['DT_DIAG'], format='%Y-%m-%d', errors='coerce')
    df['ANOMES_DIA'] = pd.to_datetime(df['ANOMES_DIA'].astype(str).str.slice(0, 6), format='%Y%m', errors='coerce')

    # Removendo linhas que não possuem a referência de data
    df = df.dropna(subset=['ANOMES_DIA'])

    # Exportação
    df.to_csv(caminho_salvamento, index=False)
    print(f"Base limpa salva com sucesso em: {caminho_salvamento}")

if __name__ == "__main__":
    executar_limpeza()