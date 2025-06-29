from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

path= Path("weather_data/death_valley_2021_simple.csv")
path2=Path("weather_data/san_francisco_2021_full.csv")
lines = path.read_text(encoding="utf-8").splitlines()
lines2 = path2.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

reader2 = csv.reader(lines2)
header_row2 = next(reader2)


for index, column_header in enumerate(header_row):
    print(index,column_header)

for index2, column_header2 in enumerate(header_row2):
    print(index2,column_header2)
dates,highs,lows = [],[],[]
dates2,highs2,lows2 = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    print(current_date)
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

for row2 in reader2:
    current_date2 = datetime.strptime(row2[5], "%Y-%m-%d")
    print(current_date2)
    try:
        high2 = int(row2[6])
        low2 = int(row2[7])
    except ValueError:
        print(f"missing data for {current_date2}")
    else:
        dates.append(current_date2)
        highs.append(high2)
        lows.append(low2)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates,highs,color="red", alpha=0.5)
ax.plot(dates,lows, color="blue",alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor="blue", alpha=0.1)
ax.plot(dates,highs, color = "red")
ax.plot(dates, lows, color= "blue")

plt.style.use("seaborn-v0_8")
#fig, ax = plt.subplots()
ax.plot(dates2,highs2,color="orange", alpha=0.5)
ax.plot(dates2,lows2, color="green",alpha=0.5)
ax.fill_between(dates2,highs2,lows2,facecolor="green", alpha=0.1)
ax.plot(dates2,highs2, color = "orange")
ax.plot(dates2, lows2, color= "green")

title = ("Daily high and low temperatures, 2021\nDeath Valley, CA")
ax.set_title(title,fontsize=20)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize = 16)
ax.tick_params(labelsize=16)

title2 = ("Daily high and low temperatures, 2021\nSan francisco and death valley")
ax.set_title(title2,fontsize=20)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize = 16)
ax.tick_params(labelsize=16)

plt.show()
