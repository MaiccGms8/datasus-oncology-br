# Predição de Atrasos no Tratamento Oncológico (DataSUS)

Repositório da equipe para o projeto de Ciência de Dados voltado à análise do tempo de início do tratamento oncológico, com base em dados públicos do **DataSUS (2013–2023)**.

---

## Configuração do Ambiente

Como os arquivos de dados brutos e limpos são grandes, eles **não são versionados pelo Git** e estão listados no `.gitignore`.

Para executar o projeto localmente, siga os passos abaixo.

### 1. Clonar o Repositório

Abra o terminal e execute:

```bash
git clone https://github.com/MaiccGms8/datasus-oncology-br.git
cd datasus-oncology-br
```

---

### 2. Baixar a Base

A base de dados oficial utilizada no projeto está hospedada no **Kaggle**.

* Acesse o dataset: [Oncology Treatment DataSUS Brazil (2013–2023)](https://www.kaggle.com/datasets/lhucastenorio/oncology-treatment-datasus-brazil-20132023)
* Baixe o arquivo compactado.
* Descompacte os arquivos.
* Coloque o arquivo principal com o nome:

```text
oncological_panel_datasus.csv
```

dentro da pasta:

```text
data/
```

A estrutura esperada será:

```text
datasus-oncology-br/
├── data/
│   └── oncological_panel_datasus.csv
├── notebooks/
│   └── 01_pre_separacao.ipynb
└── ...
```

---

