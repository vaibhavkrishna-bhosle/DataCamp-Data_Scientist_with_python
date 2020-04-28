'''Before you analyze data, you will need to read the data into a pandas DataFrame. In this exercise, you will be looking at data from US School Improvement Grants in 2010. This program gave nearly $4B to schools to help them renovate or improve their programs.

This first step in most data analysis is to import pandas and seaborn and read a data file in order to analyze it further.

This course introduces a lot of new concepts, so if you ever need a quick refresher, download the Seaborn Cheat Sheet and keep it handy!'''

# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)

