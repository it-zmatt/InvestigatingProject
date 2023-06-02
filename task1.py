import numpy as np

# Task 1

# Create Year and Durations List
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {
    'years': years,
    'durations': durations
}

# Print the dictionary
print(movie_dict)


# Task 2

# Import pandas under its usual alias
import pandas as pd
# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# Task 3

# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(years, durations)
# Create a title
plt.title('Netflix Movie Durations 2011-2020')
# Show the plot


# Task 4

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv('dataset/netflix_data.csv')

# Print the first five rows of the DataFrame
print(netflix_df[0:5])

# Task 5

# Subset the DataFrame where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset[0:5])

# Task 6

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[['release_year']], netflix_movies_col_subset[['duration']])

# Create a title
plt.title('Movie Duration by Year of Release')
# Show the plot

# Task 7

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] <= 60]

# Print the first 20 rows of short_movies
print(short_movies[0:20])