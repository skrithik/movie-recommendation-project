import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie
import time

# Page configuration
st.set_page_config(
    page_title="Cinema Sage - Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# Load data
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity


movies, similarity = load_data()


# Load animations
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Animation assets
movie_animation = load_lottie("https://assets3.lottiefiles.com/packages/lf20_khzniaya.json")
loading_animation = load_lottie("https://assets5.lottiefiles.com/private_files/lf30_bb9bkg1h.json")


# Fetch movie poster and details
def fetch_movie_details(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()

    details = {
        'poster_path': f"https://image.tmdb.org/t/p/w500/{data.get('poster_path', '')}",
        'release_date': data.get('release_date', 'N/A'),
        'vote_average': data.get('vote_average', 'N/A'),
        'overview': data.get('overview', 'No overview available')
    }
    return details


# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommendations.append({
            'title': movies.iloc[i[0]].title,
            'poster': details['poster_path'],
            'release_date': details['release_date'],
            'rating': details['vote_average'],
            'overview': details['overview']
        })

    return recommendations


# Custom CSS for styling
st.markdown("""
    <style>
        /* General Styling */
        .main {
            background-color: #0a0a0a;
            color: #ffffff;
        }

        /* Header Styling */
        .title-container {
            background: linear-gradient(90deg, #E50914 0%, #8B0000 100%);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }

        /* Movie Card Styling */
        .movie-card {
            background-color: rgba(20, 20, 20, 0.7);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .movie-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        }

        .movie-poster {
            border-radius: 8px;
            width: 100%;
            transition: transform 0.3s ease;
        }

        .movie-poster:hover {
            transform: scale(1.05);
        }

        .movie-title {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            margin: 10px 0;
        }

        .movie-info {
            font-size: 14px;
            color: #cccccc;
        }

        /* Selected Movie Styling */
        .selected-movie-container {
            background-color: rgba(30, 30, 30, 0.8);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }

        /* Button Styling */
        .css-1x8cf1d {
            background-color: #E50914;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        .css-1x8cf1d:hover {
            background-color: #B2070F;
        }

        /* Divider */
        .divider {
            height: 3px;
            background: linear-gradient(90deg, transparent, #E50914, transparent);
            margin: 30px 0;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            color: #999999;
            font-size: 14px;
        }

        /* Animation Container */
        .animation-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("🎬 Cinema Sage: Discover Your Next Favorite Movie 🍿")
st.markdown('</div>', unsafe_allow_html=True)

# Side Animation
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(movie_animation, height=200, key="movie_animation")
with col2:
    st.markdown("### Welcome to Cinema Sage!")
    st.markdown("""
    Discover movies similar to your favorites using advanced machine learning. 
    Our system analyzes thousands of films to find the perfect recommendations just for you.

    👇 Get started by selecting a movie you love below!
    """)

# Movie selection with search
selected_movie = st.selectbox(
    "🔍 Search for a movie you enjoyed",
    movies['title'].values,
    index=0,
    help="Type to search or scroll through the list"
)

# Display selected movie details
if selected_movie:
    movie_index = movies[movies['title'] == selected_movie].index[0]
    movie_id = movies.iloc[movie_index].movie_id
    movie_details = fetch_movie_details(movie_id)

    st.markdown('<div class="selected-movie-container">', unsafe_allow_html=True)
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(movie_details['poster_path'], width=200)
    with cols[1]:
        st.markdown(f"### {selected_movie}")
        st.markdown(f"**Release Date:** {movie_details['release_date']}")
        st.markdown(f"**Rating:** ⭐ {movie_details['vote_average']}/10")
        st.markdown("**Overview:**")
        st.markdown(f"{movie_details['overview']}")
    st.markdown('</div>', unsafe_allow_html=True)

# Show Recommendations Button
if st.button('🎥 Find Similar Movies'):
    # Show loading animation
    with st.spinner("Finding your perfect movie matches..."):
        placeholder = st.empty()
        with placeholder.container():
            animation_col = st.columns([1, 1, 1])
            with animation_col[1]:
                st_lottie(loading_animation, height=200, key="loading")

        # Get recommendations
        recommendations = recommend(selected_movie)
        time.sleep(1.5)  # For effect
        placeholder.empty()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.subheader("🔥 Your Personalized Movie Recommendations")

    # Display recommendations in a grid
    columns = st.columns(5)
    for i, movie in enumerate(recommendations):
        with columns[i]:
            st.markdown(f'<div class="movie-card">', unsafe_allow_html=True)
            st.image(movie['poster'], use_container_width=True, caption=None)
            st.markdown(f'<div class="movie-title">{movie["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="movie-info">⭐ {movie["rating"]}/10 • {movie["release_date"][:4]}</div>',
                        unsafe_allow_html=True)

            with st.expander("Overview"):
                st.write(movie["overview"])
            st.markdown('</div>', unsafe_allow_html=True)

# Add footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">Cinema Sage © 2025 | Powered by TMDB API</div>', unsafe_allow_html=True)

# Add session state to track user history
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for history
with st.sidebar:
    st.title("Your Movie Journey")

    # View History
    if st.session_state.history:
        st.subheader("Recently Viewed")
        for movie in st.session_state.history[-5:]:
            st.markdown(f"• {movie}")

    # Additional Features
    st.subheader("Features")
    st.markdown("- 🌟 Personalized recommendations")
    st.markdown("- 📊 Smart matching algorithm")
    st.markdown("- 📝 Detailed movie information")

    # Add a feedback section
    st.subheader("Feedback")
    feedback = st.text_area("Share your thoughts:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# Add current movie to history when recommendations are shown
if 'recommendations' in locals() and selected_movie not in st.session_state.history:
    st.session_state.history.append(selected_movie)
