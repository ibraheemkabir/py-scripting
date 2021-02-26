import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data['LAT'])
lon = list(data['LON'])


map = folium.Map(location=[38.58,-99.09],zooom_start=6,tiles="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")

for coordinates in [[38.2,-99.1],[37.5,-97.1]]:
    map.add_child(folium.Marker(location=coordinates,popup="Hi I'm a Merker",icon=folium.Icon(color='green')))
   
for lt,ln in zip(lat,lon):
    map.add_child(folium.Marker(location=[lt,ln],popup="Hi I'm a Merker",icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")