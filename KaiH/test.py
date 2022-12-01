# SET FOLDER ENVIRONMENT
import sys
if sys.platform=='win32':
    dots='..'
    kaipath=''
else:
    dots='.'
    kaipath='./KaiH/'

dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')

# SET STREAMLIT BASE
import streamlit as st
if sys.platform=='win32':
    st.title('***LOCAL INSTANCE***')
st.title('Nuke.N.')
st.image(f'{kaipath}bikinibomb.jpg')

# IMPORT ADDITIONAL PACKAGES
from urllib.request import urlopen
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from copy import deepcopy
import pandas as pd
import json

# IMPORT PLOTS

usr= {'jvk':0,
      'ak':0,
      'kb':1,
      'kh':0}

def import_plots():
    (key, fig, info_dict) = plots[0]

if usr['kb']:
    import plotkb as pkb
    plots=pkb.get_plots()
    st.header('Kai B Plots')

    st.header(plots[0][2]['title'])
    st.subheader(plots[0][2]['description'])
    st.plotly_chart(plots[0][1])

if usr['ak']:
    import plotak as pak
    plots=pak.get_plots()
    st.header('Alexej Plots')

    st.plotly_chart(plots[0][1])

if usr['jvk']:
    import plotjvk as pjvk
    plots=pjvk.get_plots()
    st.header('Jonas Plots')

    st.plotly_chart(plots[0][1])

if usr['kh']:
    import plotkh as pkh
    plots=pkh.get_plots()
    st.header('Kai H Plots')

    st.plotly_chart(plots[0][1])






