from datetime import datetime
format = "%Y-%m-%d %H:%M:%S"
date1="2025-01-17 17:00:00"
date2="2025-01-02 18:30:00"
dt1=datetime.strptime(date1,format)
dt2=datetime.strptime(date2,format)
difference=abs((dt1-dt2).total_seconds())
print(difference)
