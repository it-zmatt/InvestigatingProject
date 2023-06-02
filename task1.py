import numpy as np

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

# Import pandas under its usual alias
import pandas as pd
# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)
print(durations_df)