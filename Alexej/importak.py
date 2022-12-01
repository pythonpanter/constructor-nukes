# Find columns which all three datasets have in common
# nuclear_weapons_proliferation_owid.csv    ---> country_name   year    nuclear_weapons_status  nuclear_weapons_consideration   nuclear_weapons_pursuit     nuclear_weapons_possession
# nuclear_weapons_stockpiles.csv            ---> country_name   year                                                                                                                        nuclear_weapons_stockpile
# nuclear_weapons_tests_states.csv          ---> country_name   year                                                                                                                                                    nuclear_weapons_tests
#
# ---> Conclusion: The columns 'country_name' and 'year' are shared between the three datasets

# Import modules
import pandas as pd
import os
import streamlit as st


@st.cache
def get_data():

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    urlcsv = dir_path+"/../dataset/nuclear_weapons_stockpiles.csv"
    df_stockpiles = pd.read_csv(
        urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    urlcsv = dir_path+"/../dataset/nuclear_weapons_tests_states.csv"
    df_states = pd.read_csv(
        urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    urlcsv = dir_path+"/../dataset/nuclear_weapons_proliferation_owid.csv"
    df_proliferation = pd.read_csv(
        urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    # Merge dataframes
    df_merged = pd.merge(pd.merge(df_proliferation, df_stockpiles, on=[
                         'country_name', 'year']), df_states, on=['country_name', 'year'])

    return "Alexej1", df_merged
