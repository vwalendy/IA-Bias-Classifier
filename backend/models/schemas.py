from pydantic import BaseModel
from typing import List, Optional

class QuestionRequest(BaseModel):
    question: str
    models: List[str] = ["gpt-3.5-turbo", "gpt-4o"]

class AnalysisResult(BaseModel):
    model_name: str
    response_text: str
    bias_score: float  # 0.0 to 1.0 (0 = neutral, 1 = biased)
    bias_analysis: str

class ClassificationResponse(BaseModel):
    question: str
    results: List[AnalysisResult]
