
from pathlib import Path
import pandas as pd

# Caminho principal do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = DATA_DIR / "tratado"

# Criar a pasta de saída se não existir
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Caminhos dos arquivos de entrada
arquivo_datasus = DATA_DIR / "oncological_panel_datasus.csv"
arquivo_limpo = DATA_DIR / "oncological_panel_limpo.csv"

# Verificar se os arquivos existem
for arquivo in (arquivo_datasus, arquivo_limpo):
    if not arquivo.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {arquivo}"
        )

# Ler as bases
datasus = pd.read_csv(arquivo_datasus, low_memory=False)
limpo = pd.read_csv(arquivo_limpo, low_memory=False)

# Limpar espaços dos nomes das colunas
datasus.columns = datasus.columns.str.strip()
limpo.columns = limpo.columns.str.strip()

# Exibir dimensões das bases
print("=== DIMENSÕES DAS BASES ===")
print("DATASUS:", datasus.shape)
print("Base limpa:", limpo.shape)

# Exibir nomes das colunas
print("\n=== COLUNAS DATASUS ===")
print(datasus.columns.tolist())

print("\n=== COLUNAS DA BASE LIMPA ===")
print(limpo.columns.tolist())

# Identificar colunas em comum
colunas_comuns = sorted(
    set(datasus.columns).intersection(limpo.columns)
)

print("\n=== COLUNAS EM COMUM ===")
print(colunas_comuns)

# Salvar relatório da análise
relatorio = OUTPUT_DIR / "relatorio_integracao.txt"

with open(relatorio, "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE INTEGRAÇÃO DAS FONTES\n\n")
    arquivo.write(f"Dimensões DATASUS: {datasus.shape}\n")
    arquivo.write(f"Dimensões base limpa: {limpo.shape}\n\n")
    arquivo.write("Colunas em comum:\n")
    arquivo.write("\n".join(colunas_comuns))
    arquivo.write("\n")

print(f"\nRelatório salvo em: {relatorio}")
print("Verificação das fontes concluída!")
