import sys
usr=['jvk','ak','kb','kh']
dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'../{d}')
dataframes=[]
dataframes.append(jvk.get_data())
dataframes.append(ak.get_data())

print(dataframes)



import importjvk as jvk
#import importak as ak              #Alexej not yet compatible
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

st.title('Nukes')
