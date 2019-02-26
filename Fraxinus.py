# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:41:00 2019

@author: Rodrigo
"""

import pandas as pd 
import folium

datos=pd.read_csv('Fraxinus.csv',sep ='\t')
datos2=pd.read_csv('Fraxinus2.csv',sep ='\t')

puntos=datos.dropna(subset=['decimalLatitude'])
puntos=datos.dropna(subset=['decimalLongitude'])
puntos2=datos2.dropna(subset=['decimalLatitude'])
puntos2=datos2.dropna(subset=['decimalLongitude'])

mapa= folium.Map(
    location=[40.4640, 1.0036],
    zoom_start=6,
    tiles='Stamen Terrain'
)
tooltip = 'Click me!'

    
for indice, ocurrencia in puntos.iterrows():
    latitud = ocurrencia['decimalLatitude']
    longitud = ocurrencia['decimalLongitude']

    if not pd.isnull(latitud):
        marca1=folium.Marker(
                location=[latitud, longitud],
                popup='Fraxinus_excelsior',
                icon=folium.Icon(color='darkgreen', icon='leaf')
                ).add_to(mapa)

            
for indice, ocurrencia2 in puntos2.iterrows():
    latitud2 = ocurrencia2['decimalLatitude']
    longitud2 = ocurrencia2['decimalLongitude']           


    if not pd.isnull(latitud):
        marca2= folium.Marker(
                location=[latitud2, longitud2],
                popup='Fraxinus_ornus',
                icon=folium.Icon(color='yellow', icon='leaf')
                ).add_to(mapa)

mapa.save('fraxinus.html')
