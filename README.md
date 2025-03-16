# 🎬 Movie Recommendation System

This is a **Movie Recommendation System** built using **Python, Streamlit, and Scikit-Learn**. It utilizes **cosine similarity** to recommend movies based on a dataset from **Kaggle**. The system preprocesses the data and provides an interactive web interface using Streamlit.

## 🚀 Features
- Movie recommendations based on **cosine similarity**.
- **Preprocessing** of movie data to improve recommendation accuracy.
- **Interactive UI** built with **Streamlit**.
- Fetches **movie posters** using The Movie Database (TMDb) API.

## 📂 Dataset
The dataset used for this movie recommendation project was sourced from **Kaggle** and contains comprehensive metadata about movies. It includes attributes such as **title, genres, overview (description), release date, cast, crew, and ratings**. The dataset provides crucial information for building an effective recommendation system by analyzing movie content, user preferences, and trends. With details about the **actors, directors, and other crew members**, it enables filtering and suggesting movies based on collaborative and content-based approaches. The **ratings and reviews** further help in ranking and recommending movies that align with user interests.

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**:
   ```sh
   streamlit run app.py
   ```

## 📌 Usage
1. Enter/select a movie from the dropdown.
2. Click **"Show Recommendation"**.
3. The system will display **top 5 similar movies** with their posters.

## 🖥️ Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Scikit-Learn** (for cosine similarity calculations)
- **Pandas** (for data processing)
- **Requests** (for fetching movie posters from TMDb API)

## 🔥 Future Improvements
- Add user-based collaborative filtering.
- Improve recommendation algorithm with deep learning.
- Include more metadata like directors and cast for better recommendations.

---

### 🎥 Made with ❤️ for movie lovers!

