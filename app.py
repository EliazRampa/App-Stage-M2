import streamlit as st
from pathlib import Path

st.set_page_config(layout='wide')
st.title('Présentation')

st.header('Contexte', divider=True)
st.write("Ceci est une application local réalisée dans le cadre de mon stage de deuxième année de master en science de la Terre, parcours Magma et Volcans, sur le sujet :")
st.subheader('Rétrospective des modélisations thermo-rhéologique des coulées de lave au Piton de la Fournaise')
st.write("Cette application regroupe de nombreux éléments: la base de données compilé, configurations de PyFLOWGO utilisées, ainsi que l'ensemble des figures réalisées au cours de mon stage")

st.header("Navigation", divider = True)
st.write('''
Pour accéder naviguer à travers l'application, il suffit de cliqué sur la page à laquelle vous souhaitez accédez dans le panneau latéral.
\n <––––––––– 
\n le thème de la page peut être modifié dans la section configuration, en haut à droite de chaque page représenté par 3 point verticaux.
\nJe recommande d'utiliser le thème clair pour la lisibilité de certains tableaux.
''')

st.header("Base de données", divider=True)
st.write('''
La base de données compilé pour ce stage est une carte interactive:

Les contours des coulée peuvent être cliqué pour ouvrir une popup contenant l'ensemble des informations compillées.

Les contours peuvent être désactivées ou réactivées au besoin dans le gestionnaire de couche en haut à droite de la carte.

L'icône noir avec un livre ouvre une popup avec la légende et les référence (source) des informations afficher pour chaque éruptions.
L'icône est déplaçable (cliqué-glissé) permettant un affichage à coté de la popup contenant les informations.
''')

st.header('Modèles', divider=True)
st.write('''
Les 4 pages intitulées Modèle A, B, C et D sont les fichier .json servant de configurations au packages PyFLOWGO qui ont été utilisé au cours de cette étude.
''')

st.header("Résultats", divider=True)
st.write("""
La page "Résultats de l'étude" regroupe les différentes figures réalisées au cours de ce projet.

Elles sont regroupées en trois catégories:
1) Les résultats globaux, qui regroupe l'ensemble des figures concernant la base de données, le cycle éruptif étudié ou qui couvrent plusieurs éruptions 

2) Les résultats par éruptions, qui réunit les résultats des différentes éruptions.
(Vous selectionnez l'éruption de votre choix dans la liste et les figures s'affiche. Il est possible de comparer les résultats de 2 éruption en cochant la case "comparaison"

3) Les annexes, qui sont les figures présentez en annexe du rapport réalisé lors de ce projet.
""")

st.header("Droit d'Auteur", divider=True)
st.write("Cette application à été créer sans utilisation de l'intelligence artificiel par Eliaz Rampa")