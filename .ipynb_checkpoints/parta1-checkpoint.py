import pandas as pd
import argparse
import numpy as np
import sys

name = sys.argv[1]
raw_data = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1')
raw_data['total_cases']=raw_data['total_cases'].replace(np.nan, 0)
raw_data['new_cases']=raw_data['new_cases'].replace(np.nan, 0)
raw_data['total_deaths']=raw_data['total_deaths'].replace(np.nan, 0)
raw_data['new_deaths']=raw_data['new_deaths'].replace(np.nan, 0)
data_slice = raw_data.loc[:,['date','location','total_cases','new_cases','total_deaths','new_deaths']]
data_slice['month']=raw_data['date'].apply(lambda x: x[:7])
data_slice['csn_new_cases']=data_slice.groupby(['month','location'])['new_cases'].cumsum() #https://stackoverflow.com/questions/22650833/pandas-groupby-cumulative-sum
data_slice['csn_new_deaths']=data_slice.groupby(['month','location'])['new_deaths'].cumsum() #https://stackoverflow.com/questions/22650833/pandas-groupby-cumulative-sum
data_slice=data_slice[pd.to_datetime(data_slice["date"]).dt.is_month_end] #https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_end.html
final_data=data_slice.loc[:,['location','month','total_cases','csn_new_cases','total_deaths','csn_new_deaths']] 
final_data=final_data.rename(columns={"csn_new_cases": "new_cases", "csn_new_deaths": "new_deaths"})
final_data= final_data[~final_data.month.str.contains("2021")] #https://stackoverflow.com/questions/28679930/how-to-drop-rows-from-pandas-data-frame-that-contains-a-particular-string-in-a-p
final_data.insert(2,'case_fatality_rate',final_data['new_deaths']/final_data['new_cases'])
final_data['case_fatality_rate']=final_data['case_fatality_rate'].replace(np.nan, 0)
final_data.to_csv(name,index=False)
print(final_data.head(5))