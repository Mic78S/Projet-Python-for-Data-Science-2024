import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = 20

list_url = ["https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html", "https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html?start=20"]

for i in range(1,10):
    root += 20
    url = f"https://www.donjondudragon.fr/drs/ad-d2/bestiaire-monstrueux.html?start={root}" 
    list_url.append(url)

#print(list_url)
#le site comprend 67 pages... mais ça marche, il faut juste lui laisser un peu de temps

monsters_stats = []
monsters_values = []
monsters_names = []

climates = []
frequencies = []
hitdices = []

organisation = []
cycle_actif = []
regime = []
intelligence = []
treasure = []
alignement = []
nombre = []
ac = []
move = []
taco = []
nbattacks = []
degats = []
special_attacks = []
special_defenses = []
magical_resistance = []
size = []
moral = []
xp = []

for url in range(1,10):
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
    
    df = pd.DataFrame({
        "Nom": monsters_names,
        "Climate/Terrain" : climates,
        "Frequency" : frequencies,
        "Hit Dices" : hitdices
    })

    # maintenant j'ai mon dataframe, qu'est-ce que j'en fais ? Compter le nombre d'occurences de chaque valeur par liste et transformer ça en graphique ?

#print(response)
#print(soup)
#print(soup1)
#print(content)
#print(type(content))
print(monsters_values)
#print(monsters_values[0])
#print(len(monsters_values))
#print(monsters_names)
#print(len(monsters_names))
#print(monsters_stats)
#print(len(monsters_stats))
#print(climates)
#print(frequencies)
#print(hitdices)
#print(df)


    #organisation = monsters_values[3::23]
    #cycle_actif = monsters_values[4::23]
    #regime = monsters_values[5::23]
    #intelligence = monsters_values[6::23]
    #treasure = monsters_values[7::23]
    #alignement = monsters_values[8::23]
    #nombre = monsters_values[9::23]
    #ac = monsters_values[10::23]
    #move = monsters_values[11::23]
    #taco = monsters_values[13::23]
    #nbattacks = monsters_values[14::23]
    #degats = monsters_values[15::23]
    #special_attacks = monsters_values[16::23]
    #special_defenses = monsters_values[17::23]
    #magical_resistance = monsters_values[18::23]
    #size = monsters_values[19::23]
    #moral = monsters_values[20::23]
    #xp = monsters_values[21::23]

