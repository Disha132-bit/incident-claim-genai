import streamlit as st
import difflib
import random

st.set_page_config(page_title="Customer Support Agent", layout="centered")
st.title("💬 Customer Support GenAI Agent")
st.markdown("Ask any question related to insurance policies or claims. We’ll do our best to help!")

FAQ_KB = {
"What does my policy cover?": """
Most insurance policies cover:

Accidental Damage

Theft or Burglary

Fire and Natural Disasters

Personal Injury

Third-party Liability

Please refer to your specific policy document for exact coverage.
""",
"How do I file a claim?": """
You can file a claim by:

Contacting your insurance company via phone, website, or agent.

Submitting required documents like FIR (if applicable), policy copy, ID proof.

Getting your claim assessed by a surveyor or claims executive.
""",
"How long does it take to process a claim?": """
It usually takes 7-14 working days to process a claim, depending on complexity and documentation.
""",
"Why was my claim rejected?": """
Claims are usually rejected due to:

Missing or incorrect documentation

Policy exclusions

Fraudulent claims

Expired policy or lapsed premium
"""
}

def get_best_match(question):
    question = question.lower()
    matches = difflib.get_close_matches(question, FAQ_KB.keys(), n=1, cutoff=0.6)
    if matches:
        return FAQ_KB[matches[0]]
    return None

question = st.text_area("❓ Ask a question:", placeholder="e.g., What does my policy cover?")
if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        answer = get_best_match(question)
        if answer:
            st.success("✅ Answer from Knowledge Base:")
            st.write(answer)
        else:
            st.warning("🤖 Sorry, I couldn't find an exact answer. Please try rephrasing your question.")
