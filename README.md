# Movie Recommendation System

## Overview
This Python program recommends movies based on user preferences for language and genre. It uses a hybrid machine learning approach, combining **content-based filtering** with similarity analysis. The program processes a dataset containing movie metadata and ranks the most relevant movies according to user-selected criteria.

## Features
- Displays a list of available genres to assist user selection.
- Filters movies by user-selected language and genre.
- Sorts recommendations by IMDb Score and IMDb Votes for relevance.
- Outputs results in a clear table format with the movie's title and rating.

## How Machine Learning is Used
The program leverages **machine learning techniques** in the following ways:

### Content-Based Filtering
1. **Feature Extraction**:
   - Combines `Genre` and `Languages` into a single feature string for each movie.
   - Uses **CountVectorizer** to convert the text data into a bag-of-words model, creating a numerical representation of movie features.

2. **Similarity Calculation**:
   - Computes pairwise similarity between movies using **cosine similarity**.
   - This allows the program to find movies with features similar to the user’s preferences.

### Ranking
Once filtered by user criteria, the movies are sorted based on:
- **IMDb Score**: Ensures recommendations are high-quality movies.
- **IMDb Votes**: Incorporates popularity into the ranking.

## Dataset
The program uses a dataset with the following columns:
- **Title**: Name of the movie.
- **Genre**: Genres associated with the movie (e.g., Action, Drama).
- **Languages**: Languages available for the movie (e.g., English, Hindi).
- **IMDb Score**: Average rating from IMDb.
- **IMDb Votes**: Number of votes, reflecting popularity.

## How to Use
1. Place the dataset file (`netflix-rotten-tomatoes-metacritic-imdb.csv`) in the same directory as the script.
2. Run the program:
   ```bash
   python movie_recommendation.py
   ```
3. The program will display all available genres.
4. Enter your preferred language and genre when prompted.
5. View the top recommendations in a table format, showing:
   - **Title**: Name of the movie.
   - **Rating**: IMDb Score.

## Example Output
```
Available genres:
- Action
- Drama
- Comedy
- Thriller

Enter preferred language: English
Enter preferred genre: Action

Top Movie Recommendations:
                   Title  Rating
    Avengers: Endgame    8.4
             Inception    8.8
          The Dark Knight  9.0
```

## Dependencies
- Python 3.7+
- pandas
- scikit-learn

Install dependencies with:
```bash
pip install pandas scikit-learn
```

## Future Enhancements
- Add collaborative filtering to incorporate user-item interaction data.
- Support additional ranking metrics (e.g., Rotten Tomatoes score).
- Enhance input handling to allow multiple genres and languages.

## Author
This program demonstrates a practical application of machine learning for personalized recommendations. Feedback and suggestions are welcome!

