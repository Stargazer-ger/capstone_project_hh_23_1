import pandas as pd

def update_names(df):
    # Define a dictionary to map old names to new names
    name_mapping = {'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                    'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                    'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'NRW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                    'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein',
                    'Nordrhein-Westphalen': 'Nordrhein-Westfalen'}

    # Use the .replace() function to replace old names with new names in the 'Name' column
    df['Federal States'] = df['Federal States'].replace(name_mapping)

    return df



