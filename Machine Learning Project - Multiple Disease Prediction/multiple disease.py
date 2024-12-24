import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Inject custom CSS for styling
custom_css = """
<style>
/* Main app background color */
[data-testid="stAppViewContainer"] {
    background-color: #FFC1C1; /* Light red background */
    color: #333333; /* Dark gray text */
}

/* Sidebar background color */
[data-testid="stSidebar"] {
    background-color: #DFF2BF; /* Light green sidebar */
}

/* Button styling */
.stButton > button {
    background-color: #4CAF50; /* Green button */
    color: white; /* White text */
    border-radius: 10px; /* Rounded corners */
    padding: 10px 15px;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #45A049; /* Darker green on hover */
}

/* Input fields styling */
input[type="text"] {
    border: 1px solid #CCCCCC;
    border-radius: 5px;
    padding: 8px;
    font-size: 14px;
}

/* Success message styling */
.stMarkdown {
    background-color: #DFF2BF; /* Light green background for success */
    color: #4F8A10; /* Dark green text */
    padding: 10px;
    border-radius: 5px;
    font-size: 16px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Load the saved models
diabetes_model = pickle.load(open('C:/Users/shuvo ray/Desktop/multiple dise/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/shuvo ray/Desktop/multiple dise/saved_models/heart_disease_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for Prediction
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) if x != '' else 0.0 for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
