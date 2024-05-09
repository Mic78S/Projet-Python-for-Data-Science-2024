import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = "https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html"

response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text, "html5lib")

#code inutile : data_utiles = soup.find_all("td")

#print(data_utiles)
print(soup)

valeurs_classes = []
valeurs_etiquettes = []

for element in soup.find_all("div", class_="valeur"):
    valeurs_classes.append(element.text.strip())

print(valeurs_classes)
print(len(valeurs_classes))
#print(valeurs_classes[21])

frequency = valeurs_classes[1:350:21]
climate = valeurs_classes[0:350:21]
hitdices = valeurs_classes[11:350:21]

#print(frequency)
#print(len(frequency))
#print(climate)
#print(len(climate))
#print(len(hitdices))
#print(hitdices)

for element in soup.find_all("div", class_="etiquette"):
    valeurs_etiquettes.append(element.text.strip())
#print(valeurs_etiquettes)
#print(len(valeurs_etiquettes))

#code inutile : etiquettes = valeurs_etiquettes[0:20]
#print(etiquettes)

etiquettes_finales = [valeurs_etiquettes[0], valeurs_etiquettes[1], valeurs_etiquettes[11]]
#print(etiquettes_finales)

df = pd.DataFrame({etiquettes_finales[0]:[climate[0:17]], etiquettes_finales[1]:[frequency], etiquettes_finales[2]:[hitdices]})

df = pd.DataFrame({
   "Climate/Terrain" : climate,
   "Frequency" : frequency,
   "Hit Dices" : hitdices
})

print(df)

