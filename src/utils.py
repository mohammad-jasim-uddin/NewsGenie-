import streamlit as st

def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = "technology"
    if "last_workflow_state" not in st.session_state:
        st.session_state.last_workflow_state = None
    if "show_debug" not in st.session_state:
        st.session_state.show_debug = False

def append_message(role: str, content: str) -> None:
    st.session_state.messages.append({"role": role, "content": content})
