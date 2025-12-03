from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import QuestionRequest, ClassificationResponse, AnalysisResult
from services.llm_client import LLMClient
from services.bias_analyzer import BiasAnalyzer
import asyncio

app = FastAPI(title="IA Bias Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = LLMClient()
bias_analyzer = BiasAnalyzer()

@app.get("/")
def read_root():
    return {"message": "Welcome to the IA Bias Classifier API"}

@app.post("/classify", response_model=ClassificationResponse)
async def classify_question(request: QuestionRequest):
    results = []
    
    async def process_model(model):
        try:
            # 1. Generate response
            response_text = await llm_client.generate_response(model, request.question)
            
            # 2. Analyze bias
            analysis = await bias_analyzer.analyze_bias(response_text)
            
            return AnalysisResult(
                model_name=model,
                response_text=response_text,
                bias_score=analysis.get("bias_score", 0.0),
                bias_analysis=analysis.get("bias_analysis", "No analysis")
            )
        except Exception as e:
            return AnalysisResult(
                model_name=model,
                response_text=f"Error: {str(e)}",
                bias_score=0.0,
                bias_analysis="Error"
            )

    # Run for all models in parallel
    tasks = [process_model(model) for model in request.models]
    results = await asyncio.gather(*tasks)
    
    return ClassificationResponse(question=request.question, results=results)
