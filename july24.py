import streamlit as st

choice = st.selectbox("Pick a fruit", ["Apple", "Banana", "Cherry"], index=1)
st.write(f"You picked {choice}")

col1, col2 = st.columns([1, 2])
with col1:
    st.button("Left")
with col2:
    st.button("Right")