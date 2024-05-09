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
values = []
names = []
climates = []
frequencies = []
hitdices = []

for url in range(1,2):
    response = requests.get(list_url[url])
    soup = BeautifulSoup(response.text, "html5lib")
    # peut-être qu'un time sleep de python time serait utile si je mets toutes les pages 
    content = soup.find("table")

    for element in content.find_all("div", class_="etiquette"):
        monsters_stats.append(element.text.strip())

    for element in content.find_all("span", class_="fc_item_title"):
        names.append(element.text.strip())

    for element in content.find_all("td"):
        values.append(element.text.strip())


#print(response)
#print(soup)
#print(content)
print(values)
print(len(values))
print(len(names))


# ça marche mais ça pose deux problèmes: les étiquettes et les valeurs sont collées et deviennent un seul indice de liste 
    # => td n'est probablement pas le bon truc, je dois garder seulement les valeurs, je pourrai définir les étiquettes en créant mon dataframe
                #les noms et les valeurs se suivent les unes après les autres pour former une seule très longue liste
    # => je ne sais pas si c'est possible, mais je devrais diviser la liste tous les 25 pas en un nombre indéfini d'autres listes









#for page in range(1,10):
 #   result = requests.get(url + str(page)), 
