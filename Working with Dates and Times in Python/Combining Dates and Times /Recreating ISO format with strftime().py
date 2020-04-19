'''In the last chapter, you used strftime() to create strings from date objects.
Now that you know about datetime objects, let's practice doing something similar.

Re-create the .isoformat() method, using .strftime(), and print the first trip start in our data set.'''


# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))