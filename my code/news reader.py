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
    data = response.json()
    return data.get("articles", [])

if __name__ == "__main__":
    topics = ["technology", "sport", "weather", "health", "education"]
    for topic in topics:
        print(f"\n=== {topic.upper()} ===")
        articles = fetch_news(topic)
        if not articles:
            print("No news articles found.")
            continue
        for art in articles[:5]:
            print("-", art["title"], "(", art["source"]["name"], ")")
