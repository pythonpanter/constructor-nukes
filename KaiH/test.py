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
st.title('Nuke. N.')
st.image(f'{kaipath}bikinibomb.jpg')
st.caption('Showgirl Joy Healy smiles as she straddles a U.S. Air Force missile, wearing a bikini costume, at an American Federation of Labor Union show, in Los Angeles, California, in 1945  (Photo credit: Hulton Archive/Getty Images)')

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

def import_plots(plots):
    for i in range (0,len(plots)):
        st.header(plots[i][2]['title'])
        st.subheader(plots[i][2]['description'])
        if (plots[i][2]['lib']=='plotly_go') or (plots[i][2]['lib']=='plotly_chart'):
            st.plotly_chart(plots[i][1])

if usr['kb']:
    import plotkb as pkb
    plots=pkb.get_plots()
    st.header('Kai B Plots')
    import_plots(plots)

if usr['ak']:
    import plotak as pak
    plots=pak.get_plots()
    st.header('Alexej Plots')
    import_plots(plots)

if usr['jvk']:
    import plotjvk as pjvk
    plots=pjvk.get_plots()
    st.header('Jonas Plots')
    import_plots(plots)

if usr['kh']:
    import plotkh as pkh
    plots=pkh.get_plots()
    st.header('Kai H Plots')
    import_plots(plots)







