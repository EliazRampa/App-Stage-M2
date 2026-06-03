import streamlit as st
from pathlib import Path
import json

models_url = Path("./pages/assets/json/modèle D.json")

with open(models_url, 'r') as f:
    models = json.load(f)

st.title("modèle D, configuration avec effet des bulles et forme des cristaux (mp_mueller et mader) avec largeur du chenal de 2 mètre")
st.json(models)