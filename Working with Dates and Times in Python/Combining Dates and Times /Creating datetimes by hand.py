'''Often you create datetime objects based on outside data. Sometimes though,
you want to create a datetime object from scratch.

You're going to create a few different datetime objects from scratch to get ' \
   'the hang of that process. These come from the bikeshare data set that you'll
use throughout the rest of the chapter.'''

# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print(dt_old)