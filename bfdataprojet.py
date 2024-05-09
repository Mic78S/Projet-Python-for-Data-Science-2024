import pandas as pd
from pathlib import Path
import csv


file_path = Path(__file__).parent

print(file_path.parent)

#df1 = pd.read_csv(file_path, "ares-inscriptions-dans-l-enseignement-superieur.csv")
df2 = pd.read_excel(file_path, "localunit_val_fr_2022_4_repartition_des_postes_de_travail_par_lieu_de_travail", sheet_name="tableau 8-17")

#print(df2)