import streamlit as st
from pathlib import Path
import json

models_url = Path("./pages/assets/json/modèle C.json")

with open(models_url, 'r') as f:
    models = json.load(f)

st.title("Modèle C, configuration avec effet des bulles et forme des cristaux (mp_mueller et mader)")
st.json(models)