import difflib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import streamlit as st


def showmovies(movie_name):

    data = pd.read_csv('data.csv', encoding='utf-8')
    selected_features = ['genres', 'title', 'keywords', 'director']

    for feature in selected_features:
        data[feature] = data[feature].fillna('')

    # finding closest named movie

    list_of_all_titles = list(data['title'])
    find_close_match = difflib.get_close_matches(
        movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    index_of_the_movie = data[data.title == close_match]['index'].values[0]

    # vectorization

    combined_features = data['genres'] + ' ' + \
        data['keywords'] + ' ' + data['director'] + data['title']
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(
        feature_vectors, feature_vectors[index_of_the_movie])
    similarity_scores = list(enumerate(similarity))
    sorted_similar_movies = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True)

    suggested_movies = []

    for movie in sorted_similar_movies:
        if len(suggested_movies) < 16:
            index = movie[0]
            tconst_of_movie = data[data.index == index]['tconst'].values[0]
            if tconst_of_movie not in suggested_movies:
                suggested_movies.append(tconst_of_movie)
            else:
                continue
        else:
            break

    tconst_of_input_movie = data[data.index ==
                                 index_of_the_movie]['tconst'].values[0]
    final_movies = suggested_movies[1:]
    random.shuffle(final_movies)
    final_movies = final_movies[:3]
    return (tconst_of_input_movie, final_movies)


def api_url(id, api):
    return f'https://api.themoviedb.org/3/find/{id}?api_key={api}&language=en-US&external_source=imdb_id'


def display_movie(msg, id, response):
    st.subheader(msg)
    c1, c2 = st.columns((1, 3))
    with c1:
        poster_path = response['movie_results'][0]['poster_path']
        st.image(f'https://image.tmdb.org/t/p/original/{poster_path}')
    with c2:
        title = response['movie_results'][0]['title']
        st.write(f'Title: {title}')
        overview = response['movie_results'][0]['overview']
        st.write(f'Overview: {overview}')
        release_date = response['movie_results'][0]['release_date']
        st.write(f'Release Date: {release_date}')
        imdb_link = f"https://www.imdb.com/title/{id}/"
        st.write(f"[IMDb Link]({imdb_link})")
