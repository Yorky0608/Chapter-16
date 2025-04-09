from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/recent_eq_30d.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags, lons, lats, eq_titles = [], [], [], []
[mags.append(eq_dict['properties']['mag']) for eq_dict in all_eq_dicts]
[lons.append(eq_dict['geometry']['coordinates'][0]) for eq_dict in all_eq_dicts]
[lats.append(eq_dict['geometry']['coordinates'][1]) for eq_dict in all_eq_dicts]
[eq_titles.append(eq_dict['properties']['title']) for eq_dict in all_eq_dicts]

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles,
)
fig.show()