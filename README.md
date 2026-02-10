# 🛡️ The Ethical LLM System

A production-ready Ethical Decision Layer for Large Language Models (LLMs) that evaluates user prompts for safety, ethics, and intent before generating responses.

This system demonstrates how responsible AI can be designed, enforced, and deployed in real-world applications.


---

🌐 **Live Deployment:**  
https://ethical-llm-system.onrender.com


---

## 🚀 Project Overview

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

## 🏗️ High-Level Architecture

```text
User Prompt
│
▼
Ethical Decision Engine
│
├── Stage 1: Risk Detection
├── Stage 2: Safety Classification
├── Stage 3: Ethical Decision
│
├── SAFE → LLM Response Generation
└── UNSAFE → Ethical Alternatives & Guidance
```

---

## ⚙️  System Components

### 1️⃣ Streamlit Interface (`app.py`)
- Clean UI for user interaction
- Displays stage-wise ethical analysis
- Presents final ethical responses clearly

---

### 2️⃣ Ethical Decision Layer (`ethical_layer/`)

| Module | Responsibility |
|------|---------------|
| `ethical_pipeline.py` | Orchestrates the complete ethical decision flow |
| `llm_generator.py` | Generates responses only for SAFE prompts |
| `ethical_alternatives.py` | Provides constructive guidance for UNSAFE prompts |

This layer is modular and can be **reused as an ethical middleware** in other AI systems.

---

### 3️⃣ Research & Evaluation (`research/`)
- Malicious prompt experimentation
- Transformer-based classification models
- Ensemble evaluation for robustness

Models evaluated include:
- RoBERTa
- XLM-R
- SentiBERT

---

### 4️⃣ Dataset (`data/`)
- Curated malicious prompt dataset
- Used to evaluate unsafe and adversarial inputs

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
├── ethical_layer/
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
```

---

## 🛠️ Technologies Used

- Python
- Streamlit (UI & deployment)
- Gemini LLM (controlled generation)
- Transformers (BERT variants) for classification
- Render for public deployment

---

## 🌍 Deployment

- Publicly deployed using **Render**
- Fully accessible via web browser
- Demonstrates real-world AI system deployment

🔗 **Live URL:** https://ethical-llm-system.onrender.com

---

## ▶️ Running Locally

```bash
git clone https://github.com/your-username/Ethical-LLM-System.git
cd Ethical-LLM-System

pip install -r requirements.txt
streamlit run app.py
