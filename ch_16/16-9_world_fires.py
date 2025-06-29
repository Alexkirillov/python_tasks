from pathlib import Path
import json

import plotly.express as px
#read data as a string convert to a python object
path=Path("ch_16/eq_data/world_fire_data.json")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
#examine alll earthquakes in the dataset

lats,lons,brights=[],[],[]
for eq_dict in all_eq_data:  
    lats.append(float(eq_dict["latitude"]))
    lons.append(float(eq_dict["longitude"]))
    brights.append(float(eq_dict["bright_t31"]))
#task 16-7 complete
title = "all world fires in the last 7 days"
print(title)
fig = px.scatter_geo(lat=lats,lon=lons,size=brights,title=title,color=brights,color_continuous_scale="viridis",labels={"color":"Magnitude"},projection="natural earth",)
fig.show()
"""
#create a more readable version of the data file
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data,indent = 4)
path.write_text(readable_contents)"""
