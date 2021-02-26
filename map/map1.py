import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data['LAT'])
lon = list(data['LON'])
elev =list(data["ELEV"])

def calc_elv(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09],zooom_start=6,tiles="Stamen Terrain")

fgv= folium.FeatureGroup(name="Volcanoes")
   
for lt,ln,el in zip(lat,lon,elev):
    map.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el) +" m",icon=folium.Icon(calc_elv(el)),radius=6, fill_color=calc_elv(el),color='grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005']<1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")