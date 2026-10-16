from pathlib import Path
import pandas as pd

# Diretório dos arquivos
DATA_DIR = Path(__file__).parent

# Ler as duas fontes
datasus = pd.read_csv(
    DATA_DIR / "oncological_panel_datasus.csv",
    low_memory=False
)

limpo = pd.read_csv(
    DATA_DIR / "oncological_panel_limpo.csv",
    low_memory=False
)

# Verificar dimensões
print("DATASUS:", datasus.shape)
print("Base limpa:", limpo.shape)

# Verificar as colunas de cada fonte
print("\nColunas DATASUS:")
print(datasus.columns.tolist())

print("\nColunas base limpa:")
print(limpo.columns.tolist())

# Verificar colunas em comum
comuns = datasus.columns.intersection(limpo.columns)
print("\nColunas em comum:")
print(comuns.tolist())

