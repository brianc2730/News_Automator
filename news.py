import requests
import webbrowser
import datetime
import os
from decouple import config

url = "https://newsapi.org/v2/top-headlines"

params = {
    "apiKey": config("API_KEY"),
    "country": "us",
    "category": "technology",
    "q": "AI",
}

response = requests.get(url, params=params)

articles = response.json()["articles"]
ai_articles = {}

for article in articles:
    if "AI" in article["title"]:
        ai_articles[article.get("title")] = article.get("url")

for link in ai_articles.values():
    webbrowser.open_new_tab(link)

news_path = os.path.join(os.path.expanduser("~"), "Documents/News_Articles/")

if not os.path.isdir(news_path):
    os.mkdir(news_path)

today_folder = os.path.join(news_path, str(datetime.date.today()))

if not os.path.isdir(today_folder):
    os.mkdir(today_folder)

for ai_article in ai_articles:
    article_path = os.path.join(today_folder, f"{ai_article}.url")

    with open(article_path, "w") as f:
        f.writelines(["[InternetShortcut]\n", f"URL={ai_articles[ai_article]}"])
