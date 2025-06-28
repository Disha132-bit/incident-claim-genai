import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.claim_parser import extract_claim_info
from backend.fraud_checker import check_for_fraud
from backend.summarizer import generate_summary_with_llama

st.set_page_config(page_title="Upload Insurance Claims", layout="centered")
st.title("📂 Upload Insurance Claim Files")
st.markdown("Upload .txt files to extract details, detect fraud, and generate GenAI summaries.")

uploaded_files = st.file_uploader("Upload TXT Claim Files", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    if "uploaded_claims" not in st.session_state:
        st.session_state.uploaded_claims = []

    for file in uploaded_files:
        st.markdown("---")
        st.subheader(f"📑 File: {file.name}")

        try:
            content = file.read().decode("utf-8")
        except Exception as e:
            st.error(f"❌ Could not read file: {e}")
            continue

        claim_data = extract_claim_info(content)

        # Display extracted fields
        for key, value in claim_data.items():
            st.write(f"**{key}:** {value}")

        # Store for reports
        st.session_state.uploaded_claims.append(claim_data)

        # Check for fraud
        fraud_reasons = check_for_fraud(claim_data)
        if fraud_reasons:
            st.error("🚨 Potential Fraud Detected:")
            for reason in fraud_reasons:
                st.write(f"- {reason}")
        else:
            st.success("✅ No fraud indicators detected.")

        # Generate summary only if required fields are present
        if claim_data.get("Claimant Name") and claim_data.get("Policy Number"):
            with st.spinner("🧠 Generating Summary with LLaMA..."):
                try:
                    # Truncate content for faster LLM response
                    trimmed_content = content[:700]

                    summary = generate_summary_with_llama(
                        trimmed_content,
                        claim_data.get("Claimant Name", ""),
                        claim_data.get("Policy Number", ""),
                        claim_data.get("Date of Incident", ""),
                        claim_data.get("Claim Amount", ""),
                        claim_data.get("Claim Reason", "")
                    )
                    st.subheader("🧠 Claim Summary by GenAI (LLaMA):")
                    st.write(summary)
                except Exception as e:
                    st.error(f"❌ Summary generation failed: {str(e)}")
