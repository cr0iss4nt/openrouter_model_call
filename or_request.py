import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def call_model(prompt):
    response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": f"{os.getenv('OPENROUTER_MODEL')}",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 2000
            })
        )
    return response
