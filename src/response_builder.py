from typing import Dict, List

def build_fallback_response(user_query: str, errors: List[str]) -> str:
    error_text = "\n".join(f"- {err}" for err in errors) if errors else "- Unknown error"
    return (
        "I could not fully complete the live request, but I can still help.\n\n"
        f"**Your query:** {user_query}\n\n"
        "**What happened:**\n"
        f"{error_text}\n\n"
        "Try one of these next steps:\n"
        "- Check whether your API keys are configured\n"
        "- Retry with a more specific topic\n"
        "- Ask for a general explanation instead of live news"
    )

def format_news_preview(articles: List[Dict]) -> str:
    if not articles:
        return "No recent articles were found."
    lines = []
    for article in articles:
        title = article.get("title", "Untitled")
        source = article.get("source", "Unknown source")
        description = article.get("description", "")
        lines.append(f"- **{title}** ({source})\n  - {description}")
    return "\n".join(lines)
