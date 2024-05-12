import requests
import json
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
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


url_api = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise"
offset = 100

api_musees = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/adresses-des-musees-reconnus-en-communaute-francaise/records?select=denomination%2C%20code_postal%2C%20localite%2C%20statut_juridique%2C%20province&limit=100"
api_spectacles = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-concert-et-theatres-en-wallonie-et-a-bruxelles/records?select=salle%2C%20code_postal%2C%20ville%2C%20categorie%2C%20jauge_maximale%2C%20province&limit=100"
api_spectacles2 = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-concert-et-theatres-en-wallonie-et-a-bruxelles/records?select=salle%2C%20code_postal%2C%20ville%2C%20categorie%2C%20jauge_maximale%2C%20province&limit=100&offset=101"
api_spectacles3 = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-concert-et-theatres-en-wallonie-et-a-bruxelles/records?select=salle%2C%20code_postal%2C%20ville%2C%20categorie%2C%20jauge_maximale%2C%20province&limit=100&offset=201"
api_cinema = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-projections-cinema/records?select=denomination_du_lieu%2C%20ville%2C%20categorie%2C%20province&limit=100"
api_cinema2 = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-projections-cinema/records?select=denomination_du_lieu%2C%20ville%2C%20categorie%2C%20province&limit=100&offset=101"
#api_bibliotheques = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/les-bibliotheques-publiques-en-federation-wallonie-bruxelles/records?select=denomination%2C%20code_postal%2C%20localite%2C%20statut_juridique%2C%20province&limit=100"
#api_cculturels = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/centre-culturels-en-communaute-francaise/records?select=denomination%2C%20code_postal%2C%20localite%2C%20statut_juridique%2C%20province&limit=100"

def api_culture(api_culture):
    response_api_culture = requests.get(api_culture)
    data_culture = json.loads(response_api_culture.text)
    results_api_culture = data_culture["results"]
    return results_api_culture

liste_musees = api_culture(api_musees)
# keys : denomination, code_postal, localite, statut_juridique, province

liste_spectacles = api_culture(api_spectacles) + api_culture(api_spectacles2) + api_culture(api_spectacles3)
# keys : salle, code_postal, ville, categorie, jauge_maximale, province
# liste_spectacles rassemble les salles de concert et les salles de théâtre, toutes deux incluses dans la même api par la fédé

liste_cinema = api_culture(api_cinema) + api_culture(api_cinema2)
# keys : denomination_du_lieu, ville, categorie, province
# attention! les salles du cinéma n'ont pas, pour une raison inconnue, de code postal, uniquement les noms propres des localités 
#   => trouver la liste des localités en belgique associées aux codes postaux

#liste_bib = api_culture(api_bibliotheques)
# keys : denomination, code_postal, localite, statut_juridique, province

#liste_centresculturels = api_culture(api_cculturels)
# keys : denomination, code_postal, localite, statut_juridique, province
# remarque : je n'ai pas conservé le champs "enjeux", ce qui aurait pu être intéressant. Mais la place des centres culturels dans la démarche reste peut-être à part. A supprimer ?

#print(liste_musees)
print(liste_spectacles)
#print(liste_cinema)
#print(liste_bib)
#print(liste_centresculturels)

print(len(liste_musees))
print(len(liste_spectacles))
print(len(liste_cinema))
#print(len(liste_bib))
#print(len(liste_centresculturels))



#response_musees = requests.get(api_musees)
#print(response_musees)
#data_musees = json.loads(response_musees.text)
#print(data_musees)

#results_api_musees = data_musees["results"]
#print(results_api_musees)
#print(len(results_api_musees))



#test = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/salles-de-projections-cinema/records?select=denomination_du_lieu%2C%20ville%2C%20categorie%2C%20province&limit=100&offset=101"

#response_test = requests.get(test)
#print(response_test)
#data_test = json.loads(response_test.text)
#print(data_test)

#suite_liste_cinema = api_culture(test)
#print(len(suite_liste_cinema))