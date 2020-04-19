'''date objects in Python have a great number of ways they can be printed out as strings.
In some cases, you want to know the date in a clear, language-agnostic format. In other cases,
you want something which can fit into a paragraph and flow naturally.

Let's try printing out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall ' \
   'in Florida), in a number of different ways, to practice using the .strftime() method.

A date object called andrew has already been created.
'''
# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))