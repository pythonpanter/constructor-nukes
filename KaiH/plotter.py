import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go


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
    return fig
