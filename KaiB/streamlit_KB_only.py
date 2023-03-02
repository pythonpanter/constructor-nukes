import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

# Read in the data
# df_raw = load_data(path="data/share-of-individuals-using-the-internet.csv")
# df_int = deepcopy(df_raw)

#df3 = pd.read_csv("data/nuclear_weapons_tests_states.csv")

import os

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the file path using os.path.join()
file_path = os.path.join(dir_path, "data", "nuclear_weapons_tests_states.csv")

# Load the data using pd.read_csv()
df3 = pd.read_csv(file_path)

# Add title and header
st.title("Number of nuclear weapons tests, 1945 to 2019")
st.caption("The interactive graph presents the number of nuclear weapon tests conducted since 1945. It indicates a high frequency of testing during the Cold War period. Although nuclear weapons were only used in WWII, many tests were conducted following the war. The chart allows for a full-screen view by clicking the top right corner.")

# Setting up columns
# left_column, middle_column, right_column = st.columns([3, 1, 1])

# Plotting

fig3 = px.bar(
        data_frame=df3.sort_values(by=["country_name"]),
        x=df3["year"],
        y=df3["nuclear_weapons_tests"],
        color=df3["country_name"],
        barmode="stack",
        height=600,
        hover_name=df3["country_name"],
        #hover_data="Test <extra></extra>",
        #labels=,
        title="Number of nuclear weapons tests, 1945 to 2019",
        labels={"color": "Country as of 2022", "x": "", "y": ""},
        color_discrete_sequence=px.colors.qualitative.G10
    )

hovertemp="%{y}"

fig3.update_traces(hovertemplate=hovertemp)

fig3.update_layout(
    xaxis=dict(
        range=[1942,2022],
        ticklabelstep=5,
        tickangle=0,
        tickmode="linear",
        showgrid=False,
        #position=0,
        #anchor="free"
    ),
    yaxis=dict(
        #tickmode="linear",
        #tick0=20,
        #ticklabelstep=20,
        dtick=20,
        range=[-5,195],
        #showgrid=False,
        griddash="dot",
        gridcolor="DarkGrey",
        gridwidth=0.01,
        #ticklabelstep=20,
        tickson="boundaries",
        ticksuffix="   ",
        #minor=dict(
        #    dtick=0.1,
        #    tick0=20),
        #tickmode="auto"

))

#fig3.update_yaxes(ticksuffix = "   ")

########## Cold War ##########

fig3.add_vrect(
    x0="1947", x1="1991",
    fillcolor="LightSalmon", opacity=0.3,
    layer="below", line_width=0,
)

fig3.add_annotation(
        x=1951,
        y=180,
        xref="x",
        yref="y",
        text="1947 - 1991<br>Cold War",
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

fig3.add_hrect(
    y0=-5, y1=0,
    fillcolor="#010008", opacity=1,
    layer="below", line_width=0,
)

fig3.add_scatter(
    x=[1946],
    y=[10],
    name="1945",
    showlegend=False,
    hovertemplate="<b>1945:</b><br>Atomic bombings of Hiroshima and Nagasaki<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1949],
    y=[10],
    name="1949",
    showlegend=False,
    hovertemplate="<b>1949:</b><br>First successful test by USSR<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1962],
    y=[185],
    name="1962",
    showlegend=False,
    hovertemplate="<b>1962:</b><br>Cuban Missile Crisis<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1968],
    y=[86],
    name="1968",
    showlegend=False,
    hovertemplate="<b>1968:</b><br>Non-Proliferation Treaty<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1970],
    y=[72],
    name="1969",
    showlegend=False,
    hovertemplate="<b>1969:</b><br>Détente began in 1969, as a core element of the foreign policy<br>of president Richard Nixon and his top advisor Henry Kissinger. They wanted to end<br>the containment policy and gain friendlier relations with the USSR and China.<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1980],
    y=[65],
    name="1979",
    showlegend=False,
    hovertemplate="<b>1979:</b><br>Cold War flares up after Soviet invasion of Afghanistan<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[1998],
    y=[10],
    name="1998",
    showlegend=False,
    hovertemplate="<b>1998:</b><br>India test detonated five nuclear weapons. Domestic pressure<br>within Pakistan began to build which resulted in detonating six nuclear weapons.<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

fig3.add_scatter(
    x=[2006],
    y=[10],
    name="2006",
    showlegend=False,
    hovertemplate="<b>2006:</b><br>First successful test by North Korea<extra></extra>",
    marker=dict(
        size=20,
        color="#21618C",
        opacity=0.8,
        line_color="white",
        line_width=1,
))

st.plotly_chart(fig3)

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)