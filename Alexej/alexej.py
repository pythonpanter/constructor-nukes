##### Find columns which all three datasets share
# nuclear_weapons_proliferation_owid.csv    ---> country_name   year    nuclear_weapons_status  nuclear_weapons_consideration   nuclear_weapons_pursuit     nuclear_weapons_possession
# nuclear_weapons_stockpiles.csv            ---> country_name   year                                                                                                                        nuclear_weapons_stockpile
# nuclear_weapons_tests_states.csv          ---> country_name   year                                                                                                                                                    nuclear_weapons_tests
#
# ---> Conclusion: The columns 'country_name' and 'year' are shared between the three datasets

##### Import modules
import pandas as pd


##### Read in the data
# nuclear_weapons_proliferation_owid.csv
df_proliferation = pd.read_csv('/Users/alexejkhalilzada/Dokumente/Data_Science/SIT_Learning/GroupChallenge/constructor-nukes/dataset/nuclear_weapons_proliferation_owid.csv')
# df_proliferation = pd.read_csv('nuclear_weapons_proliferation_owid.csv', index_col=0)
#df_proliferation = data.sort_values(by=['country_name', 'year'])
#df_proliferation = data.reset_index()

# nuclear_weapons_stockpiles.csv
df_stockpiles = pd.read_csv('/Users/alexejkhalilzada/Dokumente/Data_Science/SIT_Learning/GroupChallenge/constructor-nukes/dataset/nuclear_weapons_stockpiles.csv')

# nuclear_weapons_tests_states.csv
df_states = pd.read_csv('/Users/alexejkhalilzada/Dokumente/Data_Science/SIT_Learning/GroupChallenge/constructor-nukes/dataset/nuclear_weapons_tests_states.csv')

###### Display dataframes
print('* df_proliferation = \n', df_proliferation)
print('* df_stockpiles = \n', df_stockpiles)
print('* df_states = \n', df_states)

##### Merge dataframes
df_merged = pd.merge(pd.merge(df_proliferation,df_stockpiles,on='country_name'),df_states,on='country_name')
df_merged_2 = pd.merge(pd.merge(df_proliferation,df_stockpiles,on=['country_name', 'year']),df_states,on=['country_name', 'year'])
print('* df_merged = \n', df_merged.head(60))
print('* df_merged_2 = \n', df_merged_2.head(60))