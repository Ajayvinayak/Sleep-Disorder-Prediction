import streamlit as st  # Import Streamlit first
import pandas as pd
import joblib

# Set page configuration
st.set_page_config(page_title="Sleep Disorder Prediction", layout="centered")

# Custom CSS for styling
custom_css = """
<style>
    body {
        background-color: #F5DEB3;
    }
    .stApp {
        background-color: #F5DEB3;
    }
    .center-button {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load the model and encoders
@st.cache_resource
def load_model_and_encoders():
    model = joblib.load("best_lightgbm_model.pkl")
    encoders = joblib.load("label_encoders.pkl")
    return model, encoders

# Predict function
def predict_sleep_disorder(input_data, model, encoders):
    input_df = pd.DataFrame([input_data])

    # Rule-based override for Insomnia
    if (input_data['Sleep Duration'] < 5.5) and (input_data['Stress Level'] > 7) and (input_data['Quality of Sleep'] < 4):
        return "Insomnia"

    # Rule-based override for Normal
    if (input_data['Sleep Duration'] > 6.5) and (input_data['Stress Level'] < 5) and (input_data['Quality of Sleep'] > 5):
        return "Normal"

    # Encode categorical inputs
    for col, encoder in encoders.items():
        if col in input_df.columns:
            input_df[col] = encoder.transform(input_df[col])

    # Make prediction
    prediction = model.predict(input_df)
    class_mapping = {i: cls for i, cls in enumerate(encoders['Sleep Disorder'].classes_)}
    return class_mapping[prediction[0]]

# Load the model and encoders
model, encoders = load_model_and_encoders()

# Streamlit App Layout
st.title("Sleep Disorder Prediction")

# Input Fields organized in a grid layout
st.markdown("### Input Patient Data")
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)
row3_col1, row3_col2, row3_col3 = st.columns(3)

# Row 1 Inputs
sleep_duration = row1_col1.slider("Sleep Duration (hours)", min_value=0.0, max_value=10.0, step=0.1, value=7.0)
daily_steps = row1_col2.slider("Daily Steps", min_value=0, max_value=20000, step=100, value=6000)
quality_of_sleep = row1_col3.number_input("Quality of Sleep (1-9)", min_value=1, max_value=9, value=5, step=1)

# Row 2 Inputs
stress_level = row2_col1.number_input("Stress Level (1-10)", min_value=1, max_value=10, value=5, step=1)
age = row2_col2.number_input("Age (years)", min_value=1, max_value=120, value=30, step=1)
heart_rate = row2_col3.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=75, step=1)

# Row 3 Inputs
physical_activity_level = row3_col1.number_input("Physical Activity Level (1-100)", min_value=1, max_value=100, value=50, step=1)
systolic_bp = row3_col2.number_input("Systolic BP (mmHg)", min_value=80, max_value=200, value=120, step=1)
diastolic_bp = row3_col3.number_input("Diastolic BP (mmHg)", min_value=40, max_value=120, value=80, step=1)

# Dropdown inputs
bmi_category = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
gender = st.selectbox("Gender", encoders['Gender'].classes_)
occupation = st.selectbox("Occupation", encoders['Occupation'].classes_)

# Predict Button in the center
with st.container():
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Predict"):
        input_data = {
            'Sleep Duration': sleep_duration,
            'Quality of Sleep': quality_of_sleep,
            'BMI Category': bmi_category,
            'Stress Level': stress_level,
            'Age': age,
            'Heart Rate': heart_rate,
            'Physical Activity Level': physical_activity_level,
            'Daily Steps': daily_steps,
            'systolic_bp': systolic_bp,
            'diastolic_bp': diastolic_bp,
            'Gender': gender,
            'Occupation': occupation
        }

        # Make prediction
        prediction = predict_sleep_disorder(input_data, model, encoders)

        # Display the result
        st.subheader("Prediction Result")
        st.success(f"The predicted sleep disorder is: **{prediction}**")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Created by **AJAY VINAYAK SRMIST, Ramapuram And L BHARATH KUMAR REC**")
