'''Pandas has a number of datetime-related attributes within the .dt accessor. Many of them are ones
you've encountered before, like .dt.month. Others are convenient and save time compared to standard Python, like .dt.weekday_name.'''
# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())