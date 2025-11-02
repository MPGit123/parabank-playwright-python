from utils import load_env
import os

load_env()

class Settings:
    browser: str = os.getenv("BROWSER")
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    default_timeout_ms: int = int(os.getenv("DEAULT_TIMEOUT_MS"))
    base_url: str = os.getenv("BASE_URL")

settings = Settings()