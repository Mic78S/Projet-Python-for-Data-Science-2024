import requests
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib

# les fichiers csv de la ville de bxl utilisent le ; comme séparateur



file_path = Path(__file__).parent

col_names = ["Catégorie", "Dénomination", "Adresse", "Code postal", "Localité", "Téléphone", "Courriel", "Site web", "Statut juridique", "Province", "Bassin de vie FWB", "BCE", "Reconnaissance FWB", "Catégorie de reconnaissance", "Géolocalisation"]

data = pd.read_csv(Path(file_path, "adresses-des-musees-reconnus-en-communaute-francaise.csv", sep=" ;", names=col_names, on_bad_lines="Skip"))["Dénomination", "Code postal", "Province"]

print(data)

df = pd.DataFrame({
    
})








