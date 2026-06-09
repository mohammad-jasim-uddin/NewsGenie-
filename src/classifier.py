from typing import Literal

QueryType = Literal["general", "news", "mixed"]

NEWS_KEYWORDS = {
    "news", "headline", "headlines", "latest", "today", "update", "updates",
    "current", "breaking", "technology", "tech", "finance", "financial",
    "sports", "sport", "market", "stock"
}

EXPLANATION_KEYWORDS = {
    "explain", "what is", "how does", "define", "tell me about", "why"
}

def classify_query(query: str, selected_category: str = "") -> QueryType:
    query_lower = query.strip().lower()
    has_news_signal = any(keyword in query_lower for keyword in NEWS_KEYWORDS)
    has_explanation_signal = any(keyword in query_lower for keyword in EXPLANATION_KEYWORDS)

    if selected_category and selected_category.lower() in query_lower:
        has_news_signal = True

    if has_news_signal and has_explanation_signal:
        return "mixed"
    if has_news_signal:
        return "news"
    return "general"
