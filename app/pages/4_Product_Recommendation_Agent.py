import streamlit as st

st.set_page_config(page_title="Insurance Product Recommender", layout="centered")
st.title("📦 Insurance Product Recommendation Agent")
st.markdown("Answer a few questions and get a personalized insurance product recommendation instantly.")

age = st.slider("📅 Age", 18, 75, 30)
income = st.selectbox("💰 Income Range", ["<5 Lakhs", "5–10 Lakhs", "10–20 Lakhs", "20+ Lakhs"])
goal = st.radio("🎯 Your Primary Goal", ["Health coverage", "Vehicle insurance", "Life protection", "Travel insurance"])

def recommend_product(age, income, goal):
    if goal == "Life protection":
        if age < 45:
            return "We recommend a Term Life Insurance Plan with ₹1 Cr coverage for 30 years. It ensures your family's financial stability in case of unforeseen events and comes with optional riders for critical illness and disability."
        else:
            return "We recommend an Endowment Life Plan that combines savings and life cover. This plan is ideal for individuals seeking guaranteed returns and life protection beyond 60."
    elif goal == "Health coverage":
        if income in ["10–20 Lakhs", "20+ Lakhs"]:
            return "A comprehensive Health Insurance Policy with ₹10–20 Lakhs sum insured is recommended. It covers hospitalization, critical illness, maternity, and cashless network benefits."
        else:
            return "We suggest a Family Floater Health Insurance Plan with ₹5 Lakhs coverage. It provides affordable medical protection for your entire family under one premium."

    elif goal == "Vehicle insurance":
        return "We recommend a Comprehensive Motor Insurance Policy that includes third-party liability, own-damage, and add-ons like zero depreciation and roadside assistance. It's ideal for both new and existing vehicle owners."

    elif goal == "Travel insurance":
        return "A Global Travel Insurance Policy is suitable, covering trip cancellation, medical emergencies abroad, lost baggage, and more. Recommended especially if you're planning international trips."

    return "We couldn’t determine a match. Please refine your inputs."

if st.button("Get Recommendation"):
    with st.spinner("🔍 Analyzing your inputs..."):
        recommendation = recommend_product(age, income, goal)
    st.success("✅ Recommended Insurance Product:")
    st.write(recommendation)
