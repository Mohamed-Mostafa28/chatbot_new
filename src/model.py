from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


# Set your Groq API key
api="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"
# api=os.getenv("Groq_API_key")

# Load model
LLM_Model = ChatGroq(
                    model="llama-3.1-70b-versatile",
                    groq_api_key=api,
                    max_tokens=500,
                    temperature=0.2,
                    # temperature=0.3,
                )
print("xxxxx model xxxxx")
