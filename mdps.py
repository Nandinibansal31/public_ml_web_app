# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:57:27 2025

@author: nandi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open('D:/multiple disease pred/saved model/diabetes_model .sav', 'rb'))

heart_disease_model = pickle.load(open('D:/multiple disease pred/saved model/heartdisease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('D:/multiple disease pred/saved model/parkinsons_model.sav', 'rb'))

breastcancer_model=pickle.load(open('D:/multiple disease pred/saved model/breastcancer_model.sav','rb'))



with st.sidebar:
    selected= option_menu ('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons=['calendar-heart-fill','activity','clipboard2-pulse','bag-heart-fill'],
                           
                           default_index=0)

#Diabetes Prediction page
if(selected =='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction')
    
    #getting input data from user
    #columns for input fields
    
    col1,col2=st.columns(2)
    
    with col1:
        Pregnancies = st.number_input("Enter number of Pregnancies", min_value=0, step=1, key="pregnancies")
        BloodPressure = st.text_input("Enter Blood Pressure", key="blood_pressure")
        Insulin = st.text_input("Enter Insulin Level", key="insulin")
        DiabetesPedigreeFunction = st.text_input("Enter Diabetes Pedigree Function", key="dpf")

    with col2:
        Glucose = st.text_input("Enter Glucose Level", key="glucose")
        SkinThickness = st.text_input("Enter Skin Thickness", key="skin_thickness")
        BMI = st.text_input("Enter BMI", key="bmi")
        Age = st.text_input("Enter Age", key="age")
        
        
    
    
    #code for prediction
    diab_dignosis= ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction= diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_dignosis='The person is Diabetic'
        else:
            diab_dignosis='The person is Not Diabetic'
            
    st.success(diab_dignosis)        
            
    
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction ')

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

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col1:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        DDP = st.text_input('Jitter:DDP')

    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction ')

    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean Radius')
        mean_perimeter = st.text_input('Mean Perimeter')
        mean_smoothness = st.text_input('Mean Smoothness')
        mean_concavity = st.text_input('Mean Concavity')
        mean_symmetry = st.text_input('Mean Symmetry')
        radius_error = st.text_input('Radius Error')
        perimeter_error = st.text_input('Perimeter Error')
        smoothness_error = st.text_input('Smoothness Error')
        concavity_error = st.text_input('Concavity Error')
        worst_radius = st.text_input('Worst Radius')

    with col2:
        mean_texture = st.text_input('Mean Texture')
        mean_area = st.text_input('Mean Area')
        mean_compactness = st.text_input('Mean Compactness')
        mean_concave_points = st.text_input('Mean Concave Points')
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
        texture_error = st.text_input('Texture Error')
        area_error = st.text_input('Area Error')
        compactness_error = st.text_input('Compactness Error')
        concave_points_error = st.text_input('Concave Points Error')
        worst_texture = st.text_input('Worst Texture')

    with col3:
        worst_perimeter = st.text_input('Worst Perimeter')
        worst_area = st.text_input('Worst Area')
        worst_smoothness = st.text_input('Worst Smoothness')
        worst_compactness = st.text_input('Worst Compactness')
        worst_concavity = st.text_input('Worst Concavity')
        worst_concave_points = st.text_input('Worst Concave Points')
        worst_symmetry = st.text_input('Worst Symmetry')
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
        symmetry_error = st.text_input('Symmetry Error')

    breastcancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Test Result'):

       user_input = [
    mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
    mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
    radius_error, texture_error, perimeter_error, area_error, smoothness_error,
    compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
    worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
    worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
]


       user_input = [float(x) for x in user_input]

       breastcancer_prediction = breastcancer_model.predict([user_input])

       if  breastcancer_prediction[0] == 1:
            breastcancer_diagnosis = 'The person is having Breast Cancer'
       else:
            breastcancer_diagnosis = 'The person does not have Breast Cancer'

    st.success( breastcancer_diagnosis)    
