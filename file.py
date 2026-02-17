import streamlit as st

st.title("Ma première application Streamlit")
st.write('Bonjour, créons une app ensemble !', 'Bienvenue sur la page de M. Le Maire')

#test avec le prof
nom = st.text_input("Quel est votre nom?")
if nom: 
    st.succes(f"Bonjour {nom} ! Bienvenue sur Streamlit") 
age = st.slider("Quel est votre âge ?", 0, 100, 25 )
st.write("vous avez", age, "ans")


if st.button("Cliquez ici"):
    st.write("Vous avez cliqué sur le bouton !")


st.balloons() #Ballon sur l'interface

st.snow()  #Fond neige

import pandas as pd
import pydeck as pdk
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Use Streamlit theme to pick map style
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)


