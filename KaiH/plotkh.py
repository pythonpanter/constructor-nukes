# SET FOLDER ENVIRONMENT
import sys
if sys.platform=='win32':
    dots='..'
    kaipath=''
else:
    dots='.'
    kaipath='./KaiH/'

dirs=['Jonas','Alexej','KaiB']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')

import pandas as pd
import plotly.graph_objects as go

#import evaljvk as ejvk
import importjvk as ijvk

data= ijvk.get_dataOLD()
df=data[1]
#print(data[1].head())
#data2=ejvk.eval_frame(datahandle="Jonas1", df=ijvk.get_dataOLD()[1])
dfraw=data[1]


codepath=f"{kaipath}country_codes.csv"

dfcodes=pd.read_csv(codepath)
#df=dfraw


def splot(cyear,lat,long,roll):
    df = dfraw[dfraw.year==cyear]




    dfc2=dfcodes[['UNTERM English Short','FIFA']]
    dfc2.dropna(inplace=True)
    print(dfc2.head())
    df= df.merge(dfc2, left_on='country_name', right_on='UNTERM English Short', how='left' )


    #df.dropna(inplace=True)
    df=df[(df.nuclear_weapons_stockpile>0)]
    print(df.info())
    print(df)
    dfc2.dropna(inplace=True)
    dfc2
    #df=df.set_index('country_name')
    #df['Russia'].FIFA='RUS'
    #df.at['Russia','FIFA']='RUS'
    #df.at['North Korea','FIFA']='PRK'
    #df.at['United Kingdom','FIFA']='GBR'  #############
    #df.at['United States','FIFA']='USA'  #############
    df['FIFA'][df.country_name=='Russia']='RUS'
    df['FIFA'][df.country_name=='North Korea']='PRK'
    df['FIFA'][df.country_name=='United Kingdom']='GBR'
    df['FIFA'][df.country_name=='United States']='USA'

    #dfc2.dropna(inplace=True)
    print(df)
    print(df.country_name.unique())





    fig = go.Figure(data=go.Choropleth(
        locations=df['FIFA'],
        z=df['nuclear_weapons_stockpile'],
        zmin=0,
        zmax=35000,
        colorscale='Bluered',

        text=df['country_name'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title="Nukes", marker_line_width=0)
    )

    #fig.update_layout(title_text='World wide web usage,')
    fig.update_layout(margin=dict(l=50, r=50, t=50, b=50), width=2000, autosize=False,
                      plot_bgcolor="#010008",
                      paper_bgcolor="#010008",
                      font_color="white",
                      geo_bgcolor="#010008",
                      )
    fig.update_geos(showlakes=False,
                    projection_type="orthographic",
                    projection_rotation=dict(lon=long, lat=lat , roll=roll),
                    showland=True, landcolor="#222222",
                    )
    #fig.update_traces(unselected_marker_opacity=0.5, selector=dict(type='choropleth'))
    title=''
    description = f'National stockpile of nuclear Weapons in {str(cyear)}'
    key='stockpilek'
    lib = 'plotly_go'
    info_dict=dict(title=title, description=description, lib=lib)
    tuple=(key,fig,info_dict)
    return tuple


def get_plots():
    rlist =[splot(1945,35,-105,0),splot(1985,60,100,0),splot(2022,90,0,0)]
    return rlist
