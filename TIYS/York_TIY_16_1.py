from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


dates, prcp = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    prcp.append(row[5])


plt.style.use('default')
fig, ax = plt.subplots()
ax.plot(dates, prcp, color='red', alpha=0.5)

# Format plot.
title = "Daily Rainfall, 2021\nSitka"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()