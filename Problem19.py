import datetime

count = 0
for i in range(1901, 2001):
    for k in range(1, 13):
        x = datetime.datetime(i, k, 1)
        if x.strftime("%A") == "Sunday":
            count += 1

print(count)
