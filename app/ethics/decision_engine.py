def evaluate_prompt(prompt: str):
    prompt_lower = prompt.lower()

    risky_words = ["hack", "kill", "bomb", "fake id", "fraud"]

    if any(word in prompt_lower for word in risky_words):
        return {
            "decision": "BLOCK",
            "risk_score": 0.85,
            "risk_categories": ["Illegal / Harmful Activity"],
            "confidence": 0.90,
            "reason": "The prompt requests guidance for illegal or harmful activity",
            "safe_alternative": "I can provide legal, ethical, or educational information instead."
        }

    return {
        "decision": "ALLOW",
        "risk_score": 0.10,
        "risk_categories": [],
        "confidence": 0.95,
        "reason": "No ethical risk detected",
        "safe_alternative": "The prompt is safe to proceed."
    }
