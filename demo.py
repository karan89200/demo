import streamlit as st

st.write("karan sharma")
st.title("karan sharma")

country = st.selectbox("choose country",["indian","pk","nepal"])
st.radio("choose country",["indian","pk","nepal"])

st.write(country)