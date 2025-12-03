import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    async def generate_response(self, model: str, prompt: str) -> str:
        if "gpt" in model:
            if not self.openai_api_key:
                return "Error: OpenAI API key not configured."
            
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
            
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers=headers,
                        json=data,
                        timeout=60.0
                    )
                    response.raise_for_status()
                    result = response.json()
                    return result["choices"][0]["message"]["content"]
                except Exception as e:
                    return f"Error calling OpenAI: {str(e)}"

        elif "claude" in model:
            # Placeholder for Anthropic via httpx if needed later
            return "Error: Anthropic support temporarily disabled due to library issues."
        else:
            raise ValueError(f"Unsupported model: {model}")
