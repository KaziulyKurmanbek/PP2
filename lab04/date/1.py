from datetime import datetime, timedelta
today = datetime.now()
print("Today: ", today.strftime("%x"))
five_days_ago = today - timedelta(5)
print("five_days_ago: ", five_days_ago.strftime("%x"))