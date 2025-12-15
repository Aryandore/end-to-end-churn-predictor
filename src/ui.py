import streamlit as st
import requests

# 1. Page Config (Tab Title)
st.set_page_config(page_title="Churn Predictor", page_icon="📉")

st.title("📉 Customer Churn Prediction System")
st.write("Enter customer details below to predict if they will cancel their subscription.")

# 2. Input Fields (Based on your API/Model inputs)
# Note: Ensure these match the columns your model was trained on!
col1, col2 = st.columns(2)

with col1:
    senior_citizen = st.selectbox("Is Senior Citizen?", ["No", "Yes"])
    tenure = st.slider("Tenure (Months)", min_value=0, max_value=72, value=12)

with col2:
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0, step=0.5)

# 3. Logic to convert inputs for API
# We need to convert "Yes"/"No" back to 1/0 because the model expects numbers
senior_numeric = 1 if senior_citizen == "Yes" else 0

input_data = {
    "SeniorCitizen": senior_numeric,
    "tenure": tenure,
    "MonthlyCharges": monthly_charges
}

# 4. Predict Button
if st.button("Predict Churn Risk"):
    # Send request to FastAPI
    try:
        # Note: We use 'localhost' here. If using Docker, it might differ.
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result["churn_prediction"]
            probability = result["churn_probability"]
            
            if prediction == 1:
                st.error(f"⚠️ High Churn Risk! (Probability: {probability:.2%})")
                st.write("Suggestion: Offer a discount or long-term contract immediately.")
            else:
                st.success(f"✅ Safe Customer. (Probability: {probability:.2%})")
        else:
            st.error("Error: Could not get prediction from API.")
            st.write(response.text)
            
    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Is the API running?")
        st.info("Make sure you are running 'uvicorn src.app:app' in a separate terminal!")