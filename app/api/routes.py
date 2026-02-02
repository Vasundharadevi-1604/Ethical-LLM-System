from fastapi import APIRouter
from ethical_pipeline import ethical_llm_pipeline

router = APIRouter()

@router.post("/moderate_prompt")
def moderate_prompt(request: dict):
    prompt = request.get("prompt", "")

    # 🔥 CALL YOUR ORIGINAL PIPELINE
    result = ethical_llm_pipeline(prompt)

    # 🔥 RETURN IT AS-IS (IMPORTANT)
    return result
