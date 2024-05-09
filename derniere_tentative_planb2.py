import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = "https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux/8560-aarakocra.html"

result = requests.get(url)
content = result.text
#print(content)
soup1 = BeautifulSoup(content, "lxml")

title = soup1.find("h2", class_="contentheading flexicontent")

box = soup1.find("table")
#print(box)

pages = soup1.find_all("a", class_="fcpagenav-next btn", href=True)
#print(pages)

for link in pages:
    link("href")

print(link)

# première page de la liste du bestiaire
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




