
from dateutil.rrule import rrule, MONTHLY
from datetime import datetime

days = rrule(MONTHLY, dtstart=datetime(1901, 1, 1), until=datetime(2000, 12, 31))

print(sum(1 for day in days if day.weekday() == 6))
