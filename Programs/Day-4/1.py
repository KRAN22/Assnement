import datetime
months = {}
for i in range(1,13):
    months[datetime.date(2020, i, 1).strftime('%B').lower()] = i
print(months)
