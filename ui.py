import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Mapping for decoding encoded features
cellphone_access = {0:'No',
                    1: 'Yes'}

gender_of_respondent = {0:'Female',
                        1: 'Male'}

education_level = {
                            0.0: 'Secondary_Education',
                            1.0: 'Vocational/Specialised_Training',
                            2.0: 'No_Formal_Education',
                            3.0: 'Primary_Education',
                            4.0: 'Other/Dont_know/RTA',
                            5.0: 'Tertiary_Education'}

job_type = {0.0: 'Formally_Employed_Government',
            1.0: 'Formally_Employed_Private',
            2.0: 'Remittance_Dependent',
            3.0: 'Self_Employed',
            4.0: 'Informally_Employed',
            5.0: 'Farming_&_Fishing',
            6.0: 'Government_Dependent',
            7.0: 'Other_Income',
            8.0: 'Dont_Know/Refuse_To_Answer',
            9.0: 'No_Income'}

def main():
    # Title of the web app
    st.title("Financial Inclusion In Africa")
    
    # page_bg_img = '''
    # <style>
    # .stApp {
    #     background-image: url('https://thirdway.imgix.net/products/unemployment-to-reemployment-an-idea-to-modernize-the-safety-net-for-the-digital-age/unemployed.jpg?mtime=20180913132907');
    #     background-size: cover;
    # }
    # </style>
    # '''
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    # # Dropdown to select the model
    # model_options = ['RidgeClassifier', 'DecisionTreeClassifier', 'RandomForestClassifier']
    # selected_model = st.selectbox('Select Model', model_options)

    # Load the selected model
    model = tf.keras.models.load_model('model.h5')

    # User input for features
    st.header('Feature Input')
    feature1 = st.selectbox('cellphone_access', options=list(cellphone_access.values()))
    feature1_encoded = [k for k, v in cellphone_access.items() if v == feature1][0]

    feature2 = st.selectbox('gender_of_respondent', options=list(gender_of_respondent.values()))
    feature2_encoded = [k for k, v in gender_of_respondent.items() if v == feature2][0]

    feature3 = st.selectbox('education_level', options=list(education_level.values()))
    feature3_encoded = [k for k, v in education_level.items() if v == feature3][0]

    feature4 = st.selectbox('job_type', options=list(job_type.values()))
    feature4_encoded = [k for k, v in job_type.items() if v == feature4][0]

    feature5 = st.number_input('age_of_respondent', value=0)

    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1_encoded, feature2_encoded, feature3_encoded, feature4_encoded, feature5]])

        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is: {prediction[0]}')

if __name__ == '__main__':
    main()
