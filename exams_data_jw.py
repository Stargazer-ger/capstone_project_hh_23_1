import pandas as pd
import add_year

def load_exams_data(year):
    # Construct the file path
    file_path = f"data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    
    # Read the CSV file
    df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

    # Make a copy of the first 4 rows
    exams_data = df.iloc[0:3].copy()
    
    # Rename the 'Land' column to 'States'
    exams_data = exams_data.rename(columns={'Land': ' '})
    
    # Remove dots from all columns except the first one
    exams_data.iloc[:, 1:] = exams_data.iloc[:, 1:].apply(lambda x: x.str.replace('.', ''))
    
    #convert first column to string
    exams_data.iloc[:, 0] = exams_data.iloc[:, 0].astype(str)

    # Rename names in the States column
    exams_data[' '] = exams_data[' '].replace({'Zahl der PrÃ¼fungen': 'Examinations Total',
                                                     '- bestanden': 'Passed Examinations',
                                                     '- nicht bestanden (abs.)': 'Failed Examinations'})

    # Transposing the dataframe
    exams_data = exams_data.T
    
    # Extract the first row as column headers
    new_header = exams_data.iloc[0]
    
    # Set the first row as column headers
    exams_data.columns = new_header
    
    # Drop the first row from the DataFrame
    exams_data = exams_data[1:]

    # Add the 'year' column
    exams_data = add_year.add_year(exams_data, 'year', year)
    
    # Convert all columns to int data type
    exams_data = exams_data.astype(int)

    # Create a new column with the name from the index
    exams_data['Federal States'] = exams_data.index

    # Replace the index with a default RangeIndex
    exams_data.index = pd.RangeIndex(len(exams_data.index))

    # Rearrange columns to have 'name' as the first column
    exams_data = exams_data[['Federal States'] + exams_data.columns[:-1].tolist()]


    # Convert the 'year' column to datetime format
    exams_data['year'] = pd.to_datetime(exams_data['year'], format='%Y')
    
    return exams_data


# Load data for each year
exams_2010 = load_exams_data(2010)
exams_2011 = load_exams_data(2011)
exams_2012 = load_exams_data(2012)
exams_2013 = load_exams_data(2013)
exams_2014 = load_exams_data(2014)
exams_2015 = load_exams_data(2015)
exams_2016 = load_exams_data(2016)
exams_2017 = load_exams_data(2017)
exams_2018 = load_exams_data(2018)
exams_2019 = load_exams_data(2019)
exams_2020 = load_exams_data(2020)
exams_2021 = load_exams_data(2021)
exams_2022 = load_exams_data(2022)
