# NewsGenie PowerPoint-Style Presentation Script

## Slide 1 – Title
**Title:** NewsGenie – An AI-Powered Information and News Assistant

**Speaker notes:**  
Good morning everyone. Today I am presenting NewsGenie, an AI-powered assistant that combines general question answering with real-time news retrieval. The project uses Streamlit for the interface, LangGraph for routing and workflow management, a large language model for response generation, and a live news API for current updates.

---

## Slide 2 – Problem Statement
**Slide points:**
- Information overload
- Fragmented news sources
- Risk of misinformation
- Need for one unified assistant

**Speaker notes:**  
Users often need to switch between search engines, news platforms, and chatbots just to get a complete answer. This makes information access slow, fragmented, and sometimes unreliable. NewsGenie solves this by unifying general AI assistance and real-time news into one platform.

---

## Slide 3 – Project Objective
**Slide points:**
- Answer general queries
- Fetch current news
- Distinguish query types
- Use workflow orchestration
- Deliver a simple user interface

**Speaker notes:**  
The main goal of NewsGenie is to build a single platform that can answer normal questions while also retrieving fresh news updates. The system must understand the user’s intent, choose the correct processing route, and return a clear answer through an easy Streamlit interface.

---

## Slide 4 – Core Features
**Slide points:**
- AI chatbot
- Real-time news API
- Web search fallback
- LangGraph routing
- Streamlit frontend

**Speaker notes:**  
The system has five key parts. First, a chatbot handles natural language input. Second, a news API brings in current headlines. Third, a fallback search module helps when live news is unavailable. Fourth, LangGraph controls the workflow. Fifth, Streamlit provides the user interface.

---

## Slide 5 – Query Types
**Slide points:**
- General query
- News query
- Mixed query

**Speaker notes:**  
The system classifies user input into three categories. A general query is something like “What is AI?” A news query is something like “Show me the latest sports news.” A mixed query combines explanation and current information, such as “Explain inflation and give me finance news.”

---

## Slide 6 – Workflow Architecture
**Slide points:**
- Input node
- Classifier node
- News retrieval node
- Fallback search node
- Final response node

**Speaker notes:**  
LangGraph manages the logic as a state-based workflow. The user input first goes to the classifier. Depending on the query type, the graph either sends the request directly to the language model or routes it to the news retrieval process. If news is unavailable, the system triggers a fallback search before generating the final answer.

---

## Slide 7 – Streamlit Interface
**Slide points:**
- Category selector
- Chat input
- Chat history
- Debug/workflow view
- Session state support

**Speaker notes:**  
The frontend is built in Streamlit. Users can choose a category like technology, finance, or sports. They can type questions in a chat box, view previous responses, and clear the session if needed. A debug panel can also show the internal workflow state for demonstration purposes.

---

## Slide 8 – Real-Time News Integration
**Slide points:**
- API-based headline retrieval
- Category mapping
- Top 5 articles
- Topic search support

**Speaker notes:**  
The news module connects to a news API and fetches recent headlines by category. Technology is mapped directly, finance uses the business category, and sports is handled as a standard sports feed. If the user asks about a specific topic, the system can also perform keyword-based news search.

---

## Slide 9 – Fallback and Error Handling
**Slide points:**
- Missing API keys
- Failed API calls
- No news found
- Fallback external context
- Graceful user messages

**Speaker notes:**  
A major requirement of the project is reliable behavior. If API keys are missing, the app explains what is wrong. If a live news request fails or returns no results, the workflow switches to fallback context. This ensures the user still receives a helpful answer instead of a broken experience.

---

## Slide 10 – Sample Outputs
**Slide points:**
- Technology headlines
- Finance updates
- Sports summaries

**Speaker notes:**  
The assistant can return sample outputs such as technology headlines, finance updates, and sports summaries. In the live app, the language model summarizes the articles into a short, readable response for the user. This keeps the interface simple and informative.

---

## Slide 11 – Technologies Used
**Slide points:**
- Python
- Streamlit
- LangGraph
- LangChain OpenAI
- Requests
- dotenv

**Speaker notes:**  
The implementation uses Python as the main language. Streamlit powers the frontend, LangGraph manages the stateful workflow, LangChain OpenAI handles model access, Requests handles API communication, and dotenv manages environment variables securely.

---

## Slide 12 – Project Structure
**Slide points:**
- app.py
- src/classifier.py
- src/news_api.py
- src/workflow.py
- src/llm_engine.py
- presentation_script.md

**Speaker notes:**  
The codebase is modular. Each responsibility is separated into its own file. This improves maintainability, readability, and makes the project easier to explain during submission or viva presentation.

---

## Slide 13 – Learning Outcomes
**Slide points:**
- Conversational AI design
- API integration
- Workflow orchestration
- UI deployment
- Error handling

**Speaker notes:**  
This project demonstrates the ability to build a complete AI system rather than just a chatbot. It combines interface design, routing logic, external APIs, language models, and fault handling into one coherent application.

---

## Slide 14 – Future Enhancements
**Slide points:**
- Personalized news feeds
- Credibility scoring
- Multilingual support
- Persistent chat history
- Advanced search integration

**Speaker notes:**  
In future versions, NewsGenie could support personalized recommendations, fact-check scoring, multilingual output, persistent user memory, and stronger search providers. These would make the system more production-ready.

---

## Slide 15 – Conclusion
**Slide points:**
- Unified AI assistant
- Current news + general answers
- Reliable workflow
- Simple user experience

**Speaker notes:**  
In conclusion, NewsGenie is a unified AI assistant that simplifies information access by combining general conversational intelligence with real-time news retrieval. It shows how modern AI tools can be integrated into a practical and user-friendly solution.

---

## Slide 16 – Demo Script
**Demo flow:**
1. Ask: “What is artificial intelligence?”
2. Ask: “Show me the latest technology news.”
3. Ask: “Explain inflation and give me finance news.”
4. Remove an API key and show fallback handling.

**Speaker notes:**  
For the demo, I would first show a general question, then a category-based news query, then a mixed query, and finally demonstrate fallback behavior by simulating an API issue. This proves the system works across the main project requirements.
