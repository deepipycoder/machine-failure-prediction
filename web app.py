import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("predictive1.pkl")

st.set_page_config(
    page_title="Machine Failure Prediction",
    page_icon="⚙️"
)

st.title("AI-Based Industrial Machine Failure Prediction")

st.write("Predict machine failure using Machine Learning.")

st.header("Enter Machine Details")

air_temp = st.number_input("Air Temperature", value=300.0)
process_temp = st.number_input("Process Temperature", value=310.0)
rotational_speed = st.number_input("Rotational Speed", value=1500)
torque = st.number_input("Torque", value=40.0)
tool_wear = st.number_input("Tool Wear", value=100)

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

if st.button("Predict Machine Failure"):

    st.write("Machine details submitted!")