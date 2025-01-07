import os

from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env


POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:pass@localhost/dbname")
APP_DEBUG = os.getenv("APP_DEBUG", "False").lower() == "true"
