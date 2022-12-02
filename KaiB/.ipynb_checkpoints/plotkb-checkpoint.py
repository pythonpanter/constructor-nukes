#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go


# In[20]:


import sys
if sys.platform=='win32':
    dots='..'
else:
    dots='.'
dirs=['Jonas','Alexej']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')
import importjvk as ijvk
data= ijvk.get_data()
df=data[1]
print(data[1].head())


# In[22]:


df = pd.read_csv("data/nuclear_weapons_tests_states.csv")


# In[23]:


df.head()


# In[118]:


df[df.country_name == "Russia"]


# In[24]:


# In[25]:


#df2 = df[["country_name","nuclear_weapons_stockpile","year"]][df["nuclear_weapons_stockpile"] > 0].copy()
#df2.head()


# In[ ]:


df3 = df[["country_name","nuclear_weapons_tests","year"]][df["nuclear_weapons_tests"] > 0].copy()

df3 = df


# In[172]:


fig3 = px.bar(
    data_frame=df3.sort_values(by=["country_name"]),
    x=df3["year"],
    y=df3["nuclear_weapons_tests"],
    color=df3["country_name"],
    barmode="stack",
    height=600,
    hover_name=df3["country_name"],
    #hover_data=,
    #labels=,
    title="Number of nuclear weapons tests, 1945 to 2019",
    labels={"color": "Country", "x": "", "y": "Tests"},
    color_discrete_sequence=px.colors.qualitative.G10
)

fig3.update_layout(
    xaxis=dict(
        range=[df3["year"].min(),2022],
        ticklabelstep=5,
        tickangle=0,
        tickmode="linear",
        #position=0,
        #anchor="free"
    ),
    yaxis=dict(
        #tickmode="linear",
        tick0=120,
        #dtick=20,
        range=[-5,190]
))

fig3.update_yaxes(ticksuffix = "   ")



########## Hiroshima, Nagasaki ##########

fig3.add_annotation(
        x=1948,
        y=40,
        xref="x",
        yref="y",
        text="1945<br>Atomic bombings<br>of Hiroshima<br> and Nagasaki",
        showarrow=False,
        font=dict(
            #family="Courier New, monospace",
            size=10,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        #ax=65,
        #ay=-80,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#21618C",
        opacity=0.8
        )

########## Cold War ##########

fig3.add_vrect(
    x0="1947", x1="1991",
    fillcolor="LightSalmon", opacity=0.3,
    layer="below", line_width=0,
),

fig3.add_annotation(
        x=1980,
        y=170,
        xref="x",
        yref="y",
        text="Cold War",
        showarrow=False,
        font=dict(
            #family="Courier New, monospace",
            size=12,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        #ax=65,
        #ay=-80,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="DarkRed",
        opacity=0.7
        )

########## USSR 1st test ##########

fig3.add_annotation(
        x=1950,
        y=80,
        xref="x",
        yref="y",
        text="1949<br>USSR: 1st<br>successful test",
        showarrow=False,
        font=dict(
            #family="Courier New, monospace",
            size=10,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=30,
        ay=-140,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#21618C",
        opacity=0.8
        )

fig3.add_hrect(
    y0=-5, y1=0,
    fillcolor="white", opacity=1,
    layer="below", line_width=0,
),

fig3.show()


# In[180]:


def kbplot():
    
    fig3 = px.bar(
        data_frame=df3.sort_values(by=["country_name"]),
        x=df3["year"],
        y=df3["nuclear_weapons_tests"],
        color=df3["country_name"],
        barmode="stack",
        height=600,
        hover_name=df3["country_name"],
        #hover_data=,
        #labels=,
        title="Number of nuclear weapons tests, 1945 to 2019",
        labels={"color": "Country", "x": "", "y": "Tests"},
        color_discrete_sequence=px.colors.qualitative.G10
    )

    fig3.update_layout(
        xaxis=dict(
            range=[df3["year"].min(),2022],
            ticklabelstep=5,
            tickangle=0,
            tickmode="linear",
            #position=0,
            #anchor="free"
        ),
        yaxis=dict(
            #tickmode="linear",
            tick0=120,
            #dtick=20,
            range=[-5,190]
    ))

    fig3.update_yaxes(ticksuffix = "   ")



    ########## Hiroshima, Nagasaki ##########

    fig3.add_annotation(
            x=1948,
            y=40,
            xref="x",
            yref="y",
            text="1945<br>Atomic bombings<br>of Hiroshima<br> and Nagasaki",
            showarrow=False,
            font=dict(
                #family="Courier New, monospace",
                size=10,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            #ax=65,
            #ay=-80,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#21618C",
            opacity=0.8
            )

    ########## Cold War ##########

    fig3.add_vrect(
        x0="1947", x1="1991",
        fillcolor="LightSalmon", opacity=0.3,
        layer="below", line_width=0,
    ),

    fig3.add_annotation(
            x=1980,
            y=170,
            xref="x",
            yref="y",
            text="Cold War",
            showarrow=False,
            font=dict(
                #family="Courier New, monospace",
                size=12,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            #ax=65,
            #ay=-80,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="DarkRed",
            opacity=0.7
            )

    ########## USSR 1st test ##########

    fig3.add_annotation(
            x=1950,
            y=80,
            xref="x",
            yref="y",
            text="1949<br>USSR: 1st<br>successful test",
            showarrow=False,
            font=dict(
                #family="Courier New, monospace",
                size=10,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=30,
            ay=-140,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#21618C",
            opacity=0.8
            )

    fig3.add_hrect(
        y0=-5, y1=0,
        fillcolor="white", opacity=1,
        layer="below", line_width=0,
    ),
    
    key=""
    info_dict=dict(title="", description="", lib="plotly_express")
    tuple=(key,fig3,info_dict)
    return tuple

def get_plots():
    rlist =[kbplot()]
    return rlist


# In[179]:


testplot = kbplot()
testplot[1].show()


# In[ ]:




