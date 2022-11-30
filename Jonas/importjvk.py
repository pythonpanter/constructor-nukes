#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:42:43 2022

@author: jvk
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
import os 
from plotly.express import choropleth
import plotly.subplots
import time


def get_data():

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    urlcsv=dir_path+"/archive/nuclear_weapons_stockpiles.csv"
    stockpiles = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/archive/nuclear_weapons_tests_states.csv"
    tests_states = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True).reset_index()
    
    urlcsv=dir_path+"/archive/nuclear_weapons_proliferation_total_owid.csv"
    proliferationTot = pd.read_csv(urlcsv, index_col = [0,1], skipinitialspace=True)
    
    urlcsv=dir_path+"/archive/nuclear_weapons_proliferation_owid.csv"
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
    # print(lrge_df.head(2))
    return "Jonas1",lrge_df
# print("")
# print("")
# print("")

# print(*lrge_df.to_numpy())
# print(lrge_df.head(2))
# print("")
# print("")
# print("")
# print(yearcontrdict[list(yearcontrdict.keys())[0]])

# quit()


# print(stockpiles.head())
# print(tests_states.head())
# print(proliferation.head())
# # lrge_df=pd.concat([stockpiles, tests_states, proliferation], axis=1, keys=["country_name","year"],ignore_index=True)
# lrge_df=pd.concat([proliferation,tests_states, stockpiles]).reset_index()
# # lrge_df = lrge_df.reset_index()
# # lrge_df = lrge_df.unstack("second")
# # lrge_df = lrge_df.unstack()
# # lrge_df.columns = lrge_df.columns.droplevel(0)

# print(lrge_df.head(2).to_numpy())
# print("")
# print("")
# print("")

# # print(lrge_df.head(100000).to_numpy()[0])
# print(*lrge_df.head(100000).to_numpy())
# print("")
# print("")
# print("")
# print(lrge_df.head(1))

# # print(lrge_df[0])

