from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    openai_api_key: str
    news_api_key: str
    tavily_api_key: str
    model_name: str
    news_api_base_url: str

def get_settings() -> Settings:
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        news_api_key=os.getenv("NEWS_API_KEY", ""),
        tavily_api_key=os.getenv("TAVILY_API_KEY", ""),
        model_name=os.getenv("MODEL_NAME", "gpt-4.1-mini"),
        news_api_base_url=os.getenv("NEWS_API_BASE_URL", "https://newsapi.org/v2"),
    )
