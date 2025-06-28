import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Dynamic Risk Assessment Agent", layout="centered")
st.title("📉 Dynamic Risk Assessment Agent")

st.markdown("Evaluate the risk profile of an insurance applicant.")

# Load model once
@st.cache_resource
def load_risk_model():
    return pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

model = load_risk_model()

# User Inputs
age = st.slider("🎂 Age", 18, 75, 30)
income = st.selectbox("💰 Income Level", ["<5 Lakhs", "5–10 Lakhs", "10–20 Lakhs", "20+ Lakhs"])
claim_amount = st.number_input("💵 Previous Claim Amount (in ₹)", min_value=0)
claim_count = st.slider("📁 Past Claims Count", 0, 5, 0)

# Prompt generation
if st.button("Evaluate Risk"):
    prompt = f"""
You are a smart insurance risk evaluation assistant.

Based on the applicant's profile, classify the risk as: Low Risk, Moderate Risk, or High Risk. Be concise.

Profile:
Age: {age}
Income: {income}
Claim Amount: ₹{claim_amount}
Past Claims: {claim_count}

Risk Evaluation:"""

    with st.spinner("🧠 Evaluating risk..."):
        try:
            response = model(
                prompt,
                max_new_tokens=60,
                temperature=0.3,      # lower = more consistent/faster
                do_sample=False,      # disables randomness
                top_p=0.9,
                truncation=True
            )[0]["generated_text"]

            # Extract answer
            if "Risk Evaluation:" in response:
                risk = response.split("Risk Evaluation:")[-1].strip().split("\n")[0]
            else:
                risk = response.strip()

            st.success("✅ Risk Evaluation Result:")
            st.write(risk)

        except Exception as e:
            st.error(f"❌ Evaluation failed: {str(e)}")
