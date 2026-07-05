from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "A modern flat illustration of SQL Joins with database tables, blue color theme, LinkedIn style"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response)