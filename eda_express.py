import pandas as pd

def read_csv_file(filepath):
    # Read CSV file with specific parameters
    df = pd.read_csv(filepath, encoding='latin-1', delimiter=';')
    
   # Create a copy of the file with specific rows and columns
    df_copy = df.iloc[6:].copy()
    
    # Rename land to noten
    df_copy.rename(columns={'Land': 'Noten'}, inplace=True)

    # Apply replace method to all columns except the first one
    df_copy.iloc[:, 1:] = df_copy.iloc[:, 1:].apply(lambda x: x.str.replace('.', ''))

    # Replace commas with dots in selected rows
    df_copy.replace(',', '.', regex=True, inplace=True)

    # Convert first column to float data type
    df_copy.iloc[:, 0] = df_copy.iloc[:, 0].astype(float)

    # Convert other columns to int data type
    df_copy.iloc[:, 1:] = df_copy.iloc[:, 1:].astype(int)

    return df_copy
