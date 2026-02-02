# RSS/API crawler placeholder
# Implement fetch_rss() and save_raw_json()

import requests
import feedparser 
import json
from datetime import datetime, date

#Função de coleta: recebe URL, retorna RSS
def coleta_rss(url):
    r = requests.get(url)
    return r.text


# Transforma RSS bruto em lista de notícias estruturadas
def transforma_rss(rss_text):
    feed = feedparser.parse(rss_text)

    lista_noticias = []

    for news in feed.entries:
        data_publicada = news.get("published_parsed")

        if data_publicada:
            published_at = (
                f"{data_publicada.tm_year}-"
                f"{data_publicada.tm_mon:02d}-"
                f"{data_publicada.tm_mday:02d}"
            )
        else:
            published_at = None

        noticia = {
            "title": news["title"],
            "link": news["link"],
            "summary": news.get("summary"),
            "published_at": published_at
        }

        lista_noticias.append(noticia)

    return lista_noticias

# # ===== Persistência =====
def persistencia_rss(lista_noticias, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista_noticias, arquivo, ensure_ascii=False, indent=4)

def main():
    url = "https://g1.globo.com/dynamo/rss2.xml"

    rss_text = coleta_rss(url)
    lista_noticias = transforma_rss(rss_text)

    data_hoje = date.today().strftime("%Y-%m-%d")
    nome_arquivo = f"data/raw/noticias_{data_hoje}.json"

    persistencia_rss(lista_noticias, nome_arquivo)

if __name__ == "__main__":
    main()

