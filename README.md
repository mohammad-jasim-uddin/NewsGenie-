# NewsGenie

NewsGenie is a Streamlit + LangGraph project that combines:
- a conversational AI assistant for general questions
- real-time news retrieval by category or topic
- fallback external context when live news is unavailable
- graceful error handling and session-aware chat history

## Features

- Distinguishes between general, news, and mixed queries
- Retrieves real-time news for Technology, Finance, and Sports
- Uses a LangGraph workflow for routing and orchestration
- Supports fallback handling for API failures or empty results
- Provides a clean Streamlit chat-style user interface
- Includes a PowerPoint-style presentation script for LMS submission

## Project Structure

```text
newsgenie_project/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── src/
    ├── __init__.py
    ├── config.py
    ├── state.py
    ├── classifier.py
    ├── news_api.py
    ├── web_search.py
    ├── llm_engine.py
    ├── response_builder.py
    ├── workflow.py
    └── utils.py
```

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### install all below  

'''streamlit>=1.44.0
langgraph>=0.2.0
langchain>=0.3.0
langchain-openai>=0.3.0
requests>=2.32.0
python-dotenv>=1.0.1
'''

### 3. Configure environment variables

Copy `.env.example` to `.env` and set your keys:

```bash
cp .env.example .env
```

Required:
- `OPENAI_API_KEY`
- `NEWS_API_KEY`
- `TAVILY_API_KEY`

### 4. Run the app

```bash
streamlit run app.py
```

## Example queries

- What is artificial intelligence?
- Show me the latest technology news.
- Give me finance news updates.
- Explain inflation and give me the latest finance news.
- What is happening in sports today?

## Notes

This project is structured for coursework submission:
- modular source files
- explainable workflow
- clear separation of UI, routing, retrieval, and generation
- ready to demo after adding API keys
