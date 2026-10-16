import pandas as pd
from pathlib import Path

# 1. Configuração de caminhos

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

# Caminhos de entrada
ARQUIVO_PAINEL = DATA_DIR / "2_tratado" / "oncological_panel_limpo.csv"
ARQUIVO_MUNICIPIOS = DATA_DIR / "1_bruto" / "municipios.csv"

# Caminho de saída
OUTPUT_DIR = DATA_DIR / "3_integracao"
ARQUIVO_SAIDA = OUTPUT_DIR / "oncological_panel_integrado.csv"

def integrar_dados():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for arquivo in [ARQUIVO_PAINEL, ARQUIVO_MUNICIPIOS]:
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    print("Lendo as bases de dados...")
    
    # 2. Ler as bases
    painel_df = pd.read_csv(ARQUIVO_PAINEL, low_memory=False)
    municipios_df = pd.read_csv(ARQUIVO_MUNICIPIOS, low_memory=False)

    print(f"Dimensões Painel Oncológico: {painel_df.shape}")
    print(f"Dimensões Municípios: {municipios_df.shape}")

    # 3. Tratamento da chave de integração
    print("\nAjustando código IBGE de 7 para 6 dígitos...")
    
    # Converte o código IBGE para string e pega apenas os 6 primeiros caracteres
    municipios_df['codigo_ibge_6'] = municipios_df['codigo_ibge'].astype(str).str[:6]
    
    # Garantir que a coluna do Datasus também seja lida como string para cruzar corretamente
    painel_df['MUN_RESID'] = painel_df['MUN_RESID'].astype(str).str.split('.').str[0]

 
    # 4. Integração dos dados
    print("Realizando o cruzamento das tabelas pelo Município de Residência (MUN_RESID)...")
    
    # Faz o merge: Trazendo os dados de latitude, longitude e nome do município para o painel
    df_integrado = pd.merge(
        painel_df, 
        municipios_df, 
        left_on='MUN_RESID', 
        right_on='codigo_ibge_6', 
        how='left' # Usamos left para não perder pacientes que por acaso tenham código de município inválido
    )

    print(f"Dimensões da Base Integrada: {df_integrado.shape}")

    # 5. Exportação para data/features
    print(f"\nSalvando resultado final em: {ARQUIVO_SAIDA}")
    df_integrado.to_csv(ARQUIVO_SAIDA, index=False)
    print("Integração concluída com sucesso!")

if __name__ == "__main__":
    integrar_dados()