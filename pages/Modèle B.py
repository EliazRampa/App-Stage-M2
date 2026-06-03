import streamlit as st
from pathlib import Path
import json

models_url = Path("./pages/assets/json/modèle B.json")

with open(models_url, 'r') as f:
    models = json.load(f)

st.title("Modèle B, configuration Einstein-Rosco adapté")
st.json(models)