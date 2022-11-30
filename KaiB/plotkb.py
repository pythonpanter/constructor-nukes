import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go

# Read in the data

df_int = pd.read_csv("data/share-of-individuals-using-the-internet.csv")
df_int.head()

# Select data from the most recent YEAR for each COUNTRY

countries = []
mr_year = []

for grp, df in df_int.groupby("Code"):
    countries.append(grp)
    #print("GRP:", grp)
    mr_year.append(df["Year"].max())
    #print("YEAR:", df["Year"].max())

df_years = pd.DataFrame({"Code": countries, "most_recent_year": mr_year})

df_rec = pd.merge(df_years, df_int)
df_rec = df_rec[df_rec["Year"]==df_rec["most_recent_year"]]
df_rec.head()

df_rec.rename(columns = {"Individuals using the Internet (% of population)": "Percentage", "Entity": "Country"}, inplace = True)
df_rec.head()

def cplot(df):
    fig = go.Figure(data=go.Choropleth(
        locations=df['Code'],
        z=df['Percentage'],
        colorscale='ice',

        text=df['Country'],  # hover text
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
    title='Im a title'
    description = 'Example description'
    key='inetusage'
    lib = 'plotly_go'
    info_dict=dict(title=title, description=description, lib=lib)
    return (key,fig,info_dict)

cplot(df_rec)