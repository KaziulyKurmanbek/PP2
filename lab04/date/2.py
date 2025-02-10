from datetime import datetime, timedelta
today = datetime.now()
print("today: ", today.strftime("%x"))
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)
print("yesterday: ", yesterday.strftime("%x"))
print("tomorrow: ", tomorrow.strftime("%x"))