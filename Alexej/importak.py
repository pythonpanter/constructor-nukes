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
from scipy import stats

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

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    
    path_to_stockpiles = "/../dataset/nuclear_weapons_stockpiles.csv"
    path_to_tests = "/../dataset/nuclear_weapons_tests_states.csv"
    path_to_proliferation = "/../dataset/nuclear_weapons_proliferation_owid.csv"
    
    df_stockpiles = read_data(path_to_stockpiles)
    df_tests = read_data(path_to_tests)
    df_proliferation = read_data(path_to_proliferation)
    
    # Debug Output
    print(df_stockpiles)
    print(df_tests)
    print(df_proliferation)
    
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


##### Get data and continue with following tests:
# Shapiro-Wilk's W test --> Is data normally distributed?
# 
get_data() # let's grab the available data

merged_df = get_data()
merged_df = merged_df[1]
print('* merged_df = .......\n', merged_df)
print(len(merged_df))

alpha = 0.05 # p value

##### Assumption Check
# H₀: The data is normally distributed.
# H₁: The data is not normally distributed.
# α=0.05. If the p-value is >0.05, it can be said that data is normally distributed.

# check whether data is normally distributed
# For checking normality, I used Shapiro-Wilk’s W test which is generally preferred for smaller samples however 
# there are other options like Kolmogorov-Smirnov and D’Agostino and Pearson’s test. 
# Please visit https://docs.scipy.org/doc/scipy/reference/stats.html for more information.
def check_normal_distribution(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")

check_normal_distribution(sunny_days_san_francisco)
check_normal_distribution(sunny_day_boston)

##### Function
# Levene's test
# For checking variance homogeneity, I preferred Levene’s test but you can also check Bartlett’s test 
# from here: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bartlett.html#scipy.stats.bartlett
def check_variance_homogeneity(sunny_days_san_francisco, sunny_day_boston):
    test_stat_var, p_value_var= stats.levene(sunny_days_san_francisco,sunny_day_boston)
    print("p value:%.4f" % p_value_var)
    if p_value_var <0.05:
        print("Reject null hypothesis >> The variances of the samples are different.")
    else:
        print("Fail to reject null hypothesis >> The variances of the samples are same.")

# check_variance_homogeneity(sunny_days_san_francisco, sunny_day_boston)

##### Since assumptions are satisfied, we can perform the parametric version of the test for 2 groups

##### Calculate t-score and test the hypothesis with alpha=0.05 Assume that all variables are normally distributed. Do not make any assumptions about the variance.
#
# ttest,p_value = stats.ttest_ind(sunny_days_san_francisco,sunny_day_boston)
print("p value:%.8f" % p_value)
print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
if p_value/2 <0.05:
    print("\nDo: --->  Reject null hypothesis")
else:
    print("\nDo: ---> Fail to reject null hypothesis")

