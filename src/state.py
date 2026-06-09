from typing import Any, Dict, List, TypedDict

class NewsGenieState(TypedDict):
    user_query: str
    chat_history: List[Dict[str, str]]
    selected_category: str
    query_type: str
    news_articles: List[Dict[str, Any]]
    search_results: List[Dict[str, Any]]
    general_answer: str
    final_answer: str
    errors: List[str]
