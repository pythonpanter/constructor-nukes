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


def plot_eval(df):
    # df[['year']]=df[['year']].astype('float64', raise_on_error = False)
    print(df.head())
    df['year']=pd.to_numeric(df['year'])
    filtered = df[df['year']>1979]
    numeric_df = filtered.filter(items=['Recency', 'Frequency', 'Revenue'])
    corr = numeric_df.corr()
    fig=sns.objects.Plot()
    fig.heatmap(corr, cmap=sns.diverging_palette(140, 10, as_cmap=True), vmin=-1, vmax=1)
    # ax.show()



data= ejvk.eval_frame()

plot_eval(data[1])







