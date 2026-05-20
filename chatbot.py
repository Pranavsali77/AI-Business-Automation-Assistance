import os
import requests

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
                    "content": """
                    You are an AI-Powered Business Automation Assistant.

                    Help users with:
                    - AI automation
                    - business workflows
                    - chatbot systems
                    - customer support
                    - lead management

                    Keep responses professional and easy to understand.
                    """
                },

                {
                    "role": "user",
                    "content": user_input
                }
            ],

            "temperature": 0.7,
            "max_tokens": 1000
        }

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        result = response.json()

        if "choices" in result:

            return result["choices"][0]["message"]["content"]

        elif "error" in result:

            return f"API Error: {result['error']['message']}"

        else:

            return "No response generated."

    except Exception as e:

        return f"Error: {str(e)}"