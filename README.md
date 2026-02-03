# 🛡️ The Ethical LLM System

A **production-deployed Ethical Decision Layer for Large Language Models (LLMs)** that performs prompt-level risk analysis and enforces responsible AI behavior before any response is generated.

---

## 🔗 Live Demo

👉 **Public Deployment:**  
https://ethical-llm-system.onrender.com

> A real-time Streamlit application demonstrating ethical prompt moderation and safe LLM response generation.

---

<h2>🚀 Project Overview</h2>

Large Language Models are powerful but can be misused through malicious, unsafe, or unethical prompts.  
**The Ethical LLM System** addresses this problem by introducing an **ethics-first decision layer** that evaluates user prompts *before* they reach the LLM.

The system:
- analyzes user intent,
- detects malicious or unsafe prompts,
- enforces ethical policies,
- generates safe alternatives when required,
- allows LLM responses only for approved prompts.

This project focuses on **Responsible AI, AI Safety, and Trust & Governance**.

---

## 🎯 Key Objectives

- Prevent harmful prompt execution
- Enforce ethical AI usage at prompt level
- Provide transparent and explainable decisions
- Demonstrate a deployable Responsible AI system
- Bridge research-backed evaluation with real-world deployment

---

## 🧠 System Architecture (High Level)


The architecture is designed to be:
- modular
- explainable
- deployment-friendly
- aligned with real-world Trust & Safety systems

📄 Full details: `docs/architecture.md`

---

## ⚙️ Core Components

### 1. Streamlit Interface (`app.py`)
- Public-facing UI
- Accepts user prompts
- Displays stage-wise ethical analysis
- Shows final ethical response

### 2. Ethical Decision Engine (`ethics_engine/`)
- `ethical_pipeline.py` – orchestrates ethical checks
- `llm_generator.py` – generates responses for SAFE prompts
- `ethical_alternatives.py` – handles UNSAFE prompts with safe guidance

This engine acts as the **ethical gatekeeper** of the system.

---

## 📊 Research & Evaluation

The ethical decision logic is supported by:
- curated malicious prompt datasets,
- transformer-based classifiers,
- ensemble model evaluation.

Multiple models (RoBERTa, XLM-R, SentiBERT) were evaluated, and an ensemble approach was selected to improve robustness and reduce false positives.

📄 Full evaluation and results are documented in the project report.

---

## 📁 Project Structure

```text
Ethical-LLM-System/
│
├── app.py
│
├── ethics_engine/
│   ├── ethical_pipeline.py
│   ├── llm_generator.py
│   └── ethical_alternatives.py
│
├── datasets/
│   └── MaliciousQueries.csv
│
├── research/
│   ├── run_experiment_final.py
│   └── bert_results_final.py
│
├── docs/
│   ├── architecture.md
│   └── project_report.pdf
│
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md


---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** (UI & deployment)
- **Gemini LLM** (controlled generation)
- **Transformers (BERT variants)** for classification
- **Render** for public deployment

---

## ▶️ Running Locally

```bash
git clone https://github.com/<your-username>/Ethical-LLM-System.git
cd Ethical-LLM-System

pip install -r requirements.txt
streamlit run app.py


```bash
git clone https://github.com/<your-username>/Ethical-LLM-System.git
cd Ethical-LLM-System

pip install -r requirements.txt
streamlit run app.py
