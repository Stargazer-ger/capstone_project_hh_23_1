import pandas as pd

def read_csv_file(filepath):
    # Read CSV file with specific parameters
    df = pd.read_csv(filepath, encoding='latin-1', delimiter=';')

    # Make a copy of the first 4 rows
    df_copy = df.iloc[0:3].copy()
    
    # Rename the 'Land' column to 'Numbers'
    df_copy = df_copy.rename(columns={'Land': 'Totals'})
    
    # Remove dots from all columns except the first one
    df_copy.iloc[:, 1:] = df_copy.iloc[:, 1:].apply(lambda x: x.str.replace('.', ''))
    
    #convert first column to string
    df_copy.iloc[:, 0] = df_copy.iloc[:, 0].astype(str)

    # Rename values in the 'Numbers' column
    df_copy['Totals'] = df_copy['Totals'].replace({'Zahl der PrÃ¼fungen': 'Examinations Total',
                                                     '- bestanden': 'Passed Examinations',
                                                     '- nicht bestanden (abs.)': 'Failed Examinations'})
    
    # Convert columns to int data type except first column
    df_copy.iloc[:, 1:] = df_copy.iloc[:, 1:].astype(int)
    

    
    return df_copy