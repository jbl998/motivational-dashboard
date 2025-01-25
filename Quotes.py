# External modules
import streamlit as st
import pyquotegen


st.markdown("# Motivational quote")

quote_by_category = pyquotegen.get_quote("motivational")

st.text(quote_by_category)
