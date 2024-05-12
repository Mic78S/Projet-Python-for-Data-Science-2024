import requests
import json
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib

root = 20

liste_musees = []

#api_musees = requests.get()

api_musees = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise/records?limit={root}"

while root <= 100:
    data = requests.get("https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise/records?limit={root}")
    liste_musees = liste_musees + list(data.json())
    root += 20




#while True:
#    data = requests.get("https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise/records?limit={root}")
 #   result = json.loads(data.text)
 #   liste_musees.append(result) 
  #  if root == 100:
  #      break
  #  else:
  #      root += 20

print(liste_musees)

#result = json.loads(api_musees.text)


#print(result)print(type(result))







