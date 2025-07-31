import streamlit as st
import os

st.title("Test 4")
st.header("Header")
st.subheader("Subheader")
st.markdown("This is a _markdown_ text")
st.caption("small text")
code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language = "python")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "1537310275440-MUT.png"), width = 200)

st.subheader("Dataframe")

