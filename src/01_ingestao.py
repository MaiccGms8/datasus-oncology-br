import os
import urllib.request

def executar_ingestao():
    print("Iniciando ingestão dos dados")
    
    # Conferindo se a pasta existe
    pasta_destino = 'data/bruto'
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Caminhos dos arquivos
    caminho_base_principal = f'{pasta_destino}/oncological_panel_datasus.csv'
    caminho_base_secundaria = f'{pasta_destino}/municipios.csv'
    
    # Validar a base principal
    if os.path.exists(caminho_base_principal):
        print(f"Base principal encontrada em {caminho_base_principal}")
    else:
        print(f"A base principal NÃO foi encontrada em {caminho_base_principal}.")
        print("Coloque o arquivo oncological_panel_datasus.csv dentro de data/bruto/")
        
    # 4. Baixar a base secundária
    url_municipios = "https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv"
    
    print(f"Baixando base secundária de: {url_municipios}")
    try:
        urllib.request.urlretrieve(url_municipios, caminho_base_secundaria)
        print(f"Base secundária salva em {caminho_base_secundaria}")
    except Exception as e:
        print(f"ERRO ao baixar a base secundária: {e}")


if __name__ == "__main__":
    executar_ingestao()