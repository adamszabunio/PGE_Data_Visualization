#!/usr/bin/env python3
'''
Unzips all zipfiles from `data_out` dir
Based on specified `utility`
Concatenates all publicly available data from 
https://pge-energydatarequest.com/public_datasets
(Quarterly Data from 2013 - 2017)
Returns a concatenated dataframe
ordered by year and month. 
'''
import os
import pandas as pd
from glob import iglob
from zipfile import ZipFile

utility = "Gas" # or "Electric"  

def quarter_check(df):
    '''
    catches error in 2017_Q4 files
    '''
    if (df.month.max() - df.month.min()) > 2:
        fixed_df = df[df.month != 9]
    else:
        return df
    
    return fixed_df

def clean_df(f, utility):
    '''
    inputs: `f`, path to file 
            `utility`, must be either "Gas" or "Electric"
    returns: cleaned DataFrame object 
    '''
    assert utility in ["Gas", "Electric"]
    # normalize column names
    if utility == "Electric":
        cols = ['zip_code', 'month', 'year', 'customer_class', 'combined',
                'total_customers', 'total_kWh', 'average_kWh'] 
    else:
        cols = ['zip_code', 'month', 'year', 'customer_class', 'combined',
                'total_customers', 'total_Thm', 'average_Thm']
    # read in and drop missing data
    df = pd.read_csv(f, names=cols, header=0, thousands=',')
    df.dropna(subset=["zip_code"], inplace=True)
    # keep datatypes consistent across all files 
    d_types = ['int64', 'int64', 'int64', 'object',
               'object', 'int64', 'int64', 'float64']  
    df = df.astype({k: v for k, v in zip(cols, d_types)})
    # quick check for 2017_Q4 data
    df = quarter_check(df)
    
    return df

def dir_check(name):
    '''
    If `name` directory doensn't exist, create it
    Returns `name` to be used as global varable
    '''
    if not os.path.exists(name):
        os.mkdir(name)
    return name
    
# if directories don't exist, create them    
data_out = dir_check("data_out")
unzipped = dir_check(os.path.join(data_out, utility.lower()))
final_data = dir_check("final_data")

# Loop through all data, unzip, and extract only .csv file
for year in range(2013, 2018):
    for quarter in [1,2,3,4]:
        file_name = "PGE_{}_Q{}_{}UsageByZip".format(year, quarter, utility)
        data_in = os.path.join("data_in", file_name+".zip")
        zip_file = ZipFile(data_in)
        zip_file.extract(file_name+".csv", path=unzipped)
        zip_file.close()

# for all unzipped files
files = iglob(os.path.join(unzipped, "*.csv"))
# clean, concatenate, drop dups, sort by year, month, and reset index
all_files = (clean_df(f, utility) for f in files)
all_data = pd.concat(all_files, ignore_index=True)
all_data.drop_duplicates(inplace=True)
all_data.sort_values(["year", "month"], inplace=True)
all_data.reset_index(drop=True, inplace=True)

all_data.to_csv(os.path.join(final_data, utility.lower()+".csv"))