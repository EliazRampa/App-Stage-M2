import json

import streamlit as st
from pathlib import Path
import json

models_url = Path("./pages/assets/json/modèle A.json")

with open(models_url, 'r') as f:
    models = json.load(f)

st.title("Modèle A, configuration par défaut DOWNFLOWGO")
st.json(models)