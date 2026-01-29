# RSS/API crawler placeholder
# Implement fetch_rss() and save_raw_json()

import requests # Biblioteca para fazer requisições HTTP
import feedparser # Biblioteca para interpretar RSS/XML
import json
from datetime import datetime, date

data_hoje = date.today().strftime('%Y-%m-%d')
nome_arquivo = 'data/raw/noticias_' + data_hoje + '.json'

#URL do feed RSS do G1
url = 'https://g1.globo.com/dynamo/rss2.xml'

# Coleta e processa notícias do RSS do G1
r = requests.get(url)

#Interpreta o RSS e transforma em estrutura Python
f = feedparser.parse(r.text)

# Seleciona a primeira notícia do feed
primeira_noticia = f.entries[0]

# Criar uma lista vazia para armazenar as notícias
lista_noticias = []

# Percorrer cada notícia em f.entries
for news in f.entries:
    # print(news.keys())
    # break

    data_publicada = news.get('published_parsed')

    if data_publicada:
        published_at = f"{data_publicada.tm_year}-{data_publicada.tm_mon:02d}-{data_publicada.tm_mday:02d}"
    else:
        published_at = None

    noticia = {
    "title": news['title'],
    "link": news['link'],
    "summary": news.get('summary'),
    "published_at" : published_at
    
}
    lista_noticias.append(noticia)
    

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(lista_noticias, arquivo, ensure_ascii=False, indent=4)
