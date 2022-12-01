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
from scipy import stats
import itertools

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
    
    path_to_stockpiles = "/../dataset/nuclear_weapons_stockpiles.csv"
    path_to_tests = "/../dataset/nuclear_weapons_tests_states.csv"
    path_to_proliferation = "/../dataset/nuclear_weapons_proliferation_owid.csv"
    
    df_stockpiles = read_data(path_to_stockpiles)
    df_tests = read_data(path_to_tests)
    df_proliferation = read_data(path_to_proliferation)

    # Merge dataframes
    df_merged = pd.merge(pd.merge(df_proliferation, df_stockpiles, on=[
                         'country_name', 'year']), df_tests, on=['country_name', 'year'])
    
        # Return the merged dataframe
    return "@Alexej_Khalilzada", df_merged

##### Main part for testing #####

get_data() # let's grab the available data

merged_df = get_data()
author = merged_df[0]
merged_df = merged_df[1]

# Debug Output
print(f'* merged_df = {merged_df}')
print(f'* Length of dataframe "merged_df" = {len(merged_df)}')
print(f'* Author = {author}')
