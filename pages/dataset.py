import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dataset',layout="wide")
st.header('Dataset Used')

data = pd.read_csv('data.csv', encoding='utf-8')
st.dataframe(data)
with open('data.csv', 'r', encoding='utf-8') as file:
    st.download_button(label='Download', data=file, file_name='data.csv')