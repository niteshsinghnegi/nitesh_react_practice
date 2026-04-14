import requests
from datetime import date, timedelta

API_KEY = "366bf8ffc6b5445786788f266101bfbf"

def fetch_news(topic):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "from": (date.today() - timedelta(days=1)).isoformat(),
        "to": date.today().isoformat(),
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["articles"]

if __name__ == "__main__":
    topics = ["technology", "health", "sports"]
    for topic in topics:
        print(f"\n=== {topic.upper()} ===")
        articles = fetch_news(topic)
        for art in articles[:5]:
            print("-", art["title"], "(", art["source"]["name"], ")")
