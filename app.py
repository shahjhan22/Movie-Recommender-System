
import pandas as pd
import streamlit as st
import pickle
import requests

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.plt', 'rb'))
movies = pd.DataFrame(movies_dict)

# Function to fetch movie poster using OMDB API
def fetch_poster(movie_title):
    response = requests.get(f'https://www.omdbapi.com/?apikey=a5d99ade&t={movie_title}')
    data = response.json()
    if data['Response'] == 'True' and 'Poster' in data:
        return data['Poster']
    else:
        return None

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_movies_posters

# Streamlit app layout
st.set_page_config(page_title="Movie Recommender System", page_icon="🎥", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .title {
        text-align: center;
        font-size: 48px;
        color: #e50914;
        font-weight: bold;
    }
    .movie-title {
        font-size: 18px;
        text-align: center;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>Movie Recommender System</div>", unsafe_allow_html=True)
selected_movie_name = st.selectbox('Write here Movie Name', movies['title'].values)
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommendations in columns with improved alignment
    cols = st.columns(5, gap="large")
    for i, col in enumerate(cols):
        with col:
            if i < len(names):
                st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
                if posters[i]:
                    st.image(posters[i], use_column_width=True)
                else:
                    st.write("Poster not available")



































# import pandas as pd
# import streamlit as st
# import pickle
# import requests
# movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# similarity=pickle.load(open('similarity.plt','rb'))
# movies=pd.DataFrame(movies_dict)
#
#
# def fetch_poster(movie_title):
#     response=requests.get('https://www.omdbapi.com/?apikey=a5d99ade&t={}'.format(movie_title))
#     data=response.json()
#     # st.text(data)
#     # st.text('https://www.omdbapi.com/?apikey=a5d99ade&t={}'.format(movie_title))
#     if data['Response'] == 'True' and 'Poster' in data:
#         return data['Poster']
#     else:
#         return None  # Return None if poster is not found
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distance = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
#     recommender=[]
#     recommended_movies_posters=[]
#     for i in movie_list:
#         movie_title=movies.iloc[i[0]].title
#         recommender.append(movies.iloc[i[0]].title)
#         # print(movie_id,"  and ", movies.iloc[i[0]].title)
#         # fetch poster api
#         recommended_movies_posters.append(fetch_poster(movie_title))
#     return  recommender,recommended_movies_posters
#
#
# st.title('Movie Recommender System')
# selected_movie_name=st.selectbox('Write here Movie Name',movies['title'].values)
# if st.button('Recommend'):
#     name,posters=recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.header(name[0])
#         st.image(posters[0])
#     with col2:
#         st.header(name[1])
#         st.image(posters[1])
#     with col3:
#         st.header(name[2])
#         st.image(posters[2])
#     with col4:
#         st.header(name[3])
#         st.image(posters[3])
#     with col5:
#         st.header(name[4])
#         st.image(posters[4])










