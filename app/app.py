import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open("model/house_price_model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details:")

crim = st.number_input("CRIM")
zn = st.number_input("ZN")
indus = st.number_input("INDUS")
chas = st.number_input("CHAS")
nox = st.number_input("NOX")
rm = st.number_input("RM")
age = st.number_input("AGE")
dis = st.number_input("DIS")
rad = st.number_input("RAD")
tax = st.number_input("TAX")
ptratio = st.number_input("PTRATIO")
b = st.number_input("B")
lstat = st.number_input("LSTAT")

if st.button("Predict Price"):
    features = np.array([[crim, zn, indus, chas, nox, rm, age,
                          dis, rad, tax, ptratio, b, lstat]])

    prediction = model.predict(features)
    st.success(f"Predicted House Price: {prediction[0]:.2f}")