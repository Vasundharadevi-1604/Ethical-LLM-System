# ethical_pipeline.py
# ---------------------------------------------------
# Main Ethical LLM Pipeline
# ---------------------------------------------------

from llm_generator import generate_safe_response
from ethical_alternatives import generate_ethical_alternatives

# ---------------------------------------------------
# Final binary labels used across the system
# ---------------------------------------------------
FINAL_LABELS = ["Harmful", "Non-Harmful"]


def apply_harmfulness_rules(detected_domain: str) -> str:
    """
    Rule-based conversion to binary labels:
    Harmful / Non-Harmful
    """
    if detected_domain:
        return "Harmful"
    return "Non-Harmful"


def ethical_llm_pipeline(user_prompt: str) -> dict:

    # ---------------------------------------------------
    # Stage 1 – Risk Detection
    # ---------------------------------------------------
    unsafe_keywords = {
        "Weapons": ["bomb", "gun", "weapon", "explosive"],
        "Cybercrime": ["hack", "phishing", "malware"],
        "Drugs": ["cocaine", "heroin", "drug"],
        "Violence": ["kill", "murder", "attack"],
        "Self-Harm": ["suicide", "self harm"]
    }

    detected_domain = None
    detected_words = []

    for domain, keywords in unsafe_keywords.items():
        for word in keywords:
            if word in user_prompt.lower():
                detected_domain = domain
                detected_words.append(word)

    stage1 = {
        "stage": "Stage 1 – Risk Detection",
        "risk_status": "UNSAFE" if detected_domain else "SAFE",
        "detected_keywords": detected_words,
        "policy_domain": detected_domain or "General Knowledge",
        "intent_type": "Malicious" if detected_domain else "Benign",
        "confidence_score": 0.95 if detected_domain else 0.99
    }

    # ---------------------------------------------------
    # Stage 2 – Age Classification
    # ---------------------------------------------------
    stage2 = {
        "stage": "Stage 2 – Age Classification",
        "content_maturity": "Restricted" if detected_domain else "General",
        "minimum_age_required": "18+" if detected_domain else "All Ages",
        "audience_suitability": "Adults Only" if detected_domain else "General Audience",
        "restriction_reason": detected_domain
    }

    # ---------------------------------------------------
    # Stage 2.5 – Rule-Based Harmfulness Classification
    # ---------------------------------------------------
    harmfulness_label = apply_harmfulness_rules(detected_domain)

    stage2_5 = {
        "stage": "Stage 2.5 – Rule-Based Harmfulness Classification",
        "final_label": harmfulness_label,
        "label_space": FINAL_LABELS,
        "decision_basis": "Rule-based safety-first mapping"
    }

    # ---------------------------------------------------
    # Stage 3 – Prompt Decision
    # ---------------------------------------------------
    if harmfulness_label == "Harmful":
        stage3 = {
            "stage": "Stage 3 – Prompt Decision",
            "enforcement_action": "BLOCK_AND_REDIRECT",
            "model_execution": "DENIED",
            "ethical_strategy": "Provide safe educational alternatives"
        }

        ethical_alt = generate_ethical_alternatives(detected_domain)

        final_response = {
            "final_response_type": "UNSAFE",
            "intro": ethical_alt.get("intro", ""),
            "bullets": ethical_alt.get("bullets", []),
            "closing": ethical_alt.get("closing", "")
        }

    else:
        stage3 = {
            "stage": "Stage 3 – Prompt Decision",
            "enforcement_action": "ALLOW",
            "model_execution": "ALLOWED",
            "ethical_strategy": "Generate accurate and informative response"
        }

        final_response = generate_safe_response(user_prompt)

        # Safety net (never break Streamlit UI)
        if not isinstance(final_response, dict):
            final_response = {
                "final_response_type": "SAFE",
                "response": "Unable to generate response."
            }

    # ---------------------------------------------------
    # Final Output
    # ---------------------------------------------------
    return {
        "stage1": stage1,
        "stage2": stage2,
        "stage2_5": stage2_5,
        "stage3": stage3,
        "final_label": harmfulness_label,
        "final_response": final_response
    }
