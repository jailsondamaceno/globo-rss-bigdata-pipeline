# Globo RSS Big Data Pipeline

Pipeline de dados desenvolvido em Python para coletar, transformar e armazenar notícias a partir do feed RSS da Globo.  
O projeto foi pensado com foco em **boas práticas de engenharia de dados**, organização de pipeline e versionamento profissional.

---

##  Objetivo

Demonstrar a construção de um pipeline de ingestão de dados desde a fonte (RSS) até a persistência em formato estruturado, com código organizado, testável e preparado para evolução em cenários de Big Data.

---

##  Arquitetura do Pipeline

O fluxo do pipeline é dividido em três etapas bem definidas:

1. **Ingestão (Coleta)**  
   - Consome o feed RSS da Globo via HTTP.

2. **Transformação**  
   - Parse do RSS/XML.
   - Extração de campos relevantes:
     - título
     - link
     - resumo
     - data de publicação

3. **Persistência**  
   - Armazenamento dos dados em JSON.
   - Versionamento por data de coleta.

---

##  Estrutura do Projeto

.
├── crawler/
│ ├── feed_reader.py # Pipeline de ingestão RSS
│ ├── tests/
│ └── README.md
│
├── etl/
│ ├── transform.py
│ ├── tests/
│ └── README.md
│
├── data/
│ ├── raw/ # Dados brutos (ignorados pelo Git)
│ └── .gitkeep
│
├── infra/
│ ├── bucket_setup.md
│ └── README.md
│
├── scripts/
│ └── upload_example.sh
│
├── docs/
│ └── README.md
│
├── .gitignore
└── README.md


---

## ▶️ Execução

O crawler possui um ponto de entrada definido:

```bash
python crawler/feed_reader.py

Ao executar:

    o RSS é coletado

    os dados são transformados

    um arquivo JSON é gerado em data/raw/

 Tecnologias Utilizadas

    Python 3

    requests

    feedparser

    JSON

    Git / GitHub

 Próximos Passos (Roadmap)

    Separação de módulos por camada (ingestão, transformação, persistência)

    Parametrização via variáveis de ambiente

    Integração com Spark para processamento em larga escala

    Orquestração com Airflow

    Dashboard para visualização das notícias

📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático, organização de código e versionamento adequado, servindo como base para pipelines de dados mais complexos em ambientes de produção.
