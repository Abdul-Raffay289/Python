import calendar

# Get the list of month names
months = list(calendar.month_name)

# Display months (skip index 0 because it's empty)
for month in months[1:]:
    print(month)
    