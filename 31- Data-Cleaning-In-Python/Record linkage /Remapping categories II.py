'''In the last exercise, you determined that the distance cutoff point for remapping typos of 'american', 'asian', and 'italian' cuisine types stored in the cuisine_type column should be 80.

In this exercise, you're going to put it all together by finding matches with similarity scores equal to or higher than 80 by using fuzywuzzy.process's extract() function, for each correct cuisine type, and replacing these matches with it. Remember, when comparing a string with an array of strings using process.extact(), the output is a list of tuples where each of tuple is as such:

(closest match, similarity score, index of match)
The restaurants DataFrame is in your environment, alongside a categories DataFrame containing the correct cuisine types in the cuisine_type column.'''

# For each correct cuisine_type in categories
for cuisine in categories['cuisine_type']:
    # Find matches in cuisine_type of restaurants
    matches = process.extract(cuisine, restaurants['cuisine_type'],
                              limit=restaurants.shape[0])

    # For each possible_match with similarity score >= 80
    for possible_match in matches:
        if possible_match[1] >= 80:
            # Find matching cuisine type
            matching_cuisine = restaurants['cuisine_type'] == possible_match[0]
            restaurants.loc[matching_cuisine, 'cuisine_type'] = cuisine

# Print unique values to confirm mapping
print(restaurants['cuisine_type'].unique())