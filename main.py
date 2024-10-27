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

# Streamlit page config
st.set_page_config(
    page_title="Henry Alonso's HSS 350 Independent Study Streamlit Modules",
    page_icon="👋")

# Directory
current = Path.cwd() 
parent = current.resolve().parent / 'data'
os.chdir(parent)

# Streamlit code
st.write("# Welcome to my HSS 350 Streamlit modules!")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    ### Click on the sidebar to see interactive maps showing where New York City has built affordable housing.

     Welcome to my Independent Study Streamlit modules! Click on the sidebar for interactive maps showing where New York City has built affordable housing.

    ### About me
    
     My name is Henry Alonso. I'm an undergradute Urban Studies student at Queens College doing independent research on affordable housing subsidies under Prof. Dwayne Baker.
"""
)