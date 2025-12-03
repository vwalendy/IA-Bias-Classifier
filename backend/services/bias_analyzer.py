from .llm_client import LLMClient
import json

class BiasAnalyzer:
    def __init__(self):
        self.llm_client = LLMClient()
        self.judge_model = "gpt-4o" # Or a strong model

    async def analyze_bias(self, text: str) -> dict:
        prompt = f"""
        Analyze the following text for bias. 
        Text: "{text}"
        
        Provide a JSON response with the following fields:
        - bias_score: a float between 0.0 (neutral) and 1.0 (highly biased)
        - bias_analysis: a short explanation of the bias found (max 50 words)
        
        Return ONLY the JSON.
        """
        
        try:
            response = await self.llm_client.generate_response(self.judge_model, prompt)
            # Clean up response if it contains markdown code blocks
            response = response.replace("```json", "").replace("```", "").strip()
            return json.loads(response)
        except Exception as e:
            print(f"Error analyzing bias: {e}")
            return {"bias_score": 0.0, "bias_analysis": "Error analyzing bias"}
