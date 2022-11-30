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
df=pd.read_csv('share-of-individuals-using-the-internet.csv')
df.rename(columns={'Individuals using the Internet (% of population)':'Percentage','Entity':'Country'}, inplace=True)

fig=cp.cplot(df)

st.plotly_chart(fig)
st.plotly_chart(fig)

print('end')

