import streamlit as st

from src.config import get_settings
from src.workflow import build_graph
from src.utils import init_session_state, append_message

st.set_page_config(page_title="NewsGenie", page_icon="📰", layout="wide")

settings = get_settings()
graph = build_graph()

def render_sidebar() -> None:
    st.sidebar.title("NewsGenie Controls")
    st.sidebar.markdown("Select a news category and app options.")

    st.session_state.selected_category = st.sidebar.selectbox(
        "News category",
        options=["technology", "finance", "sports"],
        index=["technology", "finance", "sports"].index(
            st.session_state.get("selected_category", "technology")
        ),
    )

    st.sidebar.checkbox(
        "Show workflow details",
        value=st.session_state.get("show_debug", False),
        key="show_debug",
    )

    if st.sidebar.button("Clear chat history"):
        st.session_state.messages = []
        st.session_state.last_workflow_state = None
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.caption("Environment status")
    st.sidebar.write(f"Model: `{settings.model_name}`")
    st.sidebar.write("News API key loaded: " + ("Yes" if settings.news_api_key else "No"))
    st.sidebar.write("OpenAI API key loaded: " + ("Yes" if settings.openai_api_key else "No"))
    st.sidebar.write("Tavily API key loaded: " + ("Yes" if settings.tavily_api_key else "No"))

def render_chat_history() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def process_user_input(user_prompt: str) -> None:
    append_message("user", user_prompt)

    state = {
        "user_query": user_prompt,
        "chat_history": st.session_state.messages[:-1],
        "selected_category": st.session_state.selected_category,
        "query_type": "",
        "news_articles": [],
        "search_results": [],
        "general_answer": "",
        "final_answer": "",
        "errors": [],
    }

    try:
        with st.spinner("NewsGenie is thinking..."):
            result = graph.invoke(state)
    except Exception as exc:
        result = {
            "final_answer": (
                "Something went wrong while processing your request.\n\n"
                f"Details: {exc}"
            ),
            "errors": [str(exc)],
        }

    st.session_state.last_workflow_state = result
    assistant_text = result.get("final_answer", "Sorry, I could not generate a response.")
    append_message("assistant", assistant_text)

    with st.chat_message("assistant"):
        st.markdown(assistant_text)

def main() -> None:
    init_session_state()

    st.title("📰 NewsGenie --- AI-Powered News & Information Assistant")
    st.caption("An AI-powered information and news assistant built with Streamlit and LangGraph.")

    render_sidebar()
    render_chat_history()

    user_prompt = st.chat_input("Ask a general question or request the latest news...")
    if user_prompt:
        with st.chat_message("user"):
            st.markdown(user_prompt)
        process_user_input(user_prompt)

    if st.session_state.get("show_debug") and st.session_state.get("last_workflow_state"):
        with st.expander("Workflow state"):
            st.json(st.session_state.last_workflow_state)

if __name__ == "__main__":
    main()
