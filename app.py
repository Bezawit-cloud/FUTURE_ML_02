# streamlit_app.py
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ------------------------------
# 1️⃣ Load Model and Encoders
# ------------------------------
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)
loaded_model = model_data["model"]
feature_names = model_data["features_names"]

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# ------------------------------
# 2️⃣ Streamlit App Layout
# ------------------------------
st.set_page_config(page_title="Telecom Churn Predictor", layout="centered")
st.title("Telecom Churn Predictor 🚀")
st.subheader("Predict whether a customer will churn or stay")

st.write("Enter customer details below:")

# ------------------------------
# 3️⃣ Input Fields (dictionary style)
# ------------------------------
input_data = {
    'gender': st.selectbox("Gender", ["Male", "Female"]),
    'SeniorCitizen': st.selectbox("Senior Citizen", [0, 1]),
    'Partner': st.selectbox("Has Partner?", ["Yes", "No"]),
    'Dependents': st.selectbox("Has Dependents?", ["Yes", "No"]),
    'tenure': st.number_input("Tenure (months)", min_value=0, max_value=100, value=12),
    'PhoneService': st.selectbox("Phone Service", ["Yes", "No"]),
    'MultipleLines': st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"]),
    'InternetService': st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"]),
    'OnlineSecurity': st.selectbox("Online Security", ["Yes", "No", "No internet service"]),
    'OnlineBackup': st.selectbox("Online Backup", ["Yes", "No", "No internet service"]),
    'DeviceProtection': st.selectbox("Device Protection", ["Yes", "No", "No internet service"]),
    'TechSupport': st.selectbox("Tech Support", ["Yes", "No", "No internet service"]),
    'StreamingTV': st.selectbox("Streaming TV", ["Yes", "No", "No internet service"]),
    'StreamingMovies': st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"]),
    'Contract': st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"]),
    'PaperlessBilling': st.selectbox("Paperless Billing", ["Yes", "No"]),
    'PaymentMethod': st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]),
    'MonthlyCharges': st.number_input("Monthly Charges", min_value=0.0, value=70.0),
    'TotalCharges': st.number_input("Total Charges", min_value=0.0, value=1000.0)
}

# ------------------------------
# 4️⃣ Convert to DataFrame
# ------------------------------
input_df = pd.DataFrame([input_data])

# Encode categorical columns
for col in input_df.select_dtypes(include='object').columns:
    if col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

# Ensure correct feature order
input_features = input_df[feature_names].values

# ------------------------------
# 5️⃣ Make Prediction
# ------------------------------
if st.button("Predict Churn"):
    prediction = loaded_model.predict(input_features)[0]
    probability = loaded_model.predict_proba(input_features)[0][1]

    if prediction == 1:
        st.error(f"Prediction: Customer will CHURN 🚨 ({probability*100:.2f}% probability)")
    else:
        st.success(f"Prediction: Customer will STAY ✅ ({(1-probability)*100:.2f}% probability)")

# ------------------------------

