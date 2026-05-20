import os
import requests

from dotenv import load_dotenv

# Load .env
load_dotenv()

# =========================================
# AI RESPONSE FUNCTION
# =========================================

def get_ai_response(user_input):

    try:

        api_key = os.getenv("OPENROUTER_API_KEY")

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {

            "Authorization": f"Bearer {api_key}",

            "Content-Type": "application/json"
        }

        data = {

            "model": "meta-llama/llama-3.1-8b-instruct",

            "messages": [

                {
                    "role": "system",
                    "content": "You are an AI Business Assistant."
                },

                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        result = response.json()

        print(result)

        if "choices" in result:

            return result["choices"][0]["message"]["content"]

        elif "error" in result:

            return f"API Error: {result['error']['message']}"

        else:

            return "No response generated."

    except Exception as e:

        return f"Error: {str(e)}"