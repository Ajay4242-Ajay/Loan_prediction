import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("loan_amount_model.pkl")

# -----------------------------
# Page title
# -----------------------------
st.set_page_config(
    page_title="Loan Amount Predictor",
    page_icon="🏦"
)

st.title("🏦 Loan Amount Prediction")
st.write("Enter the applicant's information below.")

# -----------------------------
# User inputs
# -----------------------------

total_income = st.number_input(
    "Total Income",
    min_value=0,
    value=5000
)

loan_term = st.number_input(
    "Loan Amount Term",
    min_value=0,
    value=360
)

credit_history = st.selectbox(
    "Credit History",
    [1, 0]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

# -----------------------------
# Prediction button
# -----------------------------

if st.button("Predict Loan Amount"):

    # Convert user inputs into model features
    input_data = pd.DataFrame([{
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "TotalIncome": total_income,

        "Gender_Male": 1 if gender == "Male" else 0,

        "Married_Yes": 1 if married == "Yes" else 0,

        "Dependents_1": 1 if dependents == "1" else 0,
        "Dependents_2": 1 if dependents == "2" else 0,
        "Dependents_3+": 1 if dependents == "3+" else 0,

        "Education_Not Graduate":
            1 if education == "Not Graduate" else 0,

        "Self_Employed_Yes":
            1 if self_employed == "Yes" else 0,

        "Property_Area_Semiurban":
            1 if property_area == "Semiurban" else 0,

        "Property_Area_Urban":
            1 if property_area == "Urban" else 0
    }])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted Loan Amount: {prediction[0]:.2f}"
    )