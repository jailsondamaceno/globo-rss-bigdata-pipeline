# RSS/API crawler placeholder
# Implement fetch_rss() and save_raw_json()

import requests # Biblioteca para fazer requisições HTTP
import feedparser # Biblioteca para interpretar RSS/XML
import json
from datetime import datetime, date

data_hoje = date.today().strftime('%Y-%m-%d')
nome_arquivo = 'data/raw/noticias_' + data_hoje + '.json'

# ===== Coleta =====
url = 'https://g1.globo.com/dynamo/rss2.xml'

r = requests.get(url)

# ===== Transformação =====
f = feedparser.parse(r.text)

primeira_noticia = f.entries[0]

lista_noticias = []

# ===== Persistência =====
for news in f.entries:
    
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
