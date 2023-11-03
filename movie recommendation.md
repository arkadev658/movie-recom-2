**Movie Recommendation System**

-   **Movie data sources**: The project uses two datasets from Kaggle, which contain information about 4803 movies from The Movie Database (TMDB). The datasets are **tmdb_5000_movies.csv** and **tmdb_5000_credits.csv**.
-   **Data integration and cleaning**: The project merges the two datasets on the movie id column, and drops unnecessary columns such as budget, homepage, revenue, etc. The project also handles missing and duplicate values, and formats the data types of the columns.
-   **Data transformation and feature engineering**: The project transforms the columns that contain JSON objects, such as genres, keywords, cast, and crew, into lists of strings. The project also creates a new column called tags, which combines the genres, keywords, overview, cast, and crew of each movie into a single string. The project then applies stemming to the tags column to reduce the words to their root forms.
-   **Data vectorization and similarity measurement**: The project uses the **TfidfVectorizer** from sklearn to convert the tags column into a matrix of TF-IDF features. The project then uses the **cosine_similarity** function from sklearn to calculate the pairwise similarity scores between the movies based on their tags.
-   **Recommendation system**: The project defines a function called **recommend**, which takes a movie title as input and returns the top five most similar movies as output. The function uses the similarity matrix and the movie index to find the movies with the highest similarity scores. The function also handles invalid or unknown movie titles.
-   **Streamlit App**

    After that we have implemented the system using streamlit app
