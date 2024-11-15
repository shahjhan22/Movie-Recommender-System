# 🎬 Movie Recommender System

A content-based movie recommender system built with Python that suggests movies similar to a user-selected title. Leveraging a dataset of over 5000 movies, it recommends movies based on descriptions, genres, and actors to enhance user discovery.

## 📜 Project Overview
This project aims to deliver personalized movie recommendations by analyzing the content of movies (such as plot descriptions, genres, and cast details). By converting text-based features into numerical representations, the system efficiently calculates similarity scores to find and recommend similar movies.

https://github.com/user-attachments/assets/6678f027-3a49-4f11-8920-b675804ac54b



### Key Features
- **Content-Based Filtering**: Recommends movies by analyzing descriptions, genres, and actors related to the user-selected movie.
- **Cosine Similarity**: Uses vector-based similarity measurement to identify and recommend the top 5 similar movies.
- **Interactive User Interface**: A simple and user-friendly web interface built with Streamlit allows users to input a movie title and view personalized movie recommendations with posters.

## 🚀 Technologies Used
- **Python**: Core programming language.
- **Pandas and NumPy**: For data manipulation and efficient numerical computations.
- **Natural Language Processing (NLP)**: For preprocessing and vectorizing text data.
- **Bag of Words (BoW)**: Converts movie content (tags) into feature vectors for comparison.
- **Cosine Similarity**: Measures the similarity between feature vectors to find related movies.
- **Streamlit**: Provides an interactive UI for the recommender system.

## 📊 Dataset
The dataset consists of 5000+ movies with features like titles, descriptions, genres, actors, and release dates. These features are preprocessed and combined to allow content-based filtering, where movies are recommended based on similarities to user-selected titles.

## 🧩 How It Works

### Data Preprocessing:
- Each movie's attributes (e.g., title, genres, description, and actors) are combined into a single text-based "tag."
- These tags are transformed into feature vectors using the **Bag of Words (BoW)** model, which allows text-based content to be represented numerically for similarity analysis.

### Similarity Calculation:
- Using **cosine similarity**, the system compares the BoW vectors of movies. This similarity score indicates how closely related two movies are based on their content.
- When a user selects a movie, the system calculates similarity scores between the chosen movie and all others, identifying the top 5 most similar titles.

### Interactive User Interface:
- The app’s interface, built with **Streamlit**, allows users to select a movie from a dropdown menu.
- Once a movie is selected, the system recommends similar movies by displaying their posters and titles, offering an engaging and visual experience for exploring related films.
