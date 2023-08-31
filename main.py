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

Extracurricular_Activities={0:'No',1: 'Yes'}
def format_func(option):
    return Extracurricular_Activities[option]
feature3 = st.selectbox("Extracurricular Activities", options=list(Extracurricular_Activities.keys()), format_func=format_func)
feature4 = st.number_input('Sleep Hours', value=0)
feature5 = st.number_input('Sample Question Papers Practiced', value=0)

#Button for predictions
clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
if clicked:
        # Perform predictions using the selected model
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5]])

        # Display the prediction result
    st.header('Prediction')
    st.write(f'The prediction result is: {prediction[0]}')




