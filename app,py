import streamlit as st
import joblib
import pandas as pd

model = joblib.load('hiv_risk_model.pkl')

st.title("🩺 HIV Risk Prediction")
st.write("Predict HIV risk using ML model")

st.sidebar.header("Patient Details")
age = st.sidebar.slider("Age", 15, 70, 25)
num_partners = st.sidebar.number_input("Number of Partners", 0, 20, 1)
adherence = st.sidebar.slider("PrEP Adherence %", 0, 100, 50)

if st.button("Predict"):
    data = [[age, num_partners, adherence]]
    prob = model.predict_proba(data)[0][1]

    if prob > 0.2:
        st.error(f"⚠️ HIGH RISK: {prob:.2%}")
    else:
        st.success(f"✅ LOW RISK: {prob:.2%}")
   
