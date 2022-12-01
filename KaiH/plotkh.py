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


#df=dfraw

df = dfraw[dfraw.year==2015]

codepath=f"{kaipath}country_codes.csv"
print(codepath)
dfcodes=pd.read_csv(codepath)
dfc2=dfcodes[['UNTERM English Short','FIFA']]
dfc2.dropna(inplace=True)
print(dfc2.head())
df= df.merge(dfc2, left_on='country_name', right_on='UNTERM English Short', how='left' )


#df.dropna(inplace=True)
df=df[(df.nuclear_weapons_stockpile>0)]
print(df.info())
df.index=df.country_name
#df['Russia'].FIFA='RUS'
df.at['Russia','FIFA']='RUS'
df.at['North Korea','FIFA']='PRK'  
df.at['United Kingdom','FIFA']='UK'  #############
df.at['United States ','FIFA']='US'  #############
dfc2.dropna(inplace=True)
print(df)
print(df.country_name.unique())




def get_plots():
    fig = go.Figure(data=go.Choropleth(
        locations=df['FIFA'],
        z=df['nuclear_weapons_stockpile'],
        colorscale='Jet',

        text=df['country_name'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title="% Pop.", marker_line_width=0)
    )

    #fig.update_layout(title_text='World wide web usage,')
    fig.update_layout(margin=dict(l=50, r=50, t=50, b=50), height=640,
                      plot_bgcolor="#0e1117",
                      paper_bgcolor="#0e1117",
                      font_color="white",
                      geo_bgcolor="#0e1117",
                      )
    fig.update_geos(showlakes=False,
                    projection_type="orthographic",
                    projection_rotation=dict(lon=10, lat=45, roll=0),
                    )
    #fig.update_traces(unselected_marker_opacity=0.5, selector=dict(type='choropleth'))
    title='dropping important stuff'
    description = 'Example description'
    key='inetusage'
    lib = 'plotly_go'
    info_dict=dict(title=title, description=description, lib=lib)
    tuple=(key,fig,info_dict)
    list=[tuple]
    return list
