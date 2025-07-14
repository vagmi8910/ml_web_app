

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:44:34 2025
@author: pc
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Breast Cancer Prediction'],
        icons=['activity', 'heart', 'gender-female'],  # fixed icon names
        default_index=0
    )


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    # Add input fields to the columns
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
        Insulin = st.text_input('Insulin Level')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Glucose = st.text_input('Glucose Level')
        BMI = st.text_input('BMI Value')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        SkinThickness = st.text_input('Skin Thickness Value')
        Age = st.text_input('Age of the Person')
    
    

    diab_diagnosis =''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[pregnancies, Glucose, BloodPressure, SkinThickness,
                                                    Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 0:
            diab_diagnosis = "The Person Is Not Diabetic"
        elif diab_prediction[0] == 1:
            diab_diagnosis = "The Person Is Diabetic"
        else:
            diab_diagnosis="Enter the valid values"

    st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')

    # Create 3 columns
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
        ca = st.text_input('Number of Major Vessels (0–3)')
        cp = st.text_input('Chest Pain Type (0–3)')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting ECG Results (0–2)')
       

    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)')
        thalach = st.text_input('Max Heart Rate Achieved')
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
        oldpeak = st.text_input('ST Depression Induced by Exercise')
        slope = st.text_input('Slope of ST Segment (0–2)')
        thal = st.text_input('Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)')

    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
            float(age), float(sex), float(cp), float(trestbps),
            float(chol), float(fbs), float(restecg), float(thalach),
            float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]
            heart_prediction = heart_disease_model.predict([input_data])
            if heart_prediction[0] == 0:
                heart_diagnosis = "The Person Is Not Having Heart Disease"
            elif heart_prediction[0] == 1:
                heart_diagnosis = "The Person Is Having Heart Disease"
            else:
                heart_diagnosis = "Enter the valid values"
        except ValueError:
            heart_diagnosis = "Please enter valid numerical values."
            
    st.success(heart_diagnosis)


elif selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction Using ML')

    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean Radius')
        mean_texture = st.text_input('Mean Texture')
        mean_perimeter = st.text_input('Mean Perimeter')
        mean_area = st.text_input('Mean Area')
        mean_smoothness = st.text_input('Mean Smoothness')
        mean_compactness = st.text_input('Mean Compactness')
        mean_concavity = st.text_input('Mean Concavity')
        mean_concave_points = st.text_input('Mean Concave Points')
        mean_symmetry = st.text_input('Mean Symmetry')
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    with col2:
        radius_error = st.text_input('Radius Error')
        texture_error = st.text_input('Texture Error')
        perimeter_error = st.text_input('Perimeter Error')
        area_error = st.text_input('Area Error')
        smoothness_error = st.text_input('Smoothness Error')
        compactness_error = st.text_input('Compactness Error')
        concavity_error = st.text_input('Concavity Error')
        concave_points_error = st.text_input('Concave Points Error')
        symmetry_error = st.text_input('Symmetry Error')
        fractal_dimension_error = st.text_input('Fractal Dimension Error')

    with col3:
        worst_radius = st.text_input('Worst Radius')
        worst_texture = st.text_input('Worst Texture')
        worst_perimeter = st.text_input('Worst Perimeter')
        worst_area = st.text_input('Worst Area')
        worst_smoothness = st.text_input('Worst Smoothness')
        worst_compactness = st.text_input('Worst Compactness')
        worst_concavity = st.text_input('Worst Concavity')
        worst_concave_points = st.text_input('Worst Concave Points')
        worst_symmetry = st.text_input('Worst Symmetry')
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    cancer_diagnosis = ''

    if st.button('Breast Cancer Test Result'):
        input_data = [[
            mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
            mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
            radius_error, texture_error, perimeter_error, area_error, smoothness_error,
            compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
            worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
            worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
        ]]

        
        try:
            input_data = [list(map(float, input_data[0]))]
            cancer_prediction = breast_cancer_model.predict(input_data)

            if cancer_prediction[0] == 0:
                cancer_diagnosis = "The Breast Cancer is Malignant"
            elif cancer_prediction[0] == 1:
                cancer_diagnosis = "The Breast Cancer is Benign"
            else:
                cancer_diagnosis = "Enter the valid values"
        except ValueError:
            cancer_diagnosis = "Please enter valid numerical values for all fields."

    st.success(cancer_diagnosis)

