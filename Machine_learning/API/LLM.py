import os
from dotenv import load_dotenv
from google import genai

load_dotenv() #loads the .env file

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Tell me a dad joke"
)

print(response.text)