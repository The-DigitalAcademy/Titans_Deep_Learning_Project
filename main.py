import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Load the pre-trained model
model = tf.keras.models.load_model('Student_Performance.h5')

st.title("Student Performance Prediction")

# User input for features
st.header('Feature Input')

feature1 = st.number_input('Hours Studied', value=0)
feature2 = st.number_input('Previous Scores', value=0)

Extracurricular Activities={0:'No',1: 'Yes'}
def format_func(option):
    return Extracurricular Activities[option]
feature3 = st.selectbox("Extracurricular Activities", options=list(Extracurricular Activities.keys()), format_func=format_func)
feature4 = st.number_input('Sleep Hours', value=0)
feature5 = st.number_input('Sample Question Papers Practiced', value=0)



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
    st.write(f"Bank account Approval Probability: {prediction[0, 0]}")
except Exception as e:
    st.error("An error occurred during prediction.")
    st.exception(e)  # Log the exception details
