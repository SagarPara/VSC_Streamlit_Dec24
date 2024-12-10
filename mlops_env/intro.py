import streamlit as st 

st.title("Hello Streamlit")

st.header("My first app!")

agree = st.checkbox("I agree")

if agree:
    st.write("Great")





