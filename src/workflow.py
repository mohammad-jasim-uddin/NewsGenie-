from langgraph.graph import END, START, StateGraph

from src.classifier import classify_query
from src.llm_engine import generate_response
from src.news_api import fetch_news_for_query
from src.response_builder import build_fallback_response
from src.state import NewsGenieState
from src.web_search import external_context_search

def classify_node(state: NewsGenieState) -> dict:
    return {
        "query_type": classify_query(
            state["user_query"],
            state.get("selected_category", ""),
        )
    }

def route_after_classification(state: NewsGenieState) -> str:
    return state["query_type"]

def general_node(state: NewsGenieState) -> dict:
    try:
        return {
            "final_answer": generate_response(
                user_query=state["user_query"],
                query_type=state["query_type"],
                news_articles=[],
                search_results=[],
            )
        }
    except Exception as exc:
        errors = state.get("errors", []) + [f"General query handling failed: {exc}"]
        return {
            "errors": errors,
            "final_answer": build_fallback_response(state["user_query"], errors),
        }

def news_node(state: NewsGenieState) -> dict:
    try:
        return {
            "news_articles": fetch_news_for_query(
                state["user_query"],
                state.get("selected_category", "technology"),
            )
        }
    except Exception as exc:
        return {"errors": state.get("errors", []) + [f"News retrieval failed: {exc}"]}

def mixed_node(state: NewsGenieState) -> dict:
    try:
        return {
            "news_articles": fetch_news_for_query(
                state["user_query"],
                state.get("selected_category", "technology"),
            )
        }
    except Exception as exc:
        return {"errors": state.get("errors", []) + [f"Mixed-query news retrieval failed: {exc}"]}

def fallback_search_node(state: NewsGenieState) -> dict:
    try:
        return {"search_results": external_context_search(state["user_query"])}
    except Exception as exc:
        return {"errors": state.get("errors", []) + [f"Fallback external search failed: {exc}"]}

def final_response_node(state: NewsGenieState) -> dict:
    try:
        search_results = state.get("search_results", [])
        if not state.get("news_articles") and state["query_type"] in {"news", "mixed"}:
            search_results = search_results or external_context_search(state["user_query"])

        return {
            "search_results": search_results,
            "final_answer": generate_response(
                user_query=state["user_query"],
                query_type=state["query_type"],
                news_articles=state.get("news_articles", []),
                search_results=search_results,
            ),
        }
    except Exception as exc:
        errors = state.get("errors", []) + [f"Final response generation failed: {exc}"]
        return {
            "errors": errors,
            "final_answer": build_fallback_response(state["user_query"], errors),
        }

def should_fallback(state: NewsGenieState) -> str:
    return "fallback_search" if not state.get("news_articles") else "final_response"

def build_graph():
    graph = StateGraph(NewsGenieState)

    graph.add_node("classify", classify_node)
    graph.add_node("general", general_node)
    graph.add_node("news", news_node)
    graph.add_node("mixed", mixed_node)
    graph.add_node("fallback_search", fallback_search_node)
    graph.add_node("final_response", final_response_node)

    graph.add_edge(START, "classify")

    graph.add_conditional_edges(
        "classify",
        route_after_classification,
        {
            "general": "general",
            "news": "news",
            "mixed": "mixed",
        },
    )

    graph.add_edge("general", END)
    graph.add_conditional_edges("news", should_fallback)
    graph.add_conditional_edges("mixed", should_fallback)
    graph.add_edge("fallback_search", "final_response")
    graph.add_edge("final_response", END)

    return graph.compile()
