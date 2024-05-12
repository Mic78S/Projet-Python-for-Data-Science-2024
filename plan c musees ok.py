import requests
import json
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib

root = 100

liste_musees = []


api_musees = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise/records?limit=100"

response_musees = requests.get(api_musees)
#print(response_musees)
data_musees = json.loads(response_musees.text)
#print(data_musees)

results_api_musees = data_musees["results"]
#print(results_api_musees)
print(len(results_api_musees))

# une liste de 73 dictionnaires, ça parait correct