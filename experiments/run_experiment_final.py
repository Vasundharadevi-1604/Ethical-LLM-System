import os
import json
import pandas as pd
from transformers import pipeline

print(">>> RUN_EXPERIMENT_FINAL.PY STARTED <<<")

# ======================================================
# PATHS
# ======================================================

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "MaliciousQueries.csv")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "model_results")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "bert_results_final.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======================================================
# LOAD DATASET
# ======================================================

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)
print("Available columns:", list(df.columns))

PROMPT_COLUMN = "Question"

if PROMPT_COLUMN not in df.columns:
    raise ValueError(f"'{PROMPT_COLUMN}' column not found in CSV")

prompts = df[PROMPT_COLUMN].dropna().astype(str).tolist()
print(f"Total prompts loaded: {len(prompts)}")

# ======================================================
# LOAD MODELS (SAFE PIPELINE MODE)
# ======================================================

print("Loading models...")
print("Device set to use cpu")

twitter_roberta = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=-1
)

twitter_xlm = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    device=-1
)

sentibert = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    device=-1
)

print("Models loaded successfully.")
print("Starting inference...")

# ======================================================
# INFERENCE
# ======================================================

results = []

for idx, text in enumerate(prompts, start=1):
    try:
        r1 = twitter_roberta(text)[0]
        r2 = twitter_xlm(text)[0]
        r3 = sentibert(text)[0]

        results.append({
            "prompt_id": idx,
            "prompt": text,

            "twitter_roberta_label": r1["label"],
            "twitter_roberta_score": float(r1["score"]),

            "twitter_xlm_label": r2["label"],
            "twitter_xlm_score": float(r2["score"]),

            "sentibert_label": r3["label"],
            "sentibert_score": float(r3["score"])
        })

        if idx % 10 == 0:
            print(f"Processed {idx}/{len(prompts)} prompts")

    except Exception as e:
        print(f"Error at prompt {idx}: {e}")

# ======================================================
# SAVE RESULTS
# ======================================================

print("Saving results...")
print("Total records:", len(results))
print("Output file:", OUTPUT_FILE)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print("=" * 60)
print("EXPERIMENT COMPLETED SUCCESSFULLY")
print(f"Results saved to: {OUTPUT_FILE}")
print("=" * 60)
