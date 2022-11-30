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

print('end')

