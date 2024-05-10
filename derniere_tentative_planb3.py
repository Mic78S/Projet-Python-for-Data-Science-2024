import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

root = 20

list_url = ["https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html", "https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html?start=20"]

for i in range(1,10):
    root += 20
    url = f"https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html?start={root}" 
    list_url.append(url)

#print(list_url)

monsters_stats = []
monsters_values = []
monsters_names = []
climates = []
frequencies = []
hitdices = []

for url in range(1,2):
    response = requests.get(list_url[url])
    soup = BeautifulSoup(response.text, "html5lib")
        # peut-être qu'un time sleep de python time serait utile si je mets toutes les pages 
    content = soup.find("table")

    #print(type(content))
    
    x = content.text
    #print(x)

    # les blancs dans la table ne sont pas des div mais des td, inutile d'essayer de les corriger plus bas, il faut le faire sur le content
   
    for tr in content.tbody.find_all("tr"):
        for td in tr.find_all("td"):
            if td.text.strip() == "":
                monsters_values.append("None")
            else:
                for element in td.find_all("div", class_="valeur"): 
                    monsters_values.append(element.text.strip())        
    
    for element in content.find_all("div", class_="etiquette"):
        monsters_stats.append(element.text.strip())

    for element in content.find_all("span", class_="fc_item_title"):
        monsters_names.append(element.text.strip())

    climates = monsters_values[1::23]
    frequencies = monsters_values[2::23]
    hitdices = monsters_values[12::23]

    

#print(response)
#print(soup)
#print(soup1)
#print(content)
#print(type(content))
#print(monsters_values)
print(monsters_values[0])
print(len(monsters_values))
print(monsters_names)
print(len(monsters_names))
#print(monsters_stats)
#print(len(monsters_stats))
print(climates)
print(frequencies)
print(hitdices)


