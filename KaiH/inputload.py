
import pandas as pd

def test():
    print('hi')
    return


def get_data():
    key='InternetUsage'
    df=pd.read_csv('share-of-individuals-using-the-internet.csv')
    df.rename(columns={'Individuals using the Internet (% of population)':'Percentage','Entity':'Country'}, inplace=True)
    return (key,df)