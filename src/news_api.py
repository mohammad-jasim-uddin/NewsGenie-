from typing import Any, Dict, List
import requests
from src.config import get_settings

CATEGORY_MAP = {
    "technology": "technology",
    "finance": "business",
    "sports": "sports",
}

class NewsAPIClient:
    def __init__(self) -> None:
        self.settings = get_settings()

    def _headers(self) -> Dict[str, str]:
        return {"X-Api-Key": self.settings.news_api_key}

    def _normalize_articles(self, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        normalized = []
        for article in articles[:5]:
            normalized.append(
                {
                    "title": article.get("title", "Untitled"),
                    "source": (article.get("source") or {}).get("name", "Unknown source"),
                    "description": article.get("description", ""),
                    "url": article.get("url", ""),
                    "published_at": article.get("publishedAt", ""),
                }
            )
        return normalized

    def top_headlines(self, category: str = "technology") -> List[Dict[str, Any]]:
        if not self.settings.news_api_key:
            raise ValueError("NEWS_API_KEY is missing.")

        mapped_category = CATEGORY_MAP.get(category.lower(), "technology")
        url = f"{self.settings.news_api_base_url}/top-headlines"
        params = {
            "category": mapped_category,
            "language": "en",
            "pageSize": 5,
        }
        response = requests.get(url, headers=self._headers(), params=params, timeout=20)
        response.raise_for_status()
        payload = response.json()
        return self._normalize_articles(payload.get("articles", []))

    def search_news(self, query: str) -> List[Dict[str, Any]]:
        if not self.settings.news_api_key:
            raise ValueError("NEWS_API_KEY is missing.")

        url = f"{self.settings.news_api_base_url}/everything"
        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 5,
        }
        response = requests.get(url, headers=self._headers(), params=params, timeout=20)
        response.raise_for_status()
        payload = response.json()
        return self._normalize_articles(payload.get("articles", []))

def fetch_news_for_query(query: str, category: str) -> List[Dict[str, Any]]:
    client = NewsAPIClient()
    query_lower = query.lower()

    if any(term in query_lower for term in ["technology", "tech"]):
        return client.top_headlines("technology")
    if any(term in query_lower for term in ["finance", "financial", "market", "stock"]):
        return client.top_headlines("finance")
    if any(term in query_lower for term in ["sports", "sport", "football", "cricket", "tennis"]):
        return client.top_headlines("sports")

    try:
        return client.search_news(query)
    except Exception:
        return client.top_headlines(category or "technology")
