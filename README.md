# Projet-Python-for-Data-Science-2024

Projet de fin de formation


Le projet de départ était de travailler sur des indicateurs socio-économiques appliqués au secteur de l'enseignement.
    Ces indicateurs sont présentés sous forme de graphiques sur le portail de la Fédération Wallonie-Bruxelles.
    Cependant, les données ayant permis de générer ces indicateurs sont disponibles uniquement sur demande auprès du Bureau des Statistiques de la Fédération Wallonie-Bruxelles. 
    Un email a été envoyé au Bureau des Statistiques de la FWB le 06 mai.
    Pas (encore) de réponse le matin du 07 mai.
    Les sites suivants ont également été vérifiés, au cas où ils contenaient les dites données : 
        data dov
        Administration générale de l'enseignement (enseignement.be)
        Open Data Wallonie-Bruxelles (odwb.be)
        datastore.brussels
Le projet actuel part des données publiées par l'Ares concernant le nombre d'inscriptions dans l'enseignement supérieur par localisation, croisées avec les données publiées
par l'ONSS (via Data gov) concernant les Statistiques emploi classées par lieu de travail. 
    La question posée devient alors y a-t-il une corrélation entre le nombre d'emplois occupés (postes de travail occupés) dans une province (ou un arrondissement administratif) et le nombre d'inscriptions dans l'enseignement supérieur (hors universitaire) par province ou arrondissement administratif. 
    Pour rendre ces données un peu plus significatives, il faudrait que j'obtienne : 
        1) Les réussites et pas les inscriptions
        2) Les universités
    1) => J'ai trouvé des données concernant les diplômés de l'enseignement supérieur (universités et le reste) en %, par commune. 
            statbel.gov
            https://statbel.fgov.be/fr/themes/datalab/datalab-census-enseignement
            => Il faudra rassembler ces données par province ou arrondissement administratif.

Les données liées à l'enseignement ne sont manifestement pas accessibles ou mal collectées.

Plan b : scraping du bestiaire du site donjondudragon

Ok, ça marche, mais c'est assez peu analysable. Je vais peut-être essayer de trouver quelque chose d'un peu plus professionnalisant

Plan c : l'accès et la place de la culture dans la ville de Bruxelles

Est-ce que chacun des sept quartiers qui composent la ville de Bruxelles est égal du point de vue de l'accès à la culture ?

Critères retenus pour définir la culture : 
- musées
- cinémas
- bibliothèques
- lieux culturels
on laisse tomber les théâtres et le parcours bd

Critères retenus pour la culture dans l'espace public: 
- street art ?
- patrimoine artistique de voiries ?

Critères retenus pour définir l'accès :
- arrêts stib
- parkings publics
- gares sncb
- parking bus scolaires
- distributeurs bancaires ?

problème : comment localiser par quartier ?

commençons par un truc simple : les musées par rapport aux arrêts stib + gares sncb / quartiers de bxl


