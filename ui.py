import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

st.title("Financial Inclusion In Africa")

# User input for features
st.header('Feature Input')

cellphone_access={0:'No',1: 'Yes'}
def format_func(option):
    return location_Type[option]
feature1 = st.selectbox("cellphone_access", options=list(location_Type.keys()), format_func=format_func)


feature2 = st.number_input('age_of_respondent', value=0)

gender_of_respondent={0:'Female',1: 'Male'}
def format_func(option):
    return location_Type[option]
feature3 = st.selectbox("gender_of_respondent", options=list(location_Type.keys()), format_func=format_func)

education_level={0:'Secondary education',1: 'Vocational/Specialised training',2: 'No formal education', 3: 'Primary education',4: 'Other/Dont know/RTA',5: 'Tertiary education'}
def format_func(option):
    return education_level[option]
feature4 = st.selectbox("Choose your education_level", options=list(education_level.keys()), format_func=format_func)


Job_type={0:'Formally employed Government', 1: 'Formally employed Private',2: 'Remittance Dependent', 3: 'Self employed', 4: 'Informally employed',5: 'Farming and Fishing', 6: 'Government Dependent',7: 'Other Income',8: 'Dont Know/Refuse to answer', 9: 'No Income'}
def format_func(option):
    return Job_type[option]
feature5 = st.selectbox("Choose your Job_type", options=list(Job_type.keys()), format_func=format_func)


 # Prepare the input data for prediction
input_data = np.array([[feature1, feature2, feature3, feature4, feature5]])

# Make predictions when a button is clicked
if st.button("Predict"):
try:
    st.write("Input Data:", input_data)  # Log the input data

    # Use the loaded model to make predictions
    prediction = model.predict(input_data)

    st.write("Raw Prediction:", prediction)  # Log the raw prediction

    # Display the prediction
    st.write(f"Loan Approval Probability: {prediction[0, 0]}")
except Exception as e:
    st.error("An error occurred during prediction.")
    st.exception(e)  # Log the exception details
