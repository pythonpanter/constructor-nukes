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




# IMPORT ADDITIONAL PACKAGES
from urllib.request import urlopen
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from copy import deepcopy
import pandas as pd
import json

# SET USR
usr= {'jvk':0,
      'ak':0,
      'kb':1,
      'kh':0}


# SET STREAMLIT BASE
import streamlit as st
st.sidebar.title('NU*ES')
st.sidebar.image(f'{kaipath}nuke.jpg')
slide = st.sidebar.radio('',['Intro','Jonas Story','Alexejs  Story','Kais  Story','Architecture'])
st.header(slide)
if sys.platform=='win32':
    st.sidebar.title('***LOCAL INSTANCE***')
def import_plots(plots):
    for i in range (0,len(plots)):
        st.header(plots[i][2]['title'])
        st.subheader(plots[i][2]['description'])
        if (plots[i][2]['lib']=='plotly_go') or (plots[i][2]['lib']=='plotly_chart'):
            st.plotly_chart(plots[i][1])

# IMPORT PLOTS
if slide==('Kais  Story'):
    if usr['kb']:
        import plotkb as pkb
        plots=pkb.get_plots()
        import_plots(plots)
elif slide == ('kb'):
    if usr['ak']:
        import plotak as pak
        plots=pak.get_plots()
        import_plots(plots)
elif slide == ('kb'):
    if usr['jvk']:
        import plotjvk as pjvk
        plots=pjvk.get_plots()
        import_plots(plots)
elif slide == ('Architecture'):
    #if usr['kh']:
     #   import plotkh as pkh
      #  plots=pkh.get_plots()
       # import_plots(plots)
    st.image(f'{kaipath}architecture.jpg')
    st.caption(
        'Architecture of underlying framework (WIP)')
elif slide == ('Intro'):
    st.image(f'{kaipath}bikinibomb.jpg')
    st.caption('Showgirl Joy Healy smiles as she straddles a U.S. Air Force missile, wearing a bikini costume, at an American Federation of Labor Union show, in Los Angeles, California, in 1945  (Photo credit: Hulton Archive/Getty Images)')