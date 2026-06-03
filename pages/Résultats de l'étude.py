import streamlit as st
from pathlib import Path
import pandas

#### chemin
downflowgo = Path("./pages/assets/results/downflowgo")
er = Path("./pages/assets/results/er")
mm = Path("./pages/assets/results/mueller mader")
mmc = Path("./pages/assets/results/mueller mader chenal")
liste = Path("./pages/assets/results/liste erup.csv")

#### Données
df = pandas.read_csv(liste, sep=";")

#### page
st.set_page_config(layout='wide')
st.title('Résultats de l\'étude')

st.header("Résultats globaux", divider=True)
grp_campus = Path('./pages/assets/results/globaux/table grp campus.png')
TAS = Path('./pages/assets/results/globaux/diagramme TAS.png')
table_downflowgo = Path('./pages/assets/results/globaux/table downflowgo.png')
stat = Path('./pages/assets/results/globaux/stat adaptation.png')
gamme_er = Path('./pages/assets/results/globaux/gamme er.png')
gamme_mm = Path('./pages/assets/results/globaux/gamme mm.png')
gamme_mmc = Path('./pages/assets/results/globaux/gamme mmc.png')

with st.container(border=True):
    st.subheader("Diagramme TAS", divider=True)
    st.image(TAS)

    st.subheader('Modélisation avec DOWNFLOWGO (Modèle A)', divider=True)
    st.write("Tableau de synthèses des modélisation")
    st.image(table_downflowgo)

    st.write('Répartition des paramètres modifiés pour les 13 éruptions nécessittant une adaptation')
    st.image(stat)

    st.subheader("Modélisation inverse avec PyFLOWGO", divider= True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Modèle B')
        st.image(gamme_er)
    with col2:
        st.write('Modèle C')
        st.image(gamme_mm)
    with col3:
        st.write("Modèle D")
        st.image(gamme_mmc)

st.header("Résultats par éruption", divider=True)
compa = st.checkbox("Comparaison")

if compa:
    colA, colB = st.columns(2)
    with colA:
        erup = st.selectbox("Sélectionner l'éruption à afficher", df['name'], key='colA')

        defaut= Path(f"{downflowgo}/{erup} défaut.png")
        adapt = Path(f"{downflowgo}/{erup} adapté.png")
        er_img = Path(f"{er}/{erup}.png")
        er_img_p1 = Path(f"{er}/{erup} P1.png")
        mm_img = Path(f"{mm}/{erup}.png")
        mm_img_p1 = Path(f"{mm}/{erup} P1.png")
        mmc_img = Path(f"{mmc}/{erup}.png")
        mmc_img_p1 = Path(f"{mmc}/{erup} P1.png")

        with st.expander(f'Résultats pour {erup}', expanded=True):
            st.subheader('Modèle A', divider=True)
            if adapt.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Paramètres par défaut')
                with col2:
                    st.write('Paramètres adapté')
            else:
                st.write('Paramètres par défaut')

            st.subheader('Modèle B', divider=True)
            if er_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write("Pulse 1")
                    st.image(er_img_p1)
                with col2:
                    st.write("Final")
                    st.image(er_img)
            else:
                st.write("Final")
                st.image(er_img)

            st.subheader('Modèle C', divider=True)
            if mm_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Pulse 1')
                    st.image(mm_img_p1)
                with col2:
                    st.write('Final')
                    st.image(mm_img)
            else:
                st.write('Final')
                st.image(mm_img)

            st.subheader('Modèle D', divider=True)
            if mmc_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Pulse 1')
                    st.image(mmc_img_p1)
                with col2:
                    st.write('Final')
                    st.image(mmc_img)
            else:
                st.write('Final')
                st.image(mmc_img)
    with colB:
        erup = st.selectbox("Sélectionner l'éruption à afficher", df['name'], key='colB')

        defaut= Path(f"{downflowgo}/{erup} défaut.png")
        adapt = Path(f"{downflowgo}/{erup} adapté.png")
        er_img = Path(f"{er}/{erup}.png")
        er_img_p1 = Path(f"{er}/{erup} P1.png")
        mm_img = Path(f"{mm}/{erup}.png")
        mm_img_p1 = Path(f"{mm}/{erup} P1.png")
        mmc_img = Path(f"{mmc}/{erup}.png")
        mmc_img_p1 = Path(f"{mmc}/{erup} P1.png")

        with st.expander(f'Résultats pour {erup}', expanded=True):
            st.subheader('Modèle A', divider=True)
            if adapt.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Paramètres par défaut')
                with col2:
                    st.write('Paramètres adapté')
            else:
                st.write("Paramètres par défaut")
                pass

            st.subheader('Modèle B', divider=True)
            if er_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write("Pulse 1")
                    st.image(er_img_p1)
                with col2:
                    st.write("Final")
                    st.image(er_img)
            else:
                st.write("Final")
                st.image(er_img)

            st.subheader('Modèle C', divider=True)
            if mm_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Pulse 1')
                    st.image(mm_img_p1)
                with col2:
                    st.write('Final')
                    st.image(mm_img)
            else:
                st.write('Final')
                st.image(mm_img)

            st.subheader('Modèle D', divider=True)
            if mmc_img_p1.exists():
                col1 , col2 = st.columns(2)
                with col1:
                    st.write('Pulse 1')
                    st.image(mmc_img_p1)
                with col2:
                    st.write('Final')
                    st.image(mmc_img)
            else:
                st.write('Final')
                st.image(mmc_img)

else:
    erup = st.selectbox("Sélectionner l'éruption à afficher", df['name'])

    defaut= Path(f"{downflowgo}/{erup} défaut.png")
    adapt = Path(f"{downflowgo}/{erup} adapté.png")
    er_img = Path(f"{er}/{erup}.png")
    er_img_p1 = Path(f"{er}/{erup} P1.png")
    mm_img = Path(f"{mm}/{erup}.png")
    mm_img_p1 = Path(f"{mm}/{erup} P1.png")
    mmc_img = Path(f"{mmc}/{erup}.png")
    mmc_img_p1 = Path(f"{mmc}/{erup} P1.png")

    with st.expander(f'Résultats pour {erup}', expanded=True):
        st.subheader('Modèle A', divider=True)
        if adapt.exists():
            col1 , col2 = st.columns(2)
            with col1:
                st.write('Paramètres par défaut')
            with col2:
                st.write('Paramètres adapté')
        else:
            st.write("Paramètres par défaut")


        st.subheader('Modèle B', divider=True)
        if er_img_p1.exists():
            col1 , col2 = st.columns(2)
            with col1:
                st.write("Pulse 1")
                st.image(er_img_p1)
            with col2:
                st.write("Final")
                st.image(er_img)
        else:
            st.write("Final")
            st.image(er_img)

        st.subheader('Modèle C', divider=True)
        if mm_img_p1.exists():
            col1 , col2 = st.columns(2)
            with col1:
                st.write('Pulse 1')
                st.image(mm_img_p1)
            with col2:
                st.write('Final')
                st.image(mm_img)
        else:
            st.write('Final')
            st.image(mm_img)

        st.subheader('Modèle D', divider=True)
        if mmc_img_p1.exists():
            col1 , col2 = st.columns(2)
            with col1:
                st.write('Pulse 1')
                st.image(mmc_img_p1)
            with col2:
                st.write('Final')
                st.image(mmc_img)
        else:
            st.write('Final')
            st.image(mmc_img)