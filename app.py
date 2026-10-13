import streamlit as st
import numpy as np

st.title("🩺 HIV Risk Prediction")
st.write("Machine Learning Model for HIV Risk Assessment")

st.sidebar.header("Patient Details")
age = st.sidebar.slider("Age", 15, 70, 25)
num_partners = st.sidebar.number_input("Number of Sexual Partners (last 12 months)", 0, 20, 1)
condom_use = st.sidebar.selectbox("Condom Use", ["Never", "Sometimes", "Always"])
adherence = st.sidebar.slider("PrEP Adherence %", 0, 100, 50)
sti_history = st.sidebar.selectbox("STI History", ["No", "Yes"])

# Simple risk logic (no pkl needed)
if st.button("Predict Risk", type="primary"):
    risk_score = 0
    risk_score += num_partners * 8
    risk_score += (70 - adherence) * 0.3
    if condom_use == "Never":
        risk_score += 20
    elif condom_use == "Sometimes":
        risk_score += 10
    if sti_history == "Yes":
        risk_score += 15
    if age < 25:
        risk_score += 10
    
    prob = min(95, risk_score) / 100
    
    st.divider()
    if prob > 0.4:
        st.error(f"⚠️ HIGH RISK: {prob:.1%}")
        st.write("Recommendation: Immediate counseling, HIV testing, and PrEP initiation advised.")
    elif prob > 0.2:
        st.warning(f"⚡ MODERATE RISK: {prob:.1%}")
        st.write("Recommendation: Risk reduction counseling and regular testing.")
    else:
        st.success(f"✅ LOW RISK: {prob:.1%}")
        st.write("Recommendation: Continue preventive measures.")

st.info("Note: This is a demonstration model for educational purposes.")
