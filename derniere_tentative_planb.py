import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

root = "https://www.donjondudragon.fr/"

website = f"{root}/drs/ad-d2/bestiaire-monstrueux.html"

response = requests.get(website)
#print(response)

soup = BeautifulSoup(response.text, "html5lib")
#print(soup)

valeurs_classes = []
valeurs_etiquettes = []
explorationdubloc = []

box = soup.find("a", href=True)

for link in box.find_all("a", href=True):
    link("href")
    print(link)

links = [link["href"] for link in box.find_all("a", href=True)]
print(links)

for element in soup.find_all("td"):
    valeurs_classes.append(element.text.strip())
#print(valeurs_classes)

for element in soup.find_all("td"):
    explorationdubloc.append(element)

for element in soup.find_all("div", class_="etiquette"):
    valeurs_etiquettes.append(element.text.strip())

etiquettes_finales = [valeurs_etiquettes[0], valeurs_etiquettes[1], valeurs_etiquettes[11]]




