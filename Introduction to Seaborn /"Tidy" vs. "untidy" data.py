'''Here, we have a sample dataset from a survey of children about their favorite animals. But can we use this dataset as-is with Seaborn? Let's use Pandas to import the csv file with the data collected from the survey and determine whether it is tidy, which is essential to having it work well with Seaborn.

To get you started, the filepath to the csv file has been assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.'''

# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())