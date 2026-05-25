import streamlit as st
import pickle
import numpy as np

with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏦 Loan Approval Predictor")
st.write("Apni details bharo aur jaano — Loan Approve hoga ya nahi!")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
property_area = 2 if property_area == "Urban" else 1 if property_area == "Semiurban" else 0

if st.button("Check Loan Status 🚀"):
    input_data = np.array([[gender, married, dependents, education,
                            self_employed, applicant_income, coapplicant_income,
                            loan_amount, loan_term, credit_history, property_area]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    approve_chance = round(probability[0][1] * 100, 2)
    reject_chance = round(probability[0][0] * 100, 2)

    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected!")

    st.write(f"✅ Approve Chance: **{approve_chance}%**")
    st.write(f"❌ Reject Chance: **{reject_chance}%**")