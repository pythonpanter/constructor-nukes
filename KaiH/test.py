import sys
usr=['jvk','ak','kb','kh']
dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'../{d}')

import importjvk as jvk
import importak as ak              #Alexej not yet compatible



#testdata
import inputload as il
import plotter as cp
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy





lj=jvk.get_data()

print(type(lj[0]))
print(type(lj[1]))


ak=ak.get_data()

print(type(ak[0]))
print(type(ak[1]))

print('start')
st.title('This is a title ...')
il.test()



k,df=il.get_data()

print(k)
print(df.head())

(key,fig,info_dict)=cp.cplot(df)
print(key)
print(info_dict)


st.plotly_chart(fig)
st.plotly_chart(fig)
st.plotly_chart(fig)
st.plotly_chart(fig)
st.plotly_chart(fig)


print('end')

