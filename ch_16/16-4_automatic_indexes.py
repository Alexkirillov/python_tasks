from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

path= Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)


for index, column_header in enumerate(header_row):
    print(index,column_header)
dates,highs,lows = [],[],[]
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

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates,highs,color="red", alpha=0.5)
ax.plot(dates,lows, color="blue",alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor="blue", alpha=0.1)
ax.plot(dates,highs, color = "red")
ax.plot(dates, lows, color= "blue")


title = (row[1])
ax.set_title(title,fontsize=20)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize = 16)
ax.tick_params(labelsize=16)

plt.show()