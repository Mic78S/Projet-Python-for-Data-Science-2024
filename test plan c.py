import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import csv

file_path = Path(__file__).parent
noms_communes = Path(file_path, "noms_de_communes_belges.csv")
codes_postaux = Path(file_path, "codes_postaux_belges.csv")
communes_et_codespostaux = Path(file_path, "codes_postaux_et_localites_belges.csv")

data_codes_postaux_et_codespostaux = pd.read_csv(communes_et_codespostaux)
#print(data_codes_postaux_et_codespostaux)
#print(type(data_codes_postaux_et_codespostaux))

data_communes = pd.read_csv(noms_communes)
liste_communes = data_communes["Localite"].tolist()
#print(liste_communes)

data_codes_postaux = pd.read_csv(codes_postaux)
liste_codespostaux = data_codes_postaux["Code"].tolist()
#print(liste_codespostaux)

list_url = ["https://statbel.fgov.be/fr/commune/bruxelles#dashboard6"]
response = requests.get(list_url)
print(response)

root = liste_communes[0]
revenus_fiscaux_communes = []

for i in liste_communes:
    root = i
    url = f"https://statbel.fgov.be/fr/commune/{root}#dashboard6"
    list_url.append(url)

    #for url in range(1,10):
   #     response = requests.get(list_url)
    #    soup = BeautifulSoup(response.text, "html5lib")
        # peut-être qu'un time sleep de python time serait utile si je mets toutes les pages 
        #content = soup.find("span", class_="master_number")

       # for element in soup.find_all("span", class_="master_number"):
        #    revenus_fiscaux_communes.append(element.text.strip())

    #print(type(content))

#print(list_url)
print(revenus_fiscaux_communes)
    
#for i in liste_communes:
 #   vroot = liste_communes[0]
  #  url = f"https://statbel.fgov.be/fr/{root}/bruxelles#dashboard6" 
   # list_url.append(url)

#print(list_url)