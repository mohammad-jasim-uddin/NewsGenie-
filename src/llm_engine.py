from typing import Dict, List
from langchain_openai import ChatOpenAI
from src.config import get_settings

SYSTEM_PROMPT = """You are NewsGenie, an AI-powered news and information assistant.

Rules:
1. Be concise, clear, and professional.
2. If real-time news articles are provided, summarize them in bullet form.
3. If no live news is available, explain that clearly and offer a fallback response.
4. For general questions, answer directly and accurately.
5. For mixed questions, first explain the concept, then present the current news.
"""

def get_model() -> ChatOpenAI:
    settings = get_settings()
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is missing.")
    return ChatOpenAI(
        model=settings.model_name,
        temperature=0.2,
        api_key=settings.openai_api_key,
    )

def build_prompt(
    user_query: str,
    query_type: str,
    news_articles: List[Dict],
    search_results: List[Dict],
) -> str:
    sections = [
        SYSTEM_PROMPT,
        f"Query type: {query_type}",
        f"User query: {user_query}",
    ]

    if news_articles:
        sections.append("News articles:")
        for idx, article in enumerate(news_articles, start=1):
            sections.append(
                f"{idx}. Title: {article.get('title')} | "
                f"Source: {article.get('source')} | "
                f"Published: {article.get('published_at')} | "
                f"Description: {article.get('description')} | "
                f"URL: {article.get('url')}"
            )

    if search_results:
        sections.append("External search results:")
        for idx, result in enumerate(search_results, start=1):
            sections.append(
                f"{idx}. Title: {result.get('title')} | "
                f"Snippet: {result.get('snippet')} | "
                f"URL: {result.get('url')}"
            )

    sections.append("Generate the final user-facing response in clean markdown.")
    return "\n".join(sections)

def generate_response(
    user_query: str,
    query_type: str,
    news_articles: List[Dict],
    search_results: List[Dict],
) -> str:
    model = get_model()
    prompt = build_prompt(user_query, query_type, news_articles, search_results)
    response = model.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)
