import datetime
current_date = datetime.datetime.now()

five_days_ago = current_date - datetime.timedelta(days=5)

print(current_date.strftime("%Y-%m-%d"))
print(five_days_ago.strftime("%Y-%m-%d"))