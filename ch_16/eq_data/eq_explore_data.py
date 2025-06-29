from pathlib import Path
import json

import plotly.express as px
#read data as a string convert to a python object
path=Path("eq_data/eq_1hour_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
#examine alll earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags,lons,lats,eq_titles=[],[],[],[]
for eq_dict in all_eq_dicts:  
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])
print(mags[:10])
print(lons[:5])
print(lats[:5])
print(type(all_eq_data))
#task 16-7 complete
title = all_eq_data["metadata"]["title"]
print(title)
fig = px.scatter_geo(lat=lats,lon=lons,size=mags,title=title,color=mags,color_continuous_scale="aggrnyl",labels={"color":"magnitude"},projection="natural earth",hover_name=eq_titles,)
fig.show()

#create a more readable version of the data file
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data,indent = 4)
path.write_text(readable_contents)
