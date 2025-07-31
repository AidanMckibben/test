import streamlit as st
from datetime import datetime, date
from typing import Dict, Union, Optional

st.title("User Information Form")

form_values: Dict[str, Union[str, float, date, None]] = {
    "name": "",
    "height": 0.0,
    "gender": "",
    "DOB": None,
    "location": "",
}

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.selectbox("Select your gender: ", ["Male", "Female", "Other"])
    form_values["DOB"] = st.date_input("Enter your birth date: ", max_value = max_date, min_value = min_date)
    form_values["location"] = st.text_input("Enter your location: ")

    submit_button = st.form_submit_button("Submit")
    print("after submit")

    if submit_button:
        if not all(form_values.values()):
            st.error("Please fill in all fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")