'''Having set the timezone for the first ten rides that W20529 took,
let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.'''

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Loop over the trips
for trip in onebike_datetimes[:10]:
    # Pull out the start and set it to UTC
    dt = trip['start'].astimezone(timezone.utc)

    # Print the start time in UTC
    print('Original:', trip['start'], '| UTC:', dt.isoformat())