import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# tentative 2 : récupérer les différentes pages de recherche du site

url = "https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html?start={}"
counter = 0

valeurs_classes = []
valeurs_etiquettes = []


while True:
    url += str(counter)
    webpage = requests.get (url)
    
    if webpage.status_code != 200:
        print("ça n'a pas marché")
        break
        

    soup = BeautifulSoup(webpage.text, "html5lib")

    for element in soup.find_all("div", class_="valeur"):
        valeurs_classes.append(element.text.strip())


frequency = valeurs_classes[1::21]
climate = valeurs_classes[0::21]
hitdices = valeurs_classes[11::21]

print(frequency)



