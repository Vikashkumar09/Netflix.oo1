# -*- coding: utf-8 -*-
"""Netflix Movies and Tv Shows.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ZIjJgAe1BM7qZR4jcfW2nIiDTH4Rn70
"""

# importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading the dataset
netflix = pd.read_csv('/content/sample_data/netflix_titles.csv')

netflix

# show the dataset info
netflix.info()

# dropping any duplicates
netflix.dropna(inplace= True)

netflix

# show the dataset info after dropping the duplicates
netflix.info()

netflix.reset_index(drop=True)

netflix.isnull()

netflix.isnull().sum()

# Convert to datetime
netflix['date_added'] = pd.to_datetime(netflix['date_added'], errors='coerce')

netflix

# Format as dd-mm-yyyy
netflix['date_added'] = netflix['date_added'].dt.strftime('%d-%m-%Y')

netflix

netflix['director'] = netflix['director'].str.lower()

netflix

"""Replace Inconsistent Values"""

netflix['country'] = netflix['country'].replace({
    'United States': 'USA',
    'U.S.': 'USA',
    'UK': 'United Kingdom'
})

netflix

"""use.str.replace() for pattern-based replacement:"""

netflix['title'] = netflix['title'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)  # Remove special characters

netflix



"""Clean Multiple Columns"""

columns_to_clean = ['title', 'director', 'country']

for col in columns_to_clean:
    netflix[col] = netflix[col].astype(str).str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

netflix

# edit the date_added column
netflix['date_added'] = pd.to_datetime(netflix['date_added'], errors='coerce', infer_datetime_format=True)

# show the dataset info after editting the date_added column
netflix.info()

# type column
types = netflix['type'].value_counts().reset_index()
types

#director column
directors = netflix['director'].value_counts().reset_index()
directors

#director and type columns
directors = netflix.groupby(['director', 'type'])['director'].value_counts().reset_index()
directors

#top 10 directors
top_10_directors = netflix.groupby(['director', 'type'])['director'].value_counts().sort_values(ascending=False).iloc[2:12]
top_10_directors

#country column
countries = netflix.groupby(['country', 'type'])['country'].value_counts().reset_index()
countries

top_10_countries = netflix.groupby(['country', 'type'])['country'].value_counts().sort_values(ascending = False).iloc[0:10]
top_10_countries

top_10_TV_Show_countries = countries[countries['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_TV_Show_countries

top_10_movie_countries = countries[countries['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_movie_countries

# release_year column
release_years = netflix.groupby(['release_year', 'type'])['release_year'].value_counts().reset_index()
release_years

top_10_movies_years = release_years[release_years['type'] == 'Movie'].sort_values(by= 'count', ascending=False).iloc[0:10]
top_10_movies_years

top_10_TV_show_years = release_years[release_years['type'] == 'TV show'].sort_values(by= 'count', ascending=False).iloc[0:10]
top_10_TV_show_years

# rating column
ratings = netflix.groupby(['rating', 'type'])['type'].value_counts().reset_index()
ratings

top_10_movies_ratings = ratings[ratings['type'] == 'Movie'].sort_values(by= 'count',ascending=False).iloc[0:10]
top_10_movies_ratings

top_10_TV_Show_ratings = ratings[ratings['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_TV_Show_ratings

durations = netflix.groupby(['duration','type'])['duration'].value_counts().reset_index()
durations

top_10_movie_durations = durations[durations['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_movie_durations

top_10_TV_Show_durations = durations[durations['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_TV_Show_durations

# listed_in column
listed_in = netflix.groupby(['listed_in', 'type'])['listed_in'].value_counts().reset_index()
listed_in

top_10_listed_in_movie = listed_in[listed_in['type'] == 'Movie'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_listed_in_movie

top_10_listed_in_TV_Show = listed_in[listed_in['type'] == 'TV Show'].sort_values(by='count', ascending=False).iloc[0:10]
top_10_listed_in_TV_Show

# visualizing the types of shows
types.set_index('type', inplace=True)
types.plot.pie(y = 'count', autopct='%.2f%%', legend='type')
plt.title("Moives VS TV Shows")
plt.show()

#visualizing the director column
plt.figure(figsize=(20, 10))
top_10_directors.plot(x='director', y='count', kind='bar')
plt.title('Top 10 Directors')
plt.xlabel('Director')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

#visualizing the country column
plt.figure(figsize=(20, 8))
top_10_countries.plot(x='country', y='country', kind='bar')
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

# visualizing the release_year column
netflix['release_year'].plot(kind='hist', bins=30)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

# visualizing the rating column
top_10_movies_ratings.plot(x='rating', y='count', kind='bar')
plt.title('Top 10 Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

top_10_TV_Show_ratings.plot(x='rating', y='count', kind='bar')
plt.title('Top 10 TV Shows Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# visualizing the duration column
top_10_movie_durations.plot(x='duration', y='count', kind='bar')
plt.title('Top 10 Movie Durations')
plt.xlabel('Duration')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

top_10_TV_Show_durations.plot(x='duration', y='count', kind='bar')
plt.title('Top 10 TV Shows Durations')
plt.xlabel('Duration')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# visualizing the listed_in column
top_10_listed_in_movie.plot(x='listed_in', y='count', kind='bar')
plt.title('Top 10 Listed Genres for Movies')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

top_10_listed_in_TV_Show.plot(x='listed_in', y='count', kind='bar')
plt.title('Top 10 Listed Genres for TV Shows')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()