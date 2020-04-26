'''Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, you'll count the number of each type of store and the number of each department number.

The stores and departments DataFrames you created in the last exercise are available and pandas is imported as pd.'''

# Count the number of stores of each type
store_counts = stores["store_type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = stores["store_type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = departments["department_num"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = departments["department_num"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)