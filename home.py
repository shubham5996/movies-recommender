import streamlit as st
from helpers import showmovies, api_url, display_movie
import requests

# constants
API_KEY = st.secrets['api_key']

# layout
st.set_page_config(page_title='Home', layout="wide")

st.header('Movies Recommender')

with st.form('movieinput'):
    movie_name = st.text_input('Enter your favourite movie!')
    submit_button = st.form_submit_button('Woosh')

if submit_button:
    with st.spinner():
        input_id, output_ids = showmovies(movie_name)
        # input movie
        input_response = requests.get(api_url(input_id, API_KEY)).json()
        display_movie('Your Movie', input_id, input_response)
        # output movies
        for i, output_id in enumerate(output_ids):
            output_response = requests.get(api_url(output_id, API_KEY)).json()
            display_movie(
                f'Suggested Movie #{i + 1}', output_id, output_response)
