import folium
import pandas

map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")

VolcanoData = pandas.read_json("resources/VolcanoList.json")
PopulationData = open("resources/PopulationList.json", "r", encoding = "utf-8-sig").read()



VolcanoName = list(VolcanoData["name"])
VolcanoType = list(VolcanoData["type"])
VolcanoElev = list(VolcanoData["elevation"])
VolcanoLat = list(VolcanoData["lat"])
VolcanoLon = list(VolcanoData["lon"])

# PopulationData = pandas.read_json("resources/PopulationList.json")

# Volcones

fgv = folium.FeatureGroup(name = "Volcanoes")

html = """<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank"> <h3> %s:</h3> </a>
Type: %s <br>
Height: %s m
"""

def VolcanoColors(type):
    if type == "Stratovolcano":
        return "red"
    elif type == "Submarine":
        return "lightblue"
    else:
        return "green"

for name, type, elev, lat, lon in zip(VolcanoName, VolcanoType, VolcanoElev, VolcanoLat, VolcanoLon):
    iframe = folium.IFrame(html = html % (name + " volcano", name, type , elev), width = 200, height = 100)
    # fg.add_child(folium.Marker(location = [lat, lon], popup = f"Name: {name}, Type: {type} , Elevation: {elev}m", icon = folium.Icon(color = 'green')))
    # fg.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(iframe), icon = folium.Icon(color = VolcanoColors(type))))

    #  To add the popup as circle use the code below
    fgv.add_child(folium.CircleMarker(location = [lat, lon], radius= 10, popup = folium.Popup(iframe), color = VolcanoColors(type), fill = True, fill_color = VolcanoColors(type)))

# Adding the population data informations
fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = PopulationData, style_function = lambda x: 
                            {'fillColor':'green' if x['properties']['POP2005'] < 20000000 
                            else 'orange' if x['properties']['POP2005'] < 50000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

# Layer control fuvtion
map.add_child(folium.LayerControl())
map.save("IndianMap.html")
    


"""" Below is a function that i used to find out how many different 
    types of volcanoes are listed in the json file 

def testing():
    result = []                          
    for ty in VolcanoType:
            if any(ty in s for s in result):
                continue
            else:
                result.append(ty)
    
    print(result)


testing()

"""

