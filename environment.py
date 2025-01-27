import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_ID = os.getenv("MODEL_ID", "")

def get_config():
    return {
        "api_key": GROQ_API_KEY,
        "model_id": MODEL_ID
    }
