from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GROQ = os.getenv("CHAVE_API_GROQ")
GROQ_MODEL = os.getenv("GROQ_MODEL")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions" 