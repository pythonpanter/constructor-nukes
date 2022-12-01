import sys
if sys.platform=='win32':
    dots='..'
else:
    dots='.'

usr=['jvk','ak','kb','kh']
dirs=['Jonas','Alexej','KaiB']

for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')
import importjvk as jvk
import importak as ak
dataframes=[]
dataframes.append(jvk.get_data())
dataframes.append(ak.get_data())
n,df=dataframes[0]
import pandas as pd
print(df.head())






import importjvk as jvk

import importak as ak
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
import streamlit as st
st.title('Nukes')
