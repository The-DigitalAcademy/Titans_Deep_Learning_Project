import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

st.title("Financial Inclusion In Africa")

# User input for features
st.header('Feature Input')


# country={0:'Rwanda',1: 'Tanzania', 2: 'Kenya', 3: 'Uganda'}
# def format_func(option):
#     return country[option]
# feature1 = st.selectbox("country", options=list(country.keys()), format_func=format_func)


cellphone_access={0:'No',1: 'Yes'}
def format_func(option):
    return cellphone_access[option]
feature1 = st.selectbox("cellphone_access", options=list(cellphone_access.keys()), format_func=format_func)


feature2 = st.number_input('age_of_respondent', value=0)

# gender_of_respondent={0:'Female',1: 'Male'}
# def format_func(option):
#     return gender_of_respondent[option]
# feature4 = st.selectbox("gender_of_respondent", options=list(gender_of_respondent.keys()), format_func=format_func)

education_level={0:'Secondary education',1: 'Vocational/Specialised training',2: 'No formal education', 3: 'Primary education',4: 'Other/Dont know/RTA',5: 'Tertiary education'}
def format_func(option):
    return education_level[option]
feature3 = st.selectbox("Choose your education_level", options=list(education_level.keys()), format_func=format_func)


job_type={0:'Formally employed Government', 1: 'Formally employed Private',2: 'Remittance Dependent', 3: 'Self employed', 4: 'Informally employed',5: 'Farming and Fishing', 6: 'Government Dependent',7: 'Other Income',8: 'Dont Know/Refuse to answer', 9: 'No Income'}
def format_func(option):
    return job_type[option]
feature4 = st.selectbox("Choose your Job_type", options=list(job_type.keys()), format_func=format_func)



#Button for predictions
clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
if clicked:
        # Perform predictions using the selected model
    prediction = model.predict([[feature1, feature2, feature3, feature4]])
    if prediction[0] <= 0.5:
        ss = "No"
    elif prediction[0] >= 0.5:
        ss = "Yes"

        # Display the prediction result
    st.header('Prediction')
    st.write(f'The prediction result is: {ss}')
