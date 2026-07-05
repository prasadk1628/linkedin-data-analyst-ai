import json


def parse_response(response_text: str):
    """
    Convert Gemini JSON response into a Python dictionary.
    """

    return json.loads(response_text)