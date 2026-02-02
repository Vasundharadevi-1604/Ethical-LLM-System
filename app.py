import streamlit as st
from ethical_pipeline import ethical_llm_pipeline

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
# Input Section
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
# Pipeline Execution (ALL INSIDE STREAMLIT)
# ---------------------------------------------------
if analyze_btn:

    if not user_prompt.strip():
        st.warning("Please enter a prompt before clicking Analyze.")
        st.stop()

    # Run Ethical LLM Pipeline
    with st.spinner("Running ethical analysis..."):
        result = ethical_llm_pipeline(user_prompt)

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
    # Final Ethical Response
    # ---------------------------------------------------
    st.subheader("✅ Final Ethical Response")

    response_type = final_response.get("final_response_type")

    # SAFE PROMPT → LLM RESPONSE
    if response_type == "SAFE":
        st.markdown(final_response.get("response", "No response generated."))

    # UNSAFE PROMPT → ETHICAL ALTERNATIVES
    elif response_type == "UNSAFE":

        if final_response.get("intro"):
            st.write(final_response["intro"])

        for bullet in final_response.get("bullets", []):
            st.write(f"- {bullet}")

        if final_response.get("closing"):
            st.write(final_response["closing"])

    else:
        st.warning("Final ethical response could not be generated.")
