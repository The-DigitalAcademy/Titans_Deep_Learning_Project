import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

st.title("Financial Inclusion In Africa")

# User input for features
st.header('Feature Input')

cellphone_access = {0: 'No', 1: 'Yes'}
feature1 = st.selectbox("Cellphone Access", options=list(cellphone_access.keys()))

feature2 = st.number_input('Age of Respondent', value=0)

gender_of_respondent = {0: 'Female', 1: 'Male'}
feature3 = st.selectbox("Gender of Respondent", options=list(gender_of_respondent.keys()))

education_level = {0: 'Secondary education', 1: 'Vocational/Specialised training', 2: 'No formal education', 3: 'Primary education', 4: 'Other/Dont know/RTA', 5: 'Tertiary education'}
feature4 = st.selectbox("Education Level", options=list(education_level.keys()))

job_type = {0: 'Formally employed Government', 1: 'Formally employed Private', 2: 'Remittance Dependent', 3: 'Self employed', 4: 'Informally employed', 5: 'Farming and Fishing', 6: 'Government Dependent', 7: 'Other Income', 8: 'Dont Know/Refuse to answer', 9: 'No Income'}
feature5 = st.selectbox("Job Type", options=list(job_type.keys()))

# Button for predictions
clicked = st.button('Get Predictions')

# Perform predictions when the button is clicked
if clicked:
    try:
        # Convert user inputs to the format expected by the model
        feature1 = float(feature1)  # Convert to float if needed
        feature2 = float(feature2)
        feature3 = float(feature3)
        feature4 = float(feature4)
        feature5 = float(feature5)

        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5]])

        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is: {prediction[0]}')
    except Exception as e:
        st.error(f"An error occurred: {str(e)} Please check your inputs.")
