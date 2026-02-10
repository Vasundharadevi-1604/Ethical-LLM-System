# 🛡️ The Ethical LLM System

A production-ready Ethical Decision Layer for Large Language Models (LLMs) that evaluates user prompts for safety, ethics, and intent before generating responses.

This system demonstrates how responsible AI can be designed, enforced, and deployed in real-world applications.

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

## ⚙️ System Components

The Ethical LLM System is designed as a **modular, production-oriented architecture**, where each component has a clear responsibility and can evolve independently.

### 1️⃣ User Interface (Streamlit – `app.py`)
- Acts as the **single entry point** for user interaction
- Accepts natural-language prompts
- Displays stage-wise ethical analysis
- Presents the final ethical response in an explainable format

This layer is intentionally kept lightweight to maintain **separation between UI and decision logic**.

---

### 2️⃣ Ethical Decision Layer (`ethical_layer/`)
This is the **core intelligence** of the system and functions as an ethical gatekeeper before any LLM response is generated.

**Key modules:**
- **`ethical_pipeline.py`**  
  Orchestrates the complete ethical decision flow, controls prompt routing, and determines SAFE vs UNSAFE outcomes.

- **`llm_generator.py`**  
  Generates responses **only for SAFE prompts** using controlled LLM access, preventing unchecked model execution.

- **`ethical_alternatives.py`**  
  Handles UNSAFE prompts by providing safe, constructive, and ethical guidance instead of harmful outputs.

This layer is designed to be **reusable as an ethical middleware** for other LLM-based systems.

---

### 3️⃣ Research & Evaluation Layer (`research/`)
- Contains experimentation and evaluation scripts
- Evaluates transformer-based models such as:
  - RoBERTa
  - XLM-R
  - SentiBERT
- Supports ensemble-based robustness analysis

This layer ensures ethical decisions are **data-driven and research-backed**.

---

### 4️⃣ Dataset Layer (`data/`)
- Includes curated malicious prompt datasets
- Represents real-world unsafe and adversarial inputs
- Used for testing, evaluation, and validation

Provides realistic grounding for ethical decision-making.

---

### 5️⃣ Documentation Layer (`docs/`)
- **`architecture.md`** – System architecture and ethical flow explanation
- **`project_report.docx`** – Complete academic and technical documentation

Supports transparency, explainability, and reviewability.

---

### 6️⃣ Deployment & Configuration
- **`requirements.txt`** – Dependency management
- **`Procfile`** – Render deployment configuration
- **`LICENSE`** – Open-source usage clarity (MIT License)

Enables **production deployment and maintainability**.

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
