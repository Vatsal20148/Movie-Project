import streamlit as st
import pickle
import pandas as pd
import base64

from altair.vegalite.v3.theme import theme


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('netflix.jpg')



def show_movies(movie):
     movie_index = movies[movies["Name"] == movie].index[0]

     distance = similarity[movie_index]

     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
     empty_list = []
     image_link = []
     for i in movie_list:
          empty_list.append(movies.iloc[i[0]].Name)
          image_link.append(movies.iloc[i[0]].PosterLink)
     return empty_list,image_link


similarity = pickle.load(open("similarity.pkl","rb"))
movies_list = pickle.load(open("movies_dict.pkl","rb"))
movies = pd.DataFrame(movies_list)
st.markdown("<h1 style='text-align: center; color: white;'>Recommend movies!</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left; color: white;'>Heyyy! Choose a movie</h4>", unsafe_allow_html=True)
option = st.selectbox("",movies["Name"].values)
if st.button("Recommend"):
     st.write(f"<h3 style='text-align: left; color: white;'>You searched for {option}</h1>", unsafe_allow_html = True)
     st.write("<h3 style='text-align: left; color: white;'>Recommendations for you:</h1>", unsafe_allow_html = True)
     # f"<h3 style='text-align: left; color: white;'>You searched for + {option}</h1>", unsafe_allow_html = True
     recommendations, poster = show_movies(option)
     col1, col2 = st.columns(2)
     with col1:
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[0]}</h4>", unsafe_allow_html = True)
         st.image(poster[0], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[2]}</h4>", unsafe_allow_html = True)
         st.image(poster[2], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[4]}</h4>", unsafe_allow_html = True)
         st.image(poster[4], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[6]}</h4>", unsafe_allow_html = True)
         st.image(poster[6], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[8]}</h4>", unsafe_allow_html = True)
         st.image(poster[8], width=250)

     with col2:
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[1]}</h4>", unsafe_allow_html = True)
         st.image(poster[1], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[3]}</h4>", unsafe_allow_html = True)
         st.image(poster[3], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[5]}</h4>", unsafe_allow_html = True)
         st.image(poster[5], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[7]}</h4>", unsafe_allow_html = True)
         st.image(poster[7], width=250)
         st.write(f"<h4 style='text-align: left; color: white;'>{recommendations[9]}</h4>", unsafe_allow_html = True)
         st.image(poster[9], width=250)
