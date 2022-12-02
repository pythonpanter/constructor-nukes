#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:47:02 2022

@author: jvk
"""


import pandas as pd
import streamlit as st
import os
import json


@st.cache
def get_dataOLD():

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_stockpiles.csv"
    stockpiles = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_tests_states.csv"
    tests_states = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_proliferation_total_owid.csv"
    proliferationTot = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True)
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_proliferation_owid.csv"
    proliferation = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    yearcontrdict={}
    def dictkeyadd(frame):
        yearpos=None
        countrpos=None
        cols=list(frame.columns.values)
        for colind in range(len(cols)):
            if cols[colind]=="year":
                yearpos=colind
            if cols[colind]=="country_name":
                countrpos=colind
        for row in frame.to_numpy():
            retval={str(cols[ind]): row[ind] for ind in range(len(row))}
            mykey=str([row[yearpos],row[countrpos]])
            if mykey in yearcontrdict.keys():
                yearcontrdict[mykey].update(retval)
            else:
                yearcontrdict[mykey]=retval
              
    dictkeyadd(stockpiles)
    dictkeyadd(tests_states)
    dictkeyadd(proliferation)
    lrge_df=pd.DataFrame.from_dict(yearcontrdict, orient='index').fillna(0).reset_index(drop=True)
    return "Jonas1",lrge_df


@st.cache
def get_data():

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #data from https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
    urlcsv=dir_path+"/../Jonas/archive/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4701247/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4701247.csv"
    GDPglob = pd.read_csv(urlcsv, index_col = [0], skipinitialspace=True,header=2)
    
    urlcsv=dir_path+"/../Jonas/archive/API_SI.POV.GINI_DS2_en_csv_v2_4701295/API_SI.POV.GINI_DS2_en_csv_v2_4701295.csv"
    giniglob = pd.read_csv(urlcsv, index_col = [0], skipinitialspace=True,header=2)
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_stockpiles.csv"
    stockpiles = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_tests_states.csv"
    tests_states = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_proliferation_total_owid.csv"
    proliferationTot = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True)
    
    urlcsv=dir_path+"/../dataset/nuclear_weapons_proliferation_owid.csv"
    proliferation = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    GDPglob.rename(columns = {'Country Name':'country_name'}, inplace = True)
    giniglob.rename(columns = {'Country Name':'country_name'}, inplace = True)
    yearcontrdict={}
    def dictkeyadd(frame):
        yearpos=None
        countrpos=None
        cols=list(frame.columns.values)
        for colind in range(len(cols)):
            if cols[colind]=="year":
                yearpos=colind
            if cols[colind]=="country_name":
                countrpos=colind
        for row in frame.to_numpy():
            retval={str(cols[ind]): row[ind] for ind in range(len(row))}
            mykey=json.dumps([row[yearpos],row[countrpos]])
            if mykey in yearcontrdict.keys():
                yearcontrdict[mykey].update(retval)
            else:
                yearcontrdict[mykey]=retval
              
    dictkeyadd(stockpiles)
    dictkeyadd(tests_states)
    dictkeyadd(proliferation)
    
    def dictkeyupdate(frame, handle):
        mykeys=list(yearcontrdict.keys())
        for key in mykeys:
            keylist = json.loads(key)
            try:
                yearcontrdict[key].update({handle:frame[str(keylist[0])][keylist[1]]})
            except:
                pass
    dictkeyupdate(GDPglob, "GDP")
    dictkeyupdate(giniglob, "Gini")
    lrge_df=pd.DataFrame.from_dict(yearcontrdict, orient='index').reset_index(drop=True)
    lrge_df=lrge_df.combine_first(get_dataOLD()[1])
    return "Jonas1",lrge_df


import numpy as np
from pandas.api.types import is_numeric_dtype

@st.cache
def eval_frame(datahandle="Jonas1", df=get_data()[1]):
    print("Evaluating "+datahandle)
    cols=list(df.columns.values)
    isnumeric=np.zeros(len(cols))
    for colind in range(len(cols)):
        isnumeric[colind]=is_numeric_dtype(df[cols[colind]])
        
    for name in list(df["country_name"].unique()):
        locdf=df[df["country_name"]==name]
        for colind in range(len(cols)):
            # print(isnumeric)
            if isnumeric[colind]:
                diff=locdf[cols[colind]].diff()
                if "_diff" not in cols[colind]:
                    df[cols[colind]+"_diff"]=diff
    cols2=list(df.columns.values)
    isnumeric2=np.zeros(len(cols2))
    for colind in range(len(cols)):
        isnumeric2[colind]=is_numeric_dtype(df[cols[colind]])
    iscategorical=np.zeros(len(cols))
    for colind in range(len(cols)):
        locvals=list(pd.unique(df[cols[colind]]))
        if len(locvals)<3 or not isnumeric2[colind]:
            iscategorical[colind]=True
        else:
            iscategorical[colind]=False
    dummydict={"title":'None',
        "description" : 'None',
        "key":'None',
        "lib" : 'None'}

    return "eval JvK", df, dummydict
import plotly.express as px
import plotly.graph_objects as go

# def get_plots(string=eval_frame()[0],df=eval_frame()[1],info=eval_frame()[2]):
#     df['Intercept'] = 1
#     empty=df.head(0)
#     print(empty)
#     cols=list(df.columns.values)
#     inactives=[]
#     for country in list(df["country_name"].unique()):
#         locdf=df[df["country_name"]==country]
#         if not (locdf["nuclear_weapons_pursuit"].max()>0):
#             inactives.append(country)
        
#     df['year']=pd.to_numeric(df['year'])
    
#     filtered = df[df['year']>1985]
#     for inactive in inactives:
#         filtered = filtered[filtered['country_name'] !=inactive]
#     dfs=[df, filtered]
#     pairs=[]
#     retval=[]
#     for ind1 in range(len(cols)):
#         for ind2 in range(0,ind1):
#            pairs.append([cols[ind1],cols[ind2]])
#     for pair in pairs:
#         for dfind in range(len(dfs)):
#             locdf=pd.DataFrame(dfs[dfind],copy=True)
#             numeric_df = filtered.filter(items=[pair[0], pair[1]]).dropna()
#             corr = numeric_df.corr()
#             npcorr=corr.to_numpy()
#             # print(type(locdf['year'].astype(str)))
#             # print(locdf[['text']].head(2))
#             # quit()
#             # locdf['text']=("country: "+locdf['country_name'].astype(str)).str.cat(
#             # ("\n year" +locdf['year'].astype(str)),
#             # ("\n "+str(pair[0]) +locdf[pair[0]].astype(str)),
#             # ("\n "+str(pair[1]) +locdf[pair[1]].astype(str)))
#             if npcorr.size==4 :
#                 boo=np.isfinite(npcorr).all() and (not np.isnan(npcorr).any())
#                 boo=boo and npcorr[1][1]<1.1 and npcorr[0][1]<1.1 and npcorr[0][0]<1.1
#                 boo=boo and npcorr[1][1]/npcorr[1][1]==1
#                 if abs(npcorr[0][1])>=0.5 and boo:
#                     print("")
#                     print(corr.to_numpy())
#                     # locdf2=locdf.dropna(subset = [pair[0], pair[1]])
#                     locdf2=locdf[df[pair[0]].notna()]
#                     locdf2=locdf2[df[pair[1]].notna()]
#                     # print(locdf[['text']].head())
#                     # quit()
#                     dummydf=pd.DataFrame(dfs[dfind],copy=True)
#                     dummydf["dummy1"]=("country: "+locdf2['country_name'].astype(str))
#                     dummydf["dummy2"]=("<br> year" +" "+locdf2['year'].astype(str))
#                     dummydf["dummy3"]=("<br> "+str(pair[0]) +": "+locdf2[pair[0]].astype(str))
#                     dummydf["dummy4"]=("<br> "+str(pair[1]) +": "+locdf2[pair[1]].astype(str))
#                     # strcols=["country: "+locdf['country_name'].astype(str), "\n year" +locdf['year'].astype(str),
#                     #       "\n "+str(pair[0]) +locdf[pair[0]].astype(str), "\n "+str(pair[1]) +locdf[pair[1]].astype(str)]
#                     strcols=["dummy1","dummy2","dummy3","dummy4"]
#                     locdf2['text']= dummydf[strcols].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
#                     # fig=px.imshow(corr)
#                     fig = go.Figure()
#                     countries=locdf2['country_name'].unique()
#                     title='Relation between '+pair[0]+" and "+pair[1]
#                     for cntry in countries:
#                         df_s = locdf2[locdf2['country_name']==cntry]
#                         fig.add_trace(
#                             go.Scatter(
#                                 x=df_s[pair[0]], y=df_s[pair[1]], 
#                                 mode="markers",
#                                 name=cntry.capitalize(),
#                                 text=df_s['country_name'],
#                                 marker={
#                                     "symbol": "square",
#                                     "sizemode": "area", 
#                                     "size": df_s['Intercept'], 
#                                     "sizeref": max(df['Intercept'])*0.01
#                                 },
#                                 hovertext=locdf2['text'],
#                                 hoverinfo="text"                               
#                                 # hoverinfo="country_name+year",
#                                 # hovertemplate="<b>%{text}</b><br><br>" +
#                                 # "Country: %{df_s['country_name']}"+
#                                 # "year: %{df_s['year']}"+
#                                 # pair[0]+": %{x:.1f}<br>" + 
#                                 # pair[1]+": %{y:.1f}<br>" +
#                                 # #"Petal length: %{marker.size:.1f}<br>" +
#                                 # "<extra></extra>"
#                             )
#                         )
#                     fig.update_layout(
#                         title=title,
#                         xaxis={"title": {"text": pair[0], "font_size": 18}}, # Note you can specify the size using font_size key
#                         yaxis={"title": {"text": pair[1], "font": {"size": 18}}}, # Or you can create a dictionnary if you want to add more font properties
#                         height=600,
#                         # plot_bgcolor="rgb(240, 250, 240)",
#                         # paper_bgcolor="rgb(240, 250, 240)"
#                         )
#                     description =pair[1] +" over "+  pair[0]#+", correlated"
#                     if dfind==0:
#                         description+=" for a data set reduced to nuclear states, cleaned of NaNs"
#                     else:
#                         description+=" for the data set, cleaned from NaNs"
#                     description+=" correllation is "+str(npcorr[1][1])
#                     key='nuclear'
#                     lib = 'plotly_go'
#                     info_dict=dict(title=title, description=description, lib=lib)
#                     retval.append((key,fig,info_dict))
#     return retval

# myplots=get_plots()

# print(len(get_plots()))
# for plot in myplots[:2]:
#     print(plot[2]["description"])
#     plot[1].show()

def get_plots():
    quit()

