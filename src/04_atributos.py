import pandas as pd
from pathlib import Path


# 1. Configuração de caminhos
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

# Entrada
ARQUIVO_ENTRADA = DATA_DIR / "3_integracao" / "oncological_panel_integrado.csv"

# Saída
ARQUIVO_SAIDA = DATA_DIR / "4_features" / "oncological_panel_features.csv"

def criar_atributos():
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO_ENTRADA}. Rode o 03_integracao.py primeiro.")

    print(f"Lendo base integrada: {ARQUIVO_ENTRADA}")
    df = pd.read_csv(ARQUIVO_ENTRADA, low_memory=False)

    print("Iniciando Engenharia de Atributos")

    # 2. Tratamento de datas e idades
    colunas_datas = ['DT_NASC', 'DT_DIAG', 'DT_TRAT']
    for col in colunas_datas:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Cria 'IDADE' no momento do diagnóstico
    if 'DT_NASC' in df.columns and 'DT_DIAG' in df.columns:
        print("Calculando idade dos pacientes...")
        # Dias de diagnóstico menos data de nascimento dividido por dias no ano
        df['IDADE'] = (df['DT_DIAG'] - df['DT_NASC']).dt.days / 365.25
        df['IDADE'] = df['IDADE'].apply(lambda x: round(x) if pd.notnull(x) else x)

    # Criar 'FAIXA_ETARIA'
    if 'IDADE' in df.columns:
        print("Criando faixas etárias...")
        bins = [0, 18, 30, 40, 50, 60, 70, 80, 120]
        labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+']
        df['FAIXA_ETARIA'] = pd.cut(df['IDADE'], bins=bins, labels=labels, right=False)

    
    # 3. Extração de padrões temporais
    if 'DT_DIAG' in df.columns:
        print("Extraindo mês do diagnóstico...")
        df['MES_DIAG'] = df['DT_DIAG'].dt.month


    # 4. Tratamento da variável alvo
    # Atraso maior que 60 dias seja 0 ou 1
    if 'ATRASO_60_DIAS' in df.columns:
        print("Tratando a variável alvo (ATRASO_60_DIAS)...")
        # Se for um valor vazio, preenche com 0, e força a virar número inteiro
        df['ATRASO_60_DIAS'] = pd.to_numeric(df['ATRASO_60_DIAS'], errors='coerce').fillna(0).astype(int)

    # 5. Limpeza de colunas que não serão utilizadas
    print("Removendo colunas que não agregam ao modelo de machine learning...")

    colunas_para_remover = ['Unnamed: 0'] 
    
    colunas_existentes_remover = [c for c in colunas_para_remover if c in df.columns]
    df.drop(columns=colunas_existentes_remover, inplace=True)

    print(f"\nDimensões da base após engenharia de atributos: {df.shape}")

    # 6. Salvar a base final
    print(f"Salvando base com features em: {ARQUIVO_SAIDA}")
    df.to_csv(ARQUIVO_SAIDA, index=False)
    print("\nEtapa 04 concluída com sucesso! A base está pronta para o 05_split.py.")

if __name__ == "__main__":
    criar_atributos()