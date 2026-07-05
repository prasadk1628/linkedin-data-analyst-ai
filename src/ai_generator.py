from google import genai
from src.config import GEMINI_API_KEY, MODEL_NAME
from src.json_parser import parse_response
from src.validators import validate_post

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_post(topic: str):

    with open("prompts/linkedin_prompt.txt", encoding="utf-8") as file:
        prompt = file.read().format(topic=topic)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    post = parse_response(response.text)

    validate_post(post)
    
    return post