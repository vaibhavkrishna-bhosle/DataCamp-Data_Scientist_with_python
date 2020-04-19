'''Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone:
        'America/New_York'. Since we know their political jurisdiction, we don't need
to look up their UTC offset. Python will do that for us.'''

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=et)
  trip['end'] = trip['end'].replace(tzinfo=et)