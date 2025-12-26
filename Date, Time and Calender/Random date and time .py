import random
from datetime import datetime, timedelta
def randomdate(startdate, enddate):
    time_date = enddate-startdate
    random_days = random.randint(0, time_date.days)
    return startdate + timedelta(days=random_days)
start = datetime(2025, 12, 26)
end = datetime(2026, 12, 26)
print(randomdate(start, end).strftime('%m/%d/%Y'))