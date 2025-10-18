from datetime import datetime, date, time, timedelta

# today = date.today()
# today = datetime.now()
date_ = date(2025, 10, 18)
print(date_)
print(date_.isocalendar())
print(date_.year)
print(date_.month)
print(date_.day)
print(date_.weekday())
print(date_.isoweekday())
print(date_.isocalendar())
print(date_.isoformat())

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%Y/%b/%d %H:%M.%f'))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

print(datetime.strptime("10/11/2025", '%d/%m/%Y'))

print(timedelta(days=1))
print(datetime.now() - timedelta(days=1, hours=1))

# start_time = time.time()
# print(start_time)
# time.sleep(1.2)
# end_time = time.time()
# print(end_time - start_time) # wait 1.2 second