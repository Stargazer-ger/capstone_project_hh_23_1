import pandas as pd

#input custom functions
import eda_express
import add_year
import exams_total

def load_noten_data(year):
    # Construct the file path
    file_path = f"/Users/kamilkarim/neuefische/capstone_project_hh_23_1/data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    
    # Load the CSV file
    noten_data = eda_express.read_csv_file(file_path)
    
    # Add the 'year' column
    noten_data = add_year.add_year(noten_data, 'year', year)

    # Convert other columns to int data type
    noten_data.iloc[:, 1:] = noten_data.iloc[:, 1:].astype(int)
    
    #noten_data = noten_data.T
    
    #noten_data.iloc[2:, :] = noten_data.iloc[2:, :].astype(int)

    #noten_data = noten_data.T

    return noten_data

# Load data for each year
noten_2010 = load_noten_data(2010)
noten_2011 = load_noten_data(2011)
noten_2012 = load_noten_data(2012)
noten_2013 = load_noten_data(2013)
noten_2014 = load_noten_data(2014)
noten_2015 = load_noten_data(2015)
noten_2016 = load_noten_data(2016)
noten_2017 = load_noten_data(2017)
noten_2018 = load_noten_data(2018)
noten_2019 = load_noten_data(2019)
noten_2020 = load_noten_data(2020)
noten_2021 = load_noten_data(2021)
noten_2022 = load_noten_data(2022)
