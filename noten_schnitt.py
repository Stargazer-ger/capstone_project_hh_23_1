import pandas as pd
import add_year

def load_schnitt(year):
    # Construct the file path
    file_path = f"data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    
    # Read the CSV file
    df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

    # Make a copy of the first 4 rows
    schnitt = df.iloc[0:7].copy()



# Load data for each year
exams_2010 = load_schnitt(2010)
exams_2011 = load_schnitt(2011)
exams_2012 = load_schnitt(2012)
exams_2013 = load_schnitt(2013)
exams_2014 = load_schnitt(2014)
exams_2015 = load_schnitt(2015)
exams_2016 = load_schnitt(2016)
exams_2017 = load_schnitt(2017)
exams_2018 = load_schnitt(2018)
exams_2019 = load_schnitt(2019)
exams_2020 = load_schnitt(2020)
exams_2021 = load_schnitt(2021)
exams_2022 = load_schnitt(2022)