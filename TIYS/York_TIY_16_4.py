from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def weather_plot(file_name):
    path = Path(file_name)
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # # Extract dates and high temperatures.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            tmax_index = header_row.index("TMAX")
            high = int(row[tmax_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)

    # Plot the high and low temperatures.
    plt.style.use('default')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='blue', alpha=0.5)

    # Format plot.
    title = f"{row[header_row.index("NAME")]}"
    ax.set_title(title, fontsize=20)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()

weather_plot("weather_data/sitka_weather_2021_simple.csv")