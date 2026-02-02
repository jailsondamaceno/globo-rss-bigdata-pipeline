# Documentação do Crawler

Este módulo é responsável pela **ingestão de dados** a partir do feed RSS do G1 (Globo).

O crawler realiza a coleta do RSS via HTTP, interpreta o conteúdo XML e transforma cada item do feed em uma estrutura padronizada contendo título, link, resumo e data de publicação.  
Os dados resultantes são armazenados em formato JSON na camada de dados brutos (`data/raw`), com versionamento por data de execução.

## Execução

O módulo possui um ponto de entrada definido e pode ser executado diretamente:

```bash
python crawler/feed_reader.py
