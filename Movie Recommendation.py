import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
def load_data():
    file_path = 'DataSet.csv'
    data = pd.read_csv(file_path)
    return data

# Preprocess dataset
def preprocess_data(data):
    # Select relevant columns
    data = data[['Title', 'Genre', 'Languages', 'IMDb Score', 'IMDb Votes']]

    # Fill missing values
    data['Genre'] = data['Genre'].fillna('')
    data['Languages'] = data['Languages'].fillna('')
    data['IMDb Score'] = data['IMDb Score'].fillna(0)
    data['IMDb Votes'] = data['IMDb Votes'].fillna(0)

    return data

# Content-based filtering using genres and language
def content_based_filtering(data):
    # Combine genres and languages into a single feature
    data['combined_features'] = data['Genre'] + " " + data['Languages']

    # Vectorize the combined features
    vectorizer = CountVectorizer()
    feature_matrix = vectorizer.fit_transform(data['combined_features'])

    # Compute cosine similarity
    similarity_matrix = cosine_similarity(feature_matrix, feature_matrix)
    return similarity_matrix

# Recommend movies based on user input
def recommend_movies(data, similarity_matrix, language, genre, top_n=10):
    # Filter movies by language and genre
    filtered_movies = data[(data['Languages'].str.contains(language, case=False)) &
                           (data['Genre'].str.contains(genre, case=False))]

    # Sort by IMDb Score and IMDb Votes
    filtered_movies = filtered_movies.sort_values(by=['IMDb Score', 'IMDb Votes'], ascending=False)

    # Select top-rated movies
    recommendations = filtered_movies.head(top_n)
    return recommendations

def main():
    # Load and preprocess data
    data = load_data()
    data = preprocess_data(data)

    # Generate similarity matrix for content-based filtering
    similarity_matrix = content_based_filtering(data)

    # User input
    language = input("Enter preferred language: ")
    genre = input("Enter preferred genre: ")

    # Get recommendations
    recommendations = recommend_movies(data, similarity_matrix, language, genre)

    # Display recommendations in table format
    print("\nTop Movie Recommendations:")
    print(recommendations[['Title', 'IMDb Score']].to_string(index=False, header=['Title', 'Rating']))

if __name__ == "__main__":
    main()




