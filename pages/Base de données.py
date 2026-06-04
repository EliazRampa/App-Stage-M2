import datetime
from pathlib import Path
import branca
import folium
import geojson
import pandas
from folium.plugins import TreeLayerControl
import streamlit as st
from streamlit_folium import folium_static

### path, data and variable
dict_list = []
dict = {}
geo_data = Path("./pages/assets/database/test_coulee.geojson")
csv = Path("./pages/assets/database/test_database.csv")
excel = Path("./pages/assets/database/PdF-sample-data-base-2014-2024.xls")
bulk_excel = Path("./pages/assets/database/bulk_db.xls")
glass_excel = Path("./pages/assets/database/glass_db.xls")



### create map for database

with open(geo_data, 'r') as f:
    data = geojson.load(f)
#popup = folium.GeoJsonPopup(fields=["date"])
attr = 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
m = folium.Map(location=(-21.243706, 55.748791), zoom_start=13, zoom_control=False)

OSM = folium.TileLayer(tiles='OpenStreetMap')
OSM.add_to(m)
ESRI = folium.TileLayer(tiles=tiles, attr=attr, name='ESRI')
ESRI.add_to(m)
df = pandas.read_csv(csv, sep=';')

fg = folium.FeatureGroup('Coulées')
m.add_child(fg)
df['flow_id'].astype(float)
col = []
for i in range(1,14):
    col.append(i)

#folium.GeoJson(geo_data, name='Coulée', highlight_function=lambda feature: {'fillColor':'red'}, popup=popup, popup_keep_highlighted=True).add_to(m)
for feature in data["features"]:
    cle = feature['properties']['flow_id']
    data = df.loc[df['flow_id']==cle].values.flatten().tolist()
    sample = pandas.read_excel(excel, sheet_name=str(cle), engine="xlrd", skiprows=1, usecols=col)
    sample_table = sample.to_html(index= False, classes="table table-striped table-hover table-condensed table-responsive")
    bulk = pandas.read_excel(bulk_excel, sheet_name=str(cle), engine="xlrd", usecols=col)
    bulk_table = bulk.to_html(index= False, classes="table table-striped table-hover table-condensed table-responsive")
    glass = pandas.read_excel(glass_excel, sheet_name=str(cle), engine="xlrd", usecols=col)
    glass_table = glass.to_html(index= False, classes="table table-striped table-hover table-condensed table-responsive")

    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
    <h1> Données de l'éruption</h1>
    <h2> Données Sources </h2>
    Date de début: {data[1]} <br>
    Date de fin: {data[2]} <br>
    Durée: {data[3]} jours 
    Volumes de lave émis: {data[5]} Mm<sup>3</sup>
    <br>
    <br>
    TADR: {data[4]} m<sup>3</sup>/s <br>

    <h2> Échantillons </h2>
    Lame minces : <pre> {data[6]}  </pre> <br>
    
    Liste des échantillons:
    <pre> {sample_table} </pre>
    
    <h2> Paramètres Pétrochimiques</h2>
    Cristallinité: {data[7]} % <br>
    Porosité : {data[8]} %<br>
    Température de l'éruption: {data[9]} °C soit {data[10]} K <br> <br>
    Chimie sur roche total:
    <pre> {bulk_table} </pre>
    <br> 
    <br>
    Chimie du verre:
    <pre> {glass_table} </pre>
    <br>
    <h2> Modèle Numérique de Terrain (MNT)</h2>
    DEM utilisé: {data[11]}
    </body>
    </html>
    """

    iframe = branca.element.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=500)
    b = folium.GeoJson(feature ['geometry'], name=data[1], popup=popup, lazy=True)
    b.add_child(folium.Tooltip(data[1]))
    b.add_to(m)


    dict = {"label":f' {data[1]}', "layer":b}
    dict_list.append(dict)
    sorted_dict = sorted(dict_list, key=lambda d: datetime.datetime.strptime(d['label'].strip(), "%d/%m/%Y"))

ref_html = f'''
    <h2> Légendes  </h2>
    [X] : n° de la références <br>
    <span style="color:red;"> (P) </span> : obtenue sur des pyroclatses <br>
    <em style="color:red;"> REUXXXXXX-X </em> : Échantillon non analysé
    <br> <br>
    <h2> Références </h2>
    
'''

icon_path = "./pages/assets/database/icon_ref.png"
iframe_ref = branca.element.IFrame(html=ref_html, width=300, height=200)
ref_popup = folium.Popup(iframe_ref, max_width=300, sticky=True)
icon = folium.CustomIcon(icon_path, icon_size=(50, 50))
ref = folium.Marker(location=[-21.2177,55.68712], icon=icon, tooltip='Légende et Références', popup=ref_popup, draggable=True, name='Légendes et Références')
ref.add_to(m)

overlay_tree = {
    "label":'Overlay',
    "children" : [
        {"label":'Coulées',
         'collapsed': 'true',
        "children": sorted_dict},
        { "label": 'Légendes et Références', 'layer': ref}]
}

baseTree = {
    'label': 'Fonds de carte',
    'children': [
        {
            'label': 'World &#x1f5fa;',
            'children': [
                { 'label': 'ESRI', 'layer': ESRI },
                {'label': 'OpenStreetMap', 'layer': OSM}
            ]}]}

TreeLayerControl(overlay_tree=overlay_tree, base_tree= baseTree, opened_symbol='&#8863; &#x1f5c1;', closed_symbol='&#8862; &#x1f5c0;').add_to(m)

m.save('database_PdF_2014_2023.html')

### page
st.set_page_config(layout='wide')
st.title('Base de données')

st.data = folium_static(m,width = 4500, height=750)
