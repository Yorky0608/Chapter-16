from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.cm as cm
import numpy as np

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
            title = row[header_row.index("NAME")]

    return dates, highs, title



def multi_weather_plots(files):
    if len(files) > 100:
        print("Too many files have been submitted! Try 100 or fewer.")
        return

    num_files = len(files)
    color_map = cm.get_cmap("viridis", num_files)
    colors = [color_map(i) for i in range(num_files)]

    # Plot the high and low temperatures.
    plt.style.use('default')
    fig, ax = plt.subplots()
    titles = "Temps:"

    for i, file in enumerate(files):
        dates, highs, title = weather_plot(file)

        ax.plot(dates, highs, color=colors[i], alpha=0.5, label=title)
        titles += f"\n{title}"

    plt.legend()

    # Format plot.
    ax.set_title(titles, fontsize=20)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()

multi_weather_plots(["weather_data/San_Francisco_weather.csv", "weather_data/sitka_weather_2021_simple.csv", "weather_data/death_valley_2021_simple.csv"])