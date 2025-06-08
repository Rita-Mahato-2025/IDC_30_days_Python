from datetime import datetime

date1 = datetime(2025, 5, 28)
date2 = datetime.now()

difference = date2 - date1

print ("Number of days between the dates: ", difference.days)
