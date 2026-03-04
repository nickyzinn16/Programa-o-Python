import datetime

now = datetime.datetime.now()

# birthday = datetime.date(1990, 8, 18)
# print(f"{birthday}")

year = now.year;
month = now.mounth;
day = now.day;
hour = now.hour;
minute = now.minute;
second = now.second;

print(f"{now.strftime('%d/%m/%Y')}")

datetime.datetime.strptime(string, "%d/%m/%Y")

# %d
# %m
# %Y
# %H
# %M
# %S
