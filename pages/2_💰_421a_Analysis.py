# Import
import os
from pathlib import Path
from shapely.geometry import Point
import numpy as np
import pandas as pd 
import geopandas as gpd
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

# Config
st.set_page_config(
    page_title='HPD 421a Analysis Dashboard',
    page_icon='🏘️',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load
HPD_AFF_Project_421a_BG22_geo = gpd.read_file("./data/HPD_AFF_Project_421a_BG22_geo.geojson")
NTA20 = gpd.read_file("./data/NTA20.geojson")

# Write 
st.write("# HPD 421a Analysis Dashboard")

st.markdown(
    """
    ### Below is an interactive map tool displaying the amount of units financed by the 421a tax abatement since 2014 across NYC 2022 Census Block Groups. 
    Click the sidebar on the left to display the targeted income of units financed by 421a across block groups.

    Sources: Census Bureau, NYC DoF, NYC HPD, 
"""
)
# Map
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12, tiles="CartoDB.Positron")

# Label options
label="unit_type"
options = ['Extremely Low Income Units',
           'Very Low Income Units',
           'Low Income Units',
           'Moderate Income Units',
           'Middle Income Units',
           'Other Income Units',
           'Counted Rental Units',
           'Counted Homeownership Units',
           'All Counted Units',
           'Total Units'
           ]

# Callback function for pollutant map
def update_map(unit_type):
    if unit_type == 'Extremely Low Income Units':
        st.session_state['selection'] = 0
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Extremely Low Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Extremely Low Income Units',
                   info_mode='on_click')
    elif unit_type == 'Very Low Income Units':
        st.session_state['selection'] = 1
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Very Low Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Very Low Income Units',
                   info_mode='on_click')
    elif unit_type == 'Low Income Units':
        st.session_state['selection'] = 2
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Low Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Low Income Units',
                   info_mode='on_click')
    elif unit_type == 'Moderate Income Units':
        st.session_state['selection'] = 3
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Moderate Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Moderate Income Units',
                   info_mode='on_click')
    elif unit_type == 'Middle Income Units':
        st.session_state['selection'] = 4
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Middle Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Middle Income Units',
                   info_mode='on_click')
    elif unit_type == 'Other Income Units':
        st.session_state['selection'] = 5
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Other Income Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Other Income Units',
                   info_mode='on_click')
    elif unit_type == 'Counted Rental Units':
        st.session_state['selection'] = 6
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Counted Rental Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Counted Rental Units',
                   info_mode='on_click')
    elif unit_type == 'Counted Homeownership Units':
        st.session_state['selection'] = 7
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Counted Homeownership Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Counted Homeownership Units',
                   info_mode='on_click')
    elif unit_type == 'All Counted Units':
        st.session_state['selection'] = 8
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='All Counted Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='All Counted Units',
                   info_mode='on_click')
    elif unit_type == 'Total Units':
        st.session_state['selection'] = 9
        m.add_data(HPD_AFF_Project_421a_BG22_geo, 
                   column='Total Units_sum', 
                   scheme='NaturalBreaks',
                   cmap='Blues', 
                   legend_title='Total Units',
                   info_mode='on_click')
    m.to_streamlit(height=500)

# Initialize the session state
if 'unit_type' not in st.session_state:
    st.session_state['unit_type'] = 'Total Units'

# Select box
with st.sidebar:
    selected_unit_type = st.selectbox(label, options, index=options.index(st.session_state['unit_type']))

update_map(selected_unit_type)
