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

for url in range(1,10):
    response = requests.get(list_url[url])
    soup = BeautifulSoup(response.text, "html5lib")
        # peut-être qu'un time sleep de python time serait utile si je mets toutes les pages 
    content = soup.find("table")

    print(type(content))
    
    x = content.text
    #print(x)

    

    for element in content.find_all("div", class_="etiquette"):
        monsters_stats.append(element.text.strip())

    for element in content.find_all("span", class_="fc_item_title"):
        monsters_names.append(element.text.strip())

    for element in content.find_all("div", class_="valeur"):
        monsters_values.append(element.text.strip())

#print(response)
#print(soup)
#print(soup1)
print(content)
#print(type(content))
#print(monsters_values)
print(len(monsters_values))
#print(monsters_names)
print(len(monsters_names))
#print(monsters_stats)
print(len(monsters_stats))


# ça marche mais il reste deux problèmes:
    # le compte ne tombe pas juste : il y a clairement des stats en trop ou trop peu (trop peu : 24 en théorie, entre 19 et 20 en moyenne)
                #les noms et les valeurs se suivent les unes après les autres pour former une seule très longue liste
    # => je ne sais pas si c'est possible, mais je devrais diviser la liste tous les 25 pas en un nombre indéfini d'autres listes









#for page in range(1,10):
 #   result = requests.get(url + str(page)), 
