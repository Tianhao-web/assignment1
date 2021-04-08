import pandas as pd
import argparse
raw_data = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1')
data_slice = raw_data.loc[:,['date','location','total_cases','new_cases','total_deaths','new_deaths']]
data_slice['month']=raw_data['date'].apply(lambda x: x[:7])
data_slice['csn_new_cases']=data_slice.groupby(['month','location'])['new_cases'].cumsum()
data_slice['csn_new_deaths']=data_slice.groupby(['month','location'])['new_deaths'].cumsum()
data_slice=data_slice[pd.to_datetime(data_slice["date"]).dt.is_month_end]
final_data=data_slice.loc[:,['location','month','total_cases','csn_new_cases','total_deaths','csn_new_deaths']]
final_data=final_data.rename(columns={"csn_new_cases": "new_cases", "csn_new_deaths": "new_deaths"})
final_data=final_data.set_index('location')
final_data= final_data[~final_data.month.str.contains("2021")]
final_data['case_fatality_rate']=final_data['total_deaths']/final_data['total_cases']
final_data.head(5)