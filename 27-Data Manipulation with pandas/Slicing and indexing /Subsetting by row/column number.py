'''The most common ways to subset rows are the ways we've previously discussed: using a Boolean condition, or by index labels. However, it is also occasionally useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to let you subset by rows and columns.

pandas is loaded as pd. temperatures (without an index) is available.'''

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])