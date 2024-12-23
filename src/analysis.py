import pandas as pd

# Load the CSV file
df = pd.read_csv('data/watchlist.csv')

# Insights
print("\nINSIGHTS:")

# 1. Most frequently watched actors/directors
if 'Directors' in df.columns:
    most_watched_directors = (
        df['Directors']
        .dropna()
        .str.split(',')
        .explode()
        .value_counts()
        .head(10)
    )
    print("\nMost Watched Directors:")
    print(most_watched_directors)

# 2. Favorite genres
if 'Genres' in df.columns:
    favorite_genres = (
        df['Genres']
        .dropna()
        .str.split(',')
        .explode()
        .value_counts()
        .head(10)
    )
    print("\nFavorite Genres:")
    print(favorite_genres)

# 3. Average IMDb Rating of watched titles
if 'IMDb Rating' in df.columns:
    avg_imdb_rating = df['IMDb Rating'].mean()
    print(f"\nAverage IMDb Rating of Watched Titles: {avg_imdb_rating:.2f}")

# 4. Average runtime of watched movies/shows
if 'Runtime (mins)' in df.columns:
    avg_runtime = df['Runtime (mins)'].mean()
    print(f"\nAverage Runtime (mins): {avg_runtime:.2f}")

# 5. Most common release years
if 'Year' in df.columns:
    most_common_years = df['Year'].value_counts().head(5)
    print("\nMost Common Release Years:")
    print(most_common_years)

# 6. Most rated titles
if 'Your Rating' in df.columns and 'Title' in df.columns:
    highest_rated_titles = df[df['Your Rating'] == df['Your Rating'].max()]
    print("\nYour Highest-Rated Titles:")
    print(highest_rated_titles[['Title', 'Your Rating', 'Directors']])

# 7. Titles by Rating (if you have rated them)
if 'Your Rating' in df.columns:
    rating_counts = df['Your Rating'].value_counts().sort_index()
    print("\nCount of Titles by Your Ratings:")
    print(rating_counts)

# 8. Most recent movies watched (by Date Rated)
if 'Date Rated' in df.columns:
    df['Date Rated'] = pd.to_datetime(df['Date Rated'], errors='coerce')
    most_recent_watched = df.sort_values('Date Rated', ascending=False).head(5)
    print("\nMost Recently Rated Titles:")
    print(most_recent_watched[['Title', 'Date Rated', 'Your Rating']])
