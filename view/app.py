import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("./models/best_model.pkl")
scaler = joblib.load("./models/scaler.pkl")  

st.title("Diabetes Risk Prediction")
st.write("Entrez les valeurs pour toutes les colonnes :")

Pregnancies = st.number_input("Pregnancies:", min_value=0, value=0, step=1)
Glucose = st.number_input("Glucose:", min_value=0.0, value=0.0, step=0.1)
BloodPressure = st.number_input("BloodPressure:", min_value=0.0, value=0.0, step=0.1)
SkinThickness = st.number_input("SkinThickness:", min_value=0.0, value=0.0, step=0.1)
Insulin = st.number_input("Insulin:", min_value=0.0, value=0.0, step=0.1)
BMI = st.number_input("BMI:", min_value=0.0, value=0.0, step=0.1)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction:", min_value=0.0, value=0.0, step=0.01)
Age = st.number_input("Age:", min_value=0, value=0, step=1)

if st.button("Prédire"):
    df_input = pd.DataFrame([[
        Pregnancies, Glucose, BloodPressure, SkinThickness,
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]], columns=[
        "Pregnancies","Glucose","BloodPressure","SkinThickness",
        "Insulin","BMI","DiabetesPedigreeFunction","Age"
    ])

    for log_col in ["BloodPressure", "Insulin", "DiabetesPedigreeFunction"]:
        df_input[log_col] = np.log1p(df_input[log_col])
    
    df_scaled = pd.DataFrame(scaler.transform(df_input), columns=df_input.columns)
    
    prediction = model.predict(df_scaled)[0]
    
    st.write(f"**Prédiction du cluster:** {prediction}")

