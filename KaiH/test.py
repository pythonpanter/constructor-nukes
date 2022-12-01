# SET FOLDER ENVIRONMENT
import sys
if sys.platform=='win32':
    dots='..'
else:
    dots='.'

dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')

# SET STREAMLIT BASE
import streamlit as st
if sys.platform=='win32':
    st.title('***LOCAL INSTANCE***')
st.title('Nuke.N.')
st.image('bikinibomb.jpg')

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
      'kb':0,
      'kh':0}

import plotkb as pkb

plots=pkb.get_plots()
(key,fig,info_dict)=plots[0]

st.title('Kai B Plot')
st.plotly_chart(fig)





