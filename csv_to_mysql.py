#!/usr/bin/env python3
import pandas as pd
import mysql.connector
import sqlalchemy
import numpy as np
#Create engine to link our pandas dataframe to our database
'''For clarity: ‘mysql+pymysql’ indicates that I am using mysql as my database management system, and functions within the module pymysql to interface with this database management system (DBMS).
username = dbuser, password =******, hostname = localhost, and database name = tutorial.
'''
engine = sqlalchemy.create_engine('mysql+pymysql://root:broletto@192.168.1.101/tutorial')
#The filename is the csv downloaded from the link in step 2 above
df = pd.read_csv('ANZ.csv')
#Check memory usage of current dataframe
#print(df.shape)
#print(df.dtypes)
#print(df.memory_usage(index=False, deep=True).sum())
#print(df.info())
#Improve memory usage
dfi = pd.read_csv('ANZ.csv',dtype={'status':'string','card_present_flag':'string','bpay_biller_code':'string','account':'string',
                                   'currency':'string','long_lat':'string','txn_description':'string',
                                   'merchant_id':'string','merchant_code':'float','first_name':'string',
                                   'balance':'float','date':'string','gender':'string','age':'int8','merchant_suburb':'string',
                                   'merchant_state':'string','extraction':'string','amount':'float','transaction_id':'string',
                                   'country':'string','customer_id':'string','merchant_long_lat':'string','movement':'string',})
dfi = dfi.replace([np.inf,-np.inf],np.nan)
df2 = dfi.replace(np.nan, '', regex=True)
df2 = df2.rename(columns={"date":"transaction_date"})
df2 = df2.rename(columns={"extraction":"extraction_timestamp"})
df2 = df2.rename(columns={"amount":"transaction_amount"})
df2['merchant_code'] = df2['merchant_code'].replace("",0.0)
#Insert the data to the database using to_sql method.
df2.to_sql(name='financial_data',con=engine, index=False, if_exists='append')
