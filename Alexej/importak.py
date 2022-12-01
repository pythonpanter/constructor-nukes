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

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    
    path_to_stockpiles = "/../dataset/nuclear_weapons_stockpiles.csv"
    path_to_tests = "/../dataset/nuclear_weapons_tests_states.csv"
    path_to_proliferation = "/../dataset/nuclear_weapons_proliferation_owid.csv"
    
    read_data(path_to_stockpiles)
    print(csv_data)
    df_stockpiles = csv_data
    
    read_data(path_to_tests)
    print(csv_data)
    df_tests = csv_data
    
    read_data(path_to_proliferation)
    print(csv_data)
    df_proliferation = csv_data
    
    # urlcsv = dir_path+"/../dataset/nuclear_weapons_stockpiles.csv"
    # df_stockpiles = pd.read_csv(
    #     urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    # urlcsv = dir_path+"/../dataset/nuclear_weapons_tests_states.csv"
    # df_states = pd.read_csv(
    #     urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    # urlcsv = dir_path+"/../dataset/nuclear_weapons_proliferation_owid.csv"
    # df_proliferation = pd.read_csv(
    #     urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()

    # Merge dataframes
    df_merged = pd.merge(pd.merge(df_proliferation, df_stockpiles, on=[
                         'country_name', 'year']), df_tests, on=['country_name', 'year'])

    return "Alexej1", df_merged

@st.cache
def read_data(pathToCsv):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    urlcsv = dir_path+pathToCsv
    csv_data = pd.read_csv(
        urlcsv, index_col=[0, 1], skipinitialspace=True).reset_index()
    
    return csv_data

##### Function
# check whether data is normally distributed
# For checking normality, I used Shapiro-Wilk’s W test which is generally preferred for smaller samples however 
# there are other options like Kolmogorov-Smirnov and D’Agostino and Pearson’s test. 
# Please visit https://docs.scipy.org/doc/scipy/reference/stats.html for more information.
@st.cache
def check_normal_distribution(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")

# check_normal_distribution(sunny_days_san_francisco)
# check_normal_distribution(sunny_day_boston)

get_data()