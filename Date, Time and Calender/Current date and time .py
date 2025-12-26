from datetime import date, time , datetime
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nToday time is", now)
print("Date component", today.year, today.month, today.day)