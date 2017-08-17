import folium
import pandas
m=folium.Map(location=[25.041807, 77.899597],zoom_start=5,tiles='Mapbox Bright')
np= pandas.read_csv("national park.txt")
vol=pandas.read_excel("volcanoes.xlsx",sheetname=0)
lat=np["Lat"]
lon=np["Lon"]
msg=np["Name"]
fg=folium.FeatureGroup(name="National Parks")
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,mg in zip(lat,lon,msg):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=mg,radius="5",fill_color='green'))
lat=vol["LAT"]
lon=vol["LON"]
msg=vol["NAME"]
for lt,ln,mg in zip(lat,lon,msg):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=mg,radius="5",fill_color='red'))
m.add_child(fg)
m.add_child(fgv)
m.save("map1.html")