# Import
import os
from pathlib import Path
from shapely.geometry import Point
import numpy as np
import pandas as pd 
import geopandas as gpd
import folium
from branca.colormap import LinearColormap
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

# Config
st.set_page_config(
    page_title='NYC 2022 Median Household Income Dashboard',
    page_icon='🏘️',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load
MedInc22_AMI22_BG22_geo = gpd.read_file("./data/MedInc22_AMI22_BG22_geo.geojson")
NTA20 = gpd.read_file("./data/NTA20.geojson")

# Write 
st.write("# NYC 2022 Median Household Income Dashboard")

st.markdown(
    """
    Below is an interactive map tool organizing 2022 median household income data by its 2022 AMI (3 family household) income range across NYC 2022 Census Block Groups. 

    Click the sidebar on the left to display the targeted income of affordable housing across block groups. 

    Sources: B19013 2022 ACS 5-Year Estimate, ANHD, Census Bureau, NYC DoF, NYC HPD
"""
)

# Styling

NTA20_style = {
    "stroke": True,
    "color": 'black',
    "weight": 1,
    "opacity":0.7,
    "fill": False
}

# Map
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12, tiles="CartoDB.Positron")

m.add_data(MedInc22_AMI22_BG22_geo, 
                   column='AMI22_3Family_Ranked',
                   legend_title='2022 AMI Range (3 Family Household)',
                   info_mode='on_click')

m.add_gdf(gdf = NTA20, style = NTA20_style, info_mode = False)

m.to_streamlit(height=500)