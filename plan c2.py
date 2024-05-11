import requests
import json
import pandas as pd
import geopandas as gpd
import geoplot
import geoplot.crs as gcrs
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
from shapely.geometry import Point, Polygon
import geojson

# les fichiers csv de la ville de bxl utilisent le ; comme séparateur



url = "https://overpass-api.de/api/map?bbox=4.3325,50.8308,4.3723,50.8589"

response = requests.get(url)
print(response)
data_map = response.content
#print(data_map)



file_path = Path(__file__).parent

with open(Path(file_path, "quartiers.geojson")) as f:
    gj = geojson.load(f)
features = gj["features"][0]

#print(gj)
#print(features)

geo_df = gpd.read_file(Path(file_path, "quartiers.geojson"))
print(geo_df.head())

print(geo_df.geom_type)

#fig, ax = plt.subplots(figsize = (10,10))
#geoplot.pointplot(geo_df)


#print(geo_df)

geoplot.polyplot(
    geo_df,
    projection=gcrs.AlbersEqualArea(),
    edgecolor="darkgrey",
    facecolor="lightgrey",
    linewidth= .3,
    figsize=(12, 8)
)




df = pd.DataFrame({
    "Quartier" : ["Laeken", "Haren", "Nord", "Nord-Est", "Neder-Over-Heembeek/Mutsaard", "Pentagone", "Louise"],
    "Latitude" : [50.886866140, 50.890099036, 50.873347688, 50.843768813, 50.8989495829, 50.845826458, 50.809945412],
    "Longitude" : [4.349189494597455, 4.416320599821119, 4.367020244449153, 4.381471777029443, 4.38484277215643, 4.352357840093162, 4.378475495683379]
})

df["Coordinates"] = list(zip(df.Longitude, df.Latitude))
#df.head()
#print(df.head())

df["Coordinates"] = df["Coordinates"].apply(Point)
df.head()
print(df.head())

gdf = gpd.GeoDataFrame(df, geometry="Coordinates")
gdf.head()
(print(gdf.head()))
print(type(gdf))
print(gdf.geometry.name)


# En résumé, j'ai commencé par essayer de visualiser un fichier geojson, de là je suis placé à spotter une map, puis à créer une map à partir de l'api d'openstreetsmap... 
# 3h de recherche pour me rendre compte que la colonne geometry est déjà dans le fichier geojson