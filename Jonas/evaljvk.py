#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:53:53 2022

@author: jvk
"""

import pandas as pd
import streamlit as st
import os
import json
# from scipy.stats import shapiro
# from importjvk import get_data
import numpy as np
import importjvk as jvk
from pandas.api.types import is_numeric_dtype

# @st.cache
def eval_frame(datahandle="Jonas1", df=jvk.get_data()[1]):
    # quit()
    # df["nuclear"]=False
    # for country in list(df["country_name"].unique()):
    #     locdf=df[df["country_name"]==country]
    #     # locdf["nuclear"]=(locdf["nuclear_weapons_pursuit"].max()>0)
    #     df[df["country_name"]==country]["nuclear"]=(locdf["nuclear_weapons_pursuit"].max()>0)
    # df["nuclear"]=df[["nuclear"]].fillna(value=False)
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
    # isnormal=np.zeros(len(cols))
    # for colind in range(len(cols)):
    #     if isnumeric2[colind] and not iscategorical[colind]:
    #         locseries=df[cols[colind]].dropna()
    #         test_stat, p_value =shapiro(locseries)
    #         if p_value>0.05:
    #             isnormal[colind]=True
    #         else:
    #             isnormal[colind]=False
    #     else:
    #         pass
    print(list(df.columns.values))
    return "eval JvK", df, None
# eval_frame()
# evalframe=eval_frame(*jvk.get_data())[1]
# # quit()

# # eval_frame(*jvk.get_data())
# # print(eval_frame(*jvk.get_data()))
# np.set_printoptions(threshold=np.inf)
# np.set_printoptions(linewidth=np.inf)
# # print(evalframe.head(1))
# # print(evalframe["nuclear"].unique())
# # print(evalframe[evalframe["nuclear"]==True].to_numpy())
# print(list(evalframe.columns.values))
# print(list(evalframe.head(1).to_numpy()))




