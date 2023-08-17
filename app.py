import streamlit as st
import pickle
import numpy as np
import pandas
import requests
# movies_list = pandas.read_pickle(open('movies_new.pkl','rb'))
movies_list = pickle.load(open('movies_new.pkl','rb'))
# scores=pandas.read_pickle(open('similarity.pkl','rb'))
scores=pickle.load(open('similarity.pkl','rb'))
title = movies_list.original_title.values
def movie_recommend(title):
    idx=np.where(movies_list['original_title']==title)[0][0]
    score_list=list(enumerate(scores[idx]))
    score_list=sorted(score_list,key=lambda x: x[1],reverse=True)
    recommended_=score_list[1:6]
    recommended_idx=[i[0] for i in recommended_]
    recommended_movies=movies_list['original_title'].iloc[recommended_idx]
    return recommended_movies

def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=83dd2fde626760e1a8352064496e9903')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + str(data['poster_path'])

st.title('Movie Recommender System')

selected_movie_name=st.selectbox('Enter the movie name here',tuple(list(title)))

if st.button('Recommend'):
    recommended_movies=movie_recommend(selected_movie_name).values
    recommended_movies_id=movie_recommend(selected_movie_name).index
    #for i in recommended_movies:
        #st.write(i)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(fetch_poster(movies_list.loc[recommended_movies_id[0],'id']))
    with col2:
        st.text(recommended_movies[1])
        st.image(fetch_poster(movies_list.loc[recommended_movies_id[1],'id']))
    with col3:
        st.text(recommended_movies[2])
        st.image(fetch_poster(movies_list.loc[recommended_movies_id[2],'id']))
    with col4:
        st.text(recommended_movies[3])
        st.image(fetch_poster(movies_list.loc[recommended_movies_id[3],'id']))
    with col5:
        st.text(recommended_movies[4])
        st.image(fetch_poster(movies_list.loc[recommended_movies_id[4],'id']))


