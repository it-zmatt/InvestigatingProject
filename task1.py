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
plt.show()

# Task 4

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv('dataset/netflix_data.csv')

# Print the first five rows of the DataFrame
print(netflix_df[0:5])