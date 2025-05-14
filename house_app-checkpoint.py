import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.title("House Price Predictor")

# Input fields for user
CRIM = st.number_input('CRIM - Per capita crime rate', 0.0, 100.0, 0.1)
ZN = st.number_input('ZN - Proportion of residential land', 0.0, 100.0, 0.0)
INDUS = st.number_input('INDUS - Non-retail business acres', 0.0, 30.0, 10.0)
RM = st.number_input('RM - Avg number of rooms', 1.0, 10.0, 6.0)
RAD = st.number_input('RAD - Index of accessibility to highways', 1, 24, 4)
TAX = st.number_input('TAX - Property tax rate', 100.0, 800.0, 300.0)
B = st.number_input('B - 1000(Bk - 0.63)^2', 0.0, 400.0, 350.0)
LSTAT = st.number_input('LSTAT - % lower status population', 1.0, 40.0, 12.0)

if st.button("Predict Price"):
    input_data = np.array([[CRIM, ZN, INDUS, RM,  RAD,
                            TAX, B, LSTAT]])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]*1000:.2f}")
#streamlit run house_app.py