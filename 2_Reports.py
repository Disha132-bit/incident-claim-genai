# app/2_Report.py

import streamlit as st
import os
import pandas as pd
import plotly.express as px
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.claim_parser import extract_claim_info
from backend.fraud_checker import check_for_fraud

st.title("📊 Claim Analytics Report")

st.markdown("This page summarizes uploaded claims with charts and insights.")

# Get uploaded files from session state
if "uploaded_claims" not in st.session_state:
    st.warning("No claims uploaded yet. Please upload from 'Upload Claim Files' page.")
    st.stop()

claims_data = st.session_state.uploaded_claims  # list of dicts

df = pd.DataFrame(claims_data)

# Convert date column
df["Date of Incident"] = pd.to_datetime(df["Date of Incident"], errors="coerce")

# Add Fraud Label
df["Fraud Detected"] = df.apply(lambda row: bool(check_for_fraud(row)), axis=1)

# --- CHARTS ---

# 1. Claim Amount Distribution
st.subheader("💰 Claim Amount Distribution")
fig1 = px.histogram(df, x="Claim Amount", nbins=10, title="Distribution of Claim Amounts")
st.plotly_chart(fig1, use_container_width=True)

# 2. Fraud vs Safe Claims
st.subheader("🧪 Fraudulent vs Safe Claims")
fraud_counts = df["Fraud Detected"].value_counts().rename({True: "Fraud", False: "Safe"})
fig2 = px.pie(names=fraud_counts.index, values=fraud_counts.values, title="Fraud Detection Overview")
st.plotly_chart(fig2, use_container_width=True)

# 3. Claims by Month
st.subheader("📅 Claims Over Time")
df['Month'] = df['Date of Incident'].dt.to_period('M').astype(str)
fig3 = px.bar(df.groupby("Month")["Claim Amount"].sum().reset_index(), x="Month", y="Claim Amount", title="Monthly Claim Volume")
st.plotly_chart(fig3, use_container_width=True)

# 4. Average Claim Amount
# Clean Claim Amount to numeric
df["Claim Amount Cleaned"] = (
    df["Claim Amount"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]  # extract numeric part
    .astype(float)
)

avg_amount = df["Claim Amount Cleaned"].mean()
total_claims = len(df)
st.metric("📊 Average Claim Amount", f"₹{avg_amount:,.0f}")

# 5. Top Claim Reasons
st.subheader("🔍 Common Claim Reasons")
top_reasons = df["Claim Reason"].value_counts().nlargest(5)
st.bar_chart(top_reasons)

