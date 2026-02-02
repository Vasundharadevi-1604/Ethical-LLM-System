import streamlit as st
import requests

# ---------------------------------------------------
# API Configuration (ONLY CHANGE: DATA SOURCE)
# ---------------------------------------------------
API_URL = "http://127.0.0.1:8000/moderate_prompt"
# Later (after deployment), replace with:
# API_URL = "https://your-fastapi-backend.onrender.com/moderate_prompt"

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Ethical LLM System",
    page_icon="🛡️",
    layout="centered"
)

# ---------------------------------------------------
# Header (Centered Title + Caption)
# ---------------------------------------------------
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0;">🛡️ Ethical LLM System</h1>
        <p style="font-size: 16px; color: gray; margin-top: 4px;">
            Multi-Stage Responsible AI Pipeline
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# Input Section (SMALL LABEL)
# ---------------------------------------------------
st.markdown(
    "<p style='font-size:16px; font-weight:600;'>Enter your prompt:</p>",
    unsafe_allow_html=True
)

user_prompt = st.text_area(
    "",
    placeholder="Ask any question here...",
    height=120
)

analyze_btn = st.button("Analyze")

# ---------------------------------------------------
# Pipeline Execution (NOW VIA FASTAPI)
# ---------------------------------------------------
if analyze_btn:

    if not user_prompt.strip():
        st.warning("Please enter a prompt before clicking Analyze.")
    else:
        try:
            response = requests.post(
                API_URL,
                json={"prompt": user_prompt},
                timeout=60
            )

            if response.status_code != 200:
                st.error("❌ Failed to connect to Ethical Decision Layer.")
                st.stop()

            result = response.json()

        except Exception as e:
            st.error("❌ Unable to reach Ethical Decision Layer.")
            st.stop()

        stage1 = result.get("stage1", {})
        stage2 = result.get("stage2", {})
        stage3 = result.get("stage3", {})
        final_response = result.get("final_response", {})

        st.divider()

        # ---------------------------------------------------
        # Stage 1 – Risk Detection
        # ---------------------------------------------------
        st.markdown("### Stage 1 – Risk Detection")
        st.json(stage1)

        # ---------------------------------------------------
        # Stage 2 – Age Classification
        # ---------------------------------------------------
        st.markdown("### Stage 2 – Age Classification")
        st.json(stage2)

        # ---------------------------------------------------
        # Stage 3 – Prompt Decision
        # ---------------------------------------------------
        st.markdown("### Stage 3 – Prompt Modification")
        st.json(stage3)

        st.divider()

        # ---------------------------------------------------
        # Final Ethical Response (BIG)
        # ---------------------------------------------------
        st.subheader("✅ Final Ethical Response")

        response_type = final_response.get("final_response_type")

        # -------------------------
        # SAFE PROMPT → Gemini Answer
        # -------------------------
        if response_type == "SAFE":
            st.markdown(final_response.get("response", "No response generated."))

        # -------------------------
        # UNSAFE PROMPT → Ethical Alternatives
        # -------------------------
        elif response_type == "UNSAFE":

            if final_response.get("intro"):
                st.write(final_response["intro"])

            bullets = final_response.get("bullets", [])
            for bullet in bullets:
                st.write(f"- {bullet}")

            if final_response.get("closing"):
                st.write(final_response["closing"])

        # -------------------------
        # Safety Fallback
        # -------------------------
        else:
            st.warning("Final ethical response could not be generated.")
