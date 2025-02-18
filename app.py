# import streamlit as st
# import pickle
# import requests
# import base64
# def fetch_poster(movie_id):
#      url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
#      data=requests.get(url)
#      data=data.json()
#      poster_path = data['poster_path']
#      full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
#      return full_path

# movies = pickle.load(open("movies_list.pkl", 'rb'))
# similarity = pickle.load(open("similarity.pkl", 'rb'))
# movies_list=movies['title'].values

# st.header("Movie Recommender System")

# import streamlit.components.v1 as components

# imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")



# imageUrls = [
#     fetch_poster(370665),
#     fetch_poster(299536),
#     fetch_poster(17455),
#     fetch_poster(2830),
#     fetch_poster(429422),
#     fetch_poster(9722),
#     fetch_poster(13972),
#     fetch_poster(240),
#     fetch_poster(155),
#     fetch_poster(598),
#     fetch_poster(914),
#     fetch_poster(255709),
#     fetch_poster(572154)
   
#     ]


# imageCarouselComponent(imageUrls=imageUrls, height=200)
# selectvalue=st.selectbox("Select movie from dropdown", movies_list)

# def recommend(movie):
#     index=movies[movies['title']==movie].index[0]
#     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
#     recommend_movie=[]
#     recommend_poster=[]
#     for i in distance[1:6]:
#         movies_id=movies.iloc[i[0]].id
#         recommend_movie.append(movies.iloc[i[0]].title)
#         recommend_poster.append(fetch_poster(movies_id))
#     return recommend_movie, recommend_poster



# if st.button("Show Recommend"):
#     movie_name, movie_poster = recommend(selectvalue)
#     col1,col2,col3,col4,col5=st.columns(5)
#     with col1:
#         st.text(movie_name[0])
#         st.image(movie_poster[0])
#     with col2:
#         st.text(movie_name[1])
#         st.image(movie_poster[1])
#     with col3:
#         st.text(movie_name[2])
#         st.image(movie_poster[2])
#     with col4:
#         st.text(movie_name[3])
#         st.image(movie_poster[3])
#     with col5:
#         st.text(movie_name[4])
#         st.image(movie_poster[4])
















# import streamlit as st
# import pickle
# import requests
# import base64

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=6f86f165e63c6ad7b794f43f89671dc8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# movies = pickle.load(open("movies_list.pkl", 'rb'))
# similarity = pickle.load(open("similarity.pkl", 'rb'))
# movies_list = movies['title'].values

# st.header("Movie Recommender System")

# import streamlit.components.v1 as components

# imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

# imageUrls = [
#     fetch_poster(370665),
#     fetch_poster(299536),
#     fetch_poster(17455),
#     fetch_poster(2830),
#     fetch_poster(429422),
#     fetch_poster(9722),
#     fetch_poster(13972),
#     fetch_poster(240),
#     fetch_poster(155),
#     fetch_poster(598),
#     fetch_poster(914),
#     fetch_poster(255709),
#     fetch_poster(572154)
# ]

# imageCarouselComponent(imageUrls=imageUrls, height=200)

# selectvalue = st.selectbox("Select movie from dropdown", movies_list)

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
#     recommend_movie = []
#     recommend_poster = []
#     for i in distance[1:9]:  # Fetch top 8 recommendations
#         movies_id = movies.iloc[i[0]].id
#         recommend_movie.append(movies.iloc[i[0]].title)
#         recommend_poster.append(fetch_poster(movies_id))
#     return recommend_movie, recommend_poster

# if st.button("Show Recommend"):
#     movie_name, movie_poster = recommend(selectvalue)
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.text(movie_name[0])
#         st.image(movie_poster[0])
#     with col2:
#         st.text(movie_name[1])
#         st.image(movie_poster[1])
#     with col3:
#         st.text(movie_name[2])
#         st.image(movie_poster[2])
#     with col4:
#         st.text(movie_name[3])
#         st.image(movie_poster[3])

#     col5, col6, col7, col8 = st.columns(4)
#     with col5:
#         st.text(movie_name[4])
#         st.image(movie_poster[4])
#     with col6:
#         st.text(movie_name[5])
#         st.image(movie_poster[5])
#     with col7:
#         st.text(movie_name[6])
#         st.image(movie_poster[6])
#     with col8:
#         st.text(movie_name[7])
#         st.image(movie_poster[7])




import streamlit as st
import pickle
import requests
import time
import streamlit.components.v1 as components

# Cache API Calls to Reduce Load
@st.cache_data
def fetch_poster(movie_id):
    time.sleep(0.5)  # Avoid API rate limits
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f86f165e63c6ad7b794f43f89671dc8"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises error if request fails
        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# Load Movie Data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit UI
st.header("🎬 Movie Recommender System")

# Image Carousel
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

# Default Posters for Carousel (5 instead of 13 for better performance)
imageUrls = [
    fetch_poster(370665),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(20453),
    fetch_poster(9722),
    fetch_poster(13),
    fetch_poster(240),
    fetch_poster(680),
    fetch_poster(598),
    fetch_poster(786)
]

imageCarouselComponent(imageUrls=imageUrls, height=200)

# Movie Selection Dropdown
selectvalue = st.selectbox("🎥 Select a movie:", movies_list)

# Movie Recommendation Function
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []  # Return empty lists if the movie is not found

    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movie = []
    recommend_poster = []

    for i in distance[1:9]:  # Fetch top 8 recommendations
        if i[0] < len(movies):  # Ensure index is valid
            movie_id = movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movie_id))

    return recommend_movie, recommend_poster

# Show Recommendations on Button Click
if st.button("🎬 Show Recommendations"):
    if selectvalue:
        movie_name, movie_poster = recommend(selectvalue)
        if movie_name:
            # Display movies in 2 rows, 4 columns each
            cols = st.columns(4)
            for i in range(4):
                with cols[i]:
                    st.text(movie_name[i])
                    st.image(movie_poster[i])

            cols = st.columns(4)
            for i in range(4, 8):
                with cols[i - 4]:
                    st.text(movie_name[i])
                    st.image(movie_poster[i])
        else:
            st.warning("⚠️ No recommendations found!")
    else:
        st.warning("⚠️ Please select a movie first!")
