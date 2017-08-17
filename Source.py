import folium
import pandas
m=folium.Map(location=[25.041807, 77.899597],zoom_start=5,tiles='Mapbox Bright')
np= pandas.read_csv("national park.txt")
vol=pandas.read_excel("volcanoes.xlsx",sheetname=0)
lat=list(np["Lat"])
lon=list(np["Lon"])
msg=list(np["Name"])
fg=folium.FeatureGroup(name="National Parks")
fgv=folium.FeatureGroup(name="Volcanoes")
pop=folium.FeatureGroup(name="Population")
for lt,ln,mg in zip(lat,lon,msg):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=mg,radius="5",fill_color='green'))
lat=list(vol["LAT"])
lon=list(vol["LON"])
msg=list(vol["NAME"])
for lt,ln,mg in zip(lat,lon,msg):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=mg,radius="5",fill_color='red'))
pop.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig"),
style_function=lambda x:{"fillColor":"blue" if x['properties']['POP2005']<=1000000
else 'yellow' if x['properties']['POP2005']<=10000000
else 'green' if x['properties']['POP2005']<=100000000
else 'orange' if x['properties']['POP2005']<80000000
else 'red'}))
m.add_child(pop)
m.add_child(fg)
m.add_child(fgv)
m.add_child(folium.LayerControl())
m.save("final.html")