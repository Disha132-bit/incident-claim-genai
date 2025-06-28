import streamlit as st

st.set_page_config(page_title="Insurance Claim GenAI", page_icon="📄", layout="centered")

st.title("📄 Insurance Claim GenAI")
st.markdown("### Welcome to the Insurance Claim Analyzer powered by LLaMA GenAI 🚀")

st.image(
"https://img.freepik.com/free-vector/healthcare-insurance-abstract-concept_335657-3180.jpg",
use_container_width=True # ✅ Updated to avoid deprecation warning
)

st.markdown("""
This intelligent system helps insurance companies:

✅ Extract claim details
✅ Detect potential fraud
✅ Summarize using LLaMA GenAI

📌 Use the sidebar to navigate:
📂 Upload Claim Files

📊 Reports

ℹ️ About this App
""")
