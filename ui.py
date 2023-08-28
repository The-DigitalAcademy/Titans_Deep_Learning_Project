import streamlit as st
import pickle

#Function to load the selected model
def load_model(model_name):
    model_path = f'{model_name}.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
  # Title of the web app
    st.title('Financial Inclusion In Africa')

    # Set custom CSS for the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('');
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')

    # Dropdown to select the model
    model_options = ['XGBClassifier']
    selected_model = st.selectbox('Select Model', model_options)  

    # Load the selected model
    model = load_model(selected_model)

    # User input for features
    st.header('Feature Input')
    
    location_Type={0:'Urban',1: 'Rural'}
    def format_func(option):
        return location_Type[option]
    feature1 = st.selectbox("Choose your Location Type", options=list(location_Type.keys()), format_func=format_func)

    # cellphone_access={0:'No',1: 'Yes'}
    # def format_func(option):
    #     return cellphone_access[option]
    # feature2 = st.selectbox("cellphone_access", options=list(cellphone_access.keys()), format_func=format_func)


    feature2 = st.number_input('age_of_respondent', value=0)


    education_level={0:'Secondary education',1: 'Vocational/Specialised training',2: 'No formal education', 3: 'Primary education',4: 'Other/Dont know/RTA',5: 'Tertiary education'}
    def format_func(option):
        return education_level[option]
    feature3 = st.selectbox("Choose your education_level", options=list(education_level.keys()), format_func=format_func)

   
    Job_type={0:'Formally employed Government', 1: 'Formally employed Private',2: 'Remittance Dependent', 3: 'Self employed', 4: 'Informally employed',5: 'Farming and Fishing', 6: 'Government Dependent',7: 'Other Income',8: 'Dont Know/Refuse to answer', 9: 'No Income'}
    def format_func(option):
        return Job_type[option]
    feature4 = st.selectbox("Choose your Job_type", options=list(Job_type.keys()), format_func=format_func)
   
 


    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4]])
        if prediction[0] == 0:
            pred="Yes"
        else:
            pred="No"
    
        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is:  {prediction[0]}')

if __name__ == '__main__':
    main()
