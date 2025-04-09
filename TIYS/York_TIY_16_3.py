from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Extract dates and high temperatures.
sitka_dates, sitka_highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    sitka_dates.append(current_date)
    sitka_highs.append(high)


path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Extract dates and high temperatures.
dv_dates, dv_highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dv_dates.append(current_date)
        dv_highs.append(high)


path = Path('weather_data/San_Francisco_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Extract dates and high temperatures.
sf_dates, sf_highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        sf_dates.append(current_date)
        sf_highs.append(high)


# Plot the high and low temperatures.
plt.style.use('default')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, color='red', alpha=0.5, label="Sitka")
ax.plot(dv_dates, dv_highs, color='blue', alpha=0.5, label="Death Valley")
ax.plot(sf_dates, sf_highs, color='green', alpha=0.5, label="San Francisco")

plt.legend()

# Format plot.
title = "Daily Temp Comparison Between\nSitka, Death Valley and San Francisco"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()