import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go

#dirs=['Jonas','Alexej']
#for d in dirs:
#    sys.path.insert(0, f'{dots}/{d}')
#import importjvk as ijvk
#data= ijvk.get_data()
#df=data[1]
#print(data[1].head())
#
#import sys
#if sys.platform=='win32':
#    dots='..'
#    kaipath=''
#else:
#    dots='.'
#    kaipath='./KaiH/'
#for d in dirs:
#    sys.path.insert(0, f'{dots}/{d}')

df3 = pd.read_csv("data/nuclear_weapons_tests_states.csv")

title="Number of nuclear weapons tests, 1945 to 2019"
description="This interactive chart shows the number of nuclear weapons tests conducted since 1945. We can see that the Cold War was a very active period of nuclear weapons development. Although nuclear weapons were only ever used in warfare during the Second World War, there have been many tests conducted since then."

def kbplot():

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
    ),

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
    ),

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

    key=""
    info_dict=dict(title=title, description=description, lib="plotly_express")
    tuple=(key,fig3,info_dict)
    return tuple

def get_plots():
    rlist =[kbplot()]
    #rlist =[kbplot(),kbplot2()] #kbplot2 definieren!
    return rlist

testplot = kbplot()
testplot[1].show()