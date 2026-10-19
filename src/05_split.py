
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Configuração dos caminhos
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

# Arquivo de entrada
ARQUIVO_ENTRADA = DATA_DIR / "4_features" / "oncological_panel_features.csv"

# Pasta e arquivos de saída
OUTPUT_DIR = DATA_DIR / "5_split"
ARQUIVO_TREINO = OUTPUT_DIR / "oncological_panel_treino.csv"
ARQUIVO_TESTE = OUTPUT_DIR / "oncological_panel_teste.csv"


def separar_dados():
    # Verifica se a base de entrada existe
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {ARQUIVO_ENTRADA}. "
            "Execute a etapa 04_atributos.py primeiro."
        )

    print("Lendo a base preparada...")
    df = pd.read_csv(ARQUIVO_ENTRADA, low_memory=False)

    print(f"Base original: {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # Separa 70% para treino e 30% para teste
    treino, teste = train_test_split(
        df,
        test_size=0.30,
        random_state=42,
        shuffle=True,
        stratify=df['ATRASO_60_DIAS']
    )

    # Cria a pasta de saída
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Salva os arquivos sem o índice do DataFrame
    treino.to_csv(ARQUIVO_TREINO, index=False)
    teste.to_csv(ARQUIVO_TESTE, index=False)

    print("\nSeparação concluída!")
    print(f"Treino: {len(treino)} registros ({len(treino) / len(df):.1%})")
    print(f"Teste: {len(teste)} registros ({len(teste) / len(df):.1%})")
    print(f"\nArquivo de treino: {ARQUIVO_TREINO}")
    print(f"Arquivo de teste: {ARQUIVO_TESTE}")


if __name__ == "__main__":
    separar_dados()
