###### Which columns do all three datasets have in common?
# nuclear_weapons_proliferation_owid.csv    ---> country_name   year    nuclear_weapons_status  nuclear_weapons_consideration   nuclear_weapons_pursuit     nuclear_weapons_possession
# nuclear_weapons_stockpiles.csv            ---> country_name   year                                                                                                                        nuclear_weapons_stockpile
# nuclear_weapons_tests_states.csv          ---> country_name   year                                                                                                                                                    nuclear_weapons_tests
#
# ---> Conclusion: The columns 'country_name' and 'year' are shared between the three datasets

###### Import modules
import pandas as pd
import os
import streamlit as st

##### Variables
list_of_columns = [] # List of columns

##### Functions
@st.cache
def read_data(pathToCsv):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    urlcsv = dir_path+pathToCsv
    csv_data = pd.read_csv(
        urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()
    return csv_data

@st.cache
def get_data():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    path_to_stockpiles = "/./dataset/nuclear_weapons_stockpiles.csv"
    path_to_tests = "/./dataset/nuclear_weapons_tests_states.csv"
    path_to_proliferation = "/./dataset/nuclear_weapons_proliferation_owid.csv"
    
    df_stockpiles = read_data(path_to_stockpiles)
    df_tests = read_data(path_to_tests)
    df_proliferation = read_data(path_to_proliferation)

    # Merge dataframes
    df_merged = pd.merge(pd.merge(df_proliferation, df_stockpiles, on=[
                         'country_name', 'year']), df_tests, on=['country_name', 'year'])
    
    
    ### Group by 'country_name' and 'year'
    overall_weapons_stockpile_per_country = df_merged.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_stockpile'].sum()
    overall_weapons_tests_per_country = df_merged.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_tests'].count()
    overall_weapons_status_per_country = df_merged.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_status'].count()
    
    # Merge dataframes
    # overall_stockpiles_tests_merged_df = pd.merge(overall_weapons_stockpile_per_country, overall_weapons_tests_per_country, on=['country_name', 'year'])
    df_merged = pd.merge(overall_weapons_stockpile_per_country, overall_weapons_tests_per_country, on=['country_name', 'year'])
    
        # Return the merged dataframe
    return "@Alexej_Khalilzada", df_merged

##### Main part for testing #####

# get_data() # let's grab the available data

""" merged_df = get_data()
author = merged_df[0]
merged_df = merged_df[1]

# Debug Output
print(f'* merged_df = \n{merged_df}')
print(f'* Length of dataframe "merged_df" = {len(merged_df)}')
print(f'* Author = {author}')

##### Playing around
### Group by country
# 
dummy_df = merged_df.copy()
overall_weapons_stockpile_per_country = dummy_df.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_stockpile'].sum()
overall_weapons_tests_per_country = dummy_df.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_tests'].count()
overall_weapons_status_per_country = dummy_df.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_status'].count()

print('\n\n****************************************************************************************************************\n')
print(overall_weapons_stockpile_per_country.head(60))
print('\n\n****************************************************************************************************************\n')
print(overall_weapons_tests_per_country.head(60))
print('\n\n****************************************************************************************************************\n')
print(overall_weapons_status_per_country.tail(60))

# Merge dataframes
overall_stockpiles_tests_merged_df = pd.merge(overall_weapons_stockpile_per_country, overall_weapons_tests_per_country, on=['country_name', 'year'])
print('\n\n****************************************************************************************************************')
print('****************************************************************************************************************\n')
print(overall_stockpiles_tests_merged_df.tail(60)) """

""" def dummy(dataframe):
    ##### Plot
    # 'year' in the x-axis and 'nuclear_weapons_stockpile' in the y-axis.
    fig = px.line(dataframe, x="year", y="nuclear_weapons_stockpile", color="country_name")

    # Marker's shape should be square.
    fig.update_traces(
        marker=dict(symbol="circle", line=dict(width=2, color="DarkSlateGrey")),
        selector=dict(mode="markers"),
    )

    # Change color background for the chart and the whole plot.
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 255)',
        'paper_bgcolor': 'rgba(255, 255, 255, 255)'
    })

    # Add title, and x and y labels with font size 18.
    fig.update_xaxes(title_text='Year', title_font = {"size": 18})
    fig.update_yaxes(title_text='Nuclear Weapons Stockpile', title_font = {"size": 18})
    fig.update_layout(title_text="Nuclear Weapons Stockpile per Country per Year", title_yanchor = "top", legend_itemsizing="constant")

    # return figure
    return fig

# weapons_tests_df = dummy_df.groupby(['country_name', 'year'], as_index=False)['nuclear_weapons_stockpile'].get_value()
# print('\n\n*************************************************************************** Weapons Tests DF *****************************\n')
# print(weapons_tests_df.tail(60))

def get_plots():
    title='Nuclear Weapons Stockpile per Country per Year'
    description = 'This chart shows the nuclear weapons stockpile per country per year'
    key='nuclear'
    lib = 'plotly_express'
    info_dict=dict(title=title, description=description, lib=lib)
    
    dummy(overall_stockpiles_tests_merged_df).show()
    
    return [(key, fig, info_dict)] """

# get_plots()