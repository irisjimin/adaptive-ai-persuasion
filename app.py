import streamlit as st
from hybrid_model import hybrid_analysis

st.title("AI Persuasion Explorer")

text = st.text_area("Enter message")

if st.button("Analyze"):
    result = hybrid_analysis(text)
    st.json(result)