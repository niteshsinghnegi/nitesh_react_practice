import datetime


current_time = datetime.datetime.now()
hour = current_time.hour


if hour >= 5 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 21:
    print("Good Evening")
else:
    print("Good Night")
