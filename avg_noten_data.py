import pandas as pd

#input custom functions
import add_year

def load_avg_noten_data(year):
    # Construct the file path
    file_path = f"/Users/kamilkarim/neuefische/capstone_project_hh_23_1/data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    
    # Read the CSV file
    df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

    # Create a copy of the file with specific rows and columns
    noten_data = df.iloc[4:5].copy()
    
    # Rename land to noten
    noten_data.rename(columns={'Land': ' '}, inplace=True)

    # Apply replace method to all columns except the first one
    #noten_data.iloc[:, 1:] = noten_data.iloc[:, 1:].apply(lambda x: x.str.replace('.', ''))

    # Replace commas with dots in selected rows
    noten_data.replace(',', '.', regex=True, inplace=True)
    
    # Transposing the dataframe
    #noten_data = noten_data.T
    
    # Extract the first row as column headers
    #new_header = noten_data.iloc[0]
    
    # Set the first row as column headers
    #noten_data.columns = new_header
    
    # Drop the first row from the DataFrame
    #noten_data = noten_data[1:]


    
    # Create a new column with the name from the index
    #noten_data['Federal States'] = noten_data.index

    # Replace the index with a default RangeIndex
    #noten_data.index = pd.RangeIndex(len(noten_data.index))

    # Rearrange columns to have 'name' as the first column
    #noten_data = noten_data[['Federal States'] + noten_data.columns[:-1].tolist()]

    # Add the 'year' column
    noten_data = add_year.add_year(noten_data, 'year', year)

    # Convert the 'year' column to datetime format
    noten_data['year'] = pd.to_datetime(noten_data['year'], format='%Y', errors='coerce')

    # Rename Notenmittel to AVG Grade
    noten_data.rename(columns={'Notenmittel': 'avg grade'}, inplace=True)

    #Convert average grades to float
    noten_data.iloc[:, 1:17] = noten_data.iloc[:, 1:17].astype(float)

    #Remove Notenmittel
    noten_data[' '] = noten_data[' '].replace({'Notenmittel': ''})


    return noten_data

# Load data for each year
avg_noten_2010 = load_avg_noten_data(2010)
avg_noten_2011 = load_avg_noten_data(2011)
avg_noten_2012 = load_avg_noten_data(2012)
avg_noten_2013 = load_avg_noten_data(2013)
avg_noten_2014 = load_avg_noten_data(2014)
avg_noten_2015 = load_avg_noten_data(2015)
avg_noten_2016 = load_avg_noten_data(2016)
avg_noten_2017 = load_avg_noten_data(2017)
avg_noten_2018 = load_avg_noten_data(2018)
avg_noten_2019 = load_avg_noten_data(2019)
avg_noten_2020 = load_avg_noten_data(2020)
avg_noten_2021 = load_avg_noten_data(2021)
avg_noten_2022 = load_avg_noten_data(2022)
