from pathlib import Path
import csv
import matplotlib.pyplot as plt
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


brightnesses, lons, lats = [], [], []
for row in reader:
    brightnesses.append(float(row[2]))
    lons.append(float(row[1]))
    lats.append(float(row[0]))

title = 'World Fires'
fig = px.scatter_geo(lat=lats, lon=lons, size=brightnesses, title=title,
    color=brightnesses,
    color_continuous_scale='Viridis',
    labels={'color':'Brightness'},
    projection='natural earth',
)
fig.show()