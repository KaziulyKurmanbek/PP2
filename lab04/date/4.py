from datetime import datetime
time1 = input("Enter the 1st date (YYYY-MM-DD HH:MM:SS): ")
time2 = input("Enter the 2nd date (YYYY-MM-DD HH:MM:SS): ")
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(time1, date_format)
date2 = datetime.strptime(time2, date_format)
diff = abs(date1 - date2)
seconds_diff = diff.total_seconds()
print(seconds_diff)