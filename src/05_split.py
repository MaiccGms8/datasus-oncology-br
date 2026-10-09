# Parte Jessya (código que deve ser alterado quando chegar os dados da parte 4 e 5)

import pandas as pd
from sklearn.model_selection import train_test_split
import os

def executar_split():
    print("Iniciando a Etapa 5: Separação de Treino e Teste...")
    
    # Ajuste: lendo da pasta tratado (ou features, quando a etapa 4 estiver pronta)
    caminho_entrada = "data/tratado/oncological_panel_limpo.csv"
    
    # Ajuste: garantindo que a pasta split existe
    pasta_saida = "../data/split"
    os.makedirs(pasta_saida, exist_ok=True)

    dados = pd.read_csv(caminho_entrada)

    print("Base carregada com sucesso!")
    print(f"Quantidade de registros: {len(dados)}")
    print(f"Quantidade de colunas: {len(dados.columns)}\n")

    # Regra da aula: semente fixa (random_state=42) e guardando o teste
    dados_treino, dados_teste = train_test_split(
        dados,
        test_size=0.30,
        random_state=42
    )

    print("Separação realizada com sucesso!")
    print(f"Total de registros: {len(dados)}")
    print(f"Registros para treino: {len(dados_treino)}")
    print(f"Registros para teste: {len(dados_teste)}\n")

    print(f"Percentual de treino: {round(len(dados_treino) / len(dados) * 100, 2)}%")
    print(f"Percentual de teste: {round(len(dados_teste) / len(dados) * 100, 2)}%\n")

    # Ajuste: salvando os arquivos na pasta correta (data/split/)
    caminho_treino = f"{pasta_saida}/oncological_panel_treino.csv"
    caminho_teste = f"{pasta_saida}/oncological_panel_teste.csv"
    
    dados_treino.to_csv(caminho_treino, index=False)
    dados_teste.to_csv(caminho_teste, index=False)

    print("Arquivos salvos com sucesso na pasta data/split/!")

if __name__ == "__main__":
    executar_split()