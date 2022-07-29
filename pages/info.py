import streamlit as st
st.set_page_config(page_title='Info', layout="wide")

st.subheader('Made with ♥️ by Subham Jalan')
st.write('This is a very basic Machine Learning application made using Python.')
st.write('Its main purpose is to showcase simple machine learning applications and is not extremely accurate.')
st.write('Here are the current limitations: ')
st.write('1. The dataset is very small. (IMDb does not contain keywords in its dataset making it difficult to use cosine similarity and hence this data is taken from Kaggle.')
st.write('2. The dataset does not contain movies released after 2017 (due to same reason as above).')
st.write('3. Sometimes when entering your favourite movie, wrong movie may be selected as input. This will be fixed using search dropdown later on.')

st.write('Stuff to work on:')
st.write('1. Use a larger database with relevant fields for feature vectorization.')
st.write('2. Search Dropdown')
