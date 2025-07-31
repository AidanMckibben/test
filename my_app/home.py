import streamlit as st

st.title("Welcome to the Window Tool Home Page")
st.write("Use the sidebar to navigate between pages.")
st.write(st.__version__)

col1, col2, col3 = st.columns(3)

if 'page' not in st.session_state:
    st.session_state.page = "home"

with col1:
    if st.button("Building Info"):
        st.session_state.page = "building_info"
        st.rerun()

with col2:
    if st.button("Assembly Info"):
        st.session_state.page = "assembly_info"
        st.rerun()

with col3:
    if st.button("Retrofit Info"):
        st.session_state.page = "retrofit_info"
        st.rerun()


if st.session_state.page == "building_info":
    import pages.Building_Info as page1
    page1.app()

elif st.session_state.page == "assembly_info":
    import pages.Assembly_Info as page2
    page2.app()

elif st.session_state.page == "retrofit_info":
    import pages.Retrofit_Info as page3
    page3.app()

else:
    st.write("Select a page from above or sidebar")