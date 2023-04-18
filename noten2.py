import pandas as pd

# Input custom functions
import eda_express
import add_year
import exams_total

def read_process_data(years):
    noten_data = {}
    for year in years:
        
        # Construct the file path
        file_path = f"/Users/kamilkarim/neuefische/capstone_project_hh_23_1/data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
        
        # Load the CSV file
        noten = eda_express.read_csv_file(file_path)

        # Add the 'year' column
        noten = add_year.add_year(noten, 'year', year)
        noten_data[year] = noten
        
    return noten_data

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
noten_data = read_process_data(years)