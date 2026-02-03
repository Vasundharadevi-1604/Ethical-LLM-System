# System Architecture – The Ethical LLM System

## Overview

The Ethical LLM System is a **prompt-level ethical decision layer**
designed to analyze user inputs before they reach a Large Language Model (LLM).
The goal is to ensure **safe, responsible, and explainable AI outputs**.

The system follows a **modular, multi-stage architecture**, inspired by
real-world Responsible AI and Trust & Safety pipelines used in Big Tech.

---

## High-Level Architecture Diagram

```mermaid
flowchart TD

    U[User Prompt] --> UI[Streamlit Web UI]

    UI --> EP[Ethical Decision Pipeline]

    EP --> RD[Risk Detection Module]
    EP --> AC[Age / Intent Classification]
    EP --> ED[Ensemble Decision Logic]

    ED -->|SAFE| LLM[LLM / Gemini Generator]
    ED -->|UNSAFE| EA[Ethical Alternatives Module]

    LLM --> FR[Final Ethical Response]
    EA --> FR

    FR --> UI

