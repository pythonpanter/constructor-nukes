#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:26:00 2022

@author: jvk
"""

# import pandas as pd
# import plotly.express as px
# import json
# import plotly.graph_objects as go
# import evaljvk as ejvk
# import importjvk as ijvk

# myEval=ejvk.eval_frame()

import evaljvk as ejvk
import seaborn as sns
import matplotlib.pyplot as plt
import importjvk as ijvk
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import numpy as np

# @st.cache
def get_plots(string=ejvk.eval_frame()[0],df=ejvk.eval_frame()[1],info=ejvk.eval_frame()[2]):
    # df[['year']]=df[['year']].astype('float64', raise_on_error = False)
    empty=df.head(0)
    print(empty)
    cols=list(df.columns.values)
    inactives=[]
    for country in list(df["country_name"].unique()):
        locdf=df[df["country_name"]==country]
        # locdf["nuclear"]=(locdf["nuclear_weapons_pursuit"].max()>0)
        if not (locdf["nuclear_weapons_pursuit"].max()>0):
            inactives.append(country)
        
    df['year']=pd.to_numeric(df['year'])
    
    filtered = df[df['year']>1985]
    for inactive in inactives:
        filtered = filtered[filtered['country_name'] !=inactive]
    dfs=[df, filtered]
    pairs=[]
    retval=[]
    for ind1 in range(len(cols)):
        for ind2 in range(0,ind1):
           pairs.append([cols[ind1],cols[ind2]])
    for pair in pairs:
        for dfind in range(len(dfs)):
            locdf=dfs[dfind]
            # print(list(filtered.columns.values))
            numeric_df = filtered.filter(items=[pair[0], pair[1]]).dropna()
            # print(numeric_df)
            corr = numeric_df.corr()
            # print("")
            # print(corr.to_numpy())
            # quit()
            npcorr=corr.to_numpy()
            if npcorr.size==4 :
                boo=np.isfinite(npcorr).all() and (not np.isnan(npcorr).any())
                # print(type(npcorr[1][1]))
                boo=boo and npcorr[1][1]<1.1 and npcorr[0][1]<1.1 and npcorr[0][0]<1.1
                boo=boo and npcorr[1][1]/npcorr[1][1]==1
                if abs(npcorr[0][1])>=0.5 and boo:
                    print("")
                    print(corr.to_numpy())
                    # fig = go.Figure()
                    # fig.add_trace(px.imshow(corr))
                    fig=px.imshow(corr)
                    # fig.heatmap(corr, cmap=sns.diverging_palette(140, 10, as_cmap=True), vmin=-1, vmax=1)
                    # fig.show()
                    title='Correlation between '+pair[0]+" and "+pair[1]
                    description = pair[0]+" and "+pair[1]+", correlated"
                    if dfind==0:
                        description+=" for a data set reduced to nuclear states, cleaned of NaNs"
                    else:
                        description+=" for the data set, cleaned from NaNs"
                    description+=" correllation is "+str(npcorr[1][1])
                    key='nuclear'
                    lib = 'plotly_express'
                    info_dict=dict(title=title, description=description, lib=lib)
                    retval.append((key,fig,info_dict))
    return retval


# def get_plots(string=ejvk.eval_frame()[0],frame=ejvk.eval_frame()[1],info=ejvk.eval_frame()[2]):
#     return plot_eval(df=frame)

myplots=get_plots()
print(len(get_plots()))
for plot in myplots[:2]:
    print(plot[2]["description"])
    plot[1].show()


