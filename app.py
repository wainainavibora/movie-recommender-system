import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie = str(movie).strip()
    # ensure titles are strings and stripped
    movies['title'] = movies['title'].astype(str).str.strip()
    movie_indices = movies.index[movies['title'].eq(movie)].tolist()
    if len(movie_indices) == 0:
        st.error(f"Movie '{movie}' not found in dataset!")
        return [], []
    movie_index = movie_indices[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_name = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)

    return recommended_movies_name, recommended_movies_posters

st.header('Movie Recommender System')

# Load data
movies_data = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert dict to DataFrame if needed
if isinstance(movies_data, dict):
    movies = pd.DataFrame(movies_data)
else:
    movies = movies_data.copy()

# Ensure 'title' and 'movie_id' columns exist
if 'title' not in movies.columns or 'movie_id' not in movies.columns:
    st.error("Movies data must have 'title' and 'movie_id' columns!")
    st.stop()

# Prepare movie list
movie_list = movies['title'].astype(str).str.strip().tolist()

# Dropdown selection
selected_movie = st.selectbox(
    'Select a movie from the dropdown',
    movie_list
)

st.write("You selected:", selected_movie)

if st.button('Show Recommendations'):
    recommended_movies_name, recommended_movies_posters = recommend(selected_movie)
    if recommended_movies_name:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movies_name[0])
            st.image(recommended_movies_posters[0])
        with col2:
            st.text(recommended_movies_name[1])
            st.image(recommended_movies_posters[1])
        with col3:
            st.text(recommended_movies_name[2])
            st.image(recommended_movies_posters[2])
        with col4:
            st.text(recommended_movies_name[3])
            st.image(recommended_movies_posters[3])
        with col5:
            st.text(recommended_movies_name[4])
            st.image(recommended_movies_posters[4])





