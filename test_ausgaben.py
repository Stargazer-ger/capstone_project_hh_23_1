import pandas as pd

#input custom functions
import add_year

def load_ausgaben_data(year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/Bildungsausgaben/Ausgaben_{year}.xlsx'
    
    #Extract number of students from  the excel file
    df = pd.read_excel(file_path, sheet_name=f'{year}_1')
    ausgaben_1 = df

    df2 = pd.read_excel(file_path, sheet_name=f'{year}_2')
    ausgaben_2 = df2

    df3 = pd.read_excel(file_path, sheet_name=f'{year}_3')
    ausgaben_3 = df3

    ausgaben_1 = ausgaben_1.rename(columns={ausgaben_1.columns[0]: 'Federal States'})
    ausgaben_2 = ausgaben_2.rename(columns={ausgaben_2.columns[0]: 'Federal States'})
    ausgaben_3 = ausgaben_3.rename(columns={ausgaben_3.columns[0]: 'Federal States'})

    # Add the 'year' column
    ausgaben_3 = add_year.add_year(ausgaben_3, 'year', year)

    # Filter by federal states
    federal_state = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
                'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
                 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
    
    ausgaben_1 = ausgaben_1[ausgaben_1['Federal States'].isin(federal_state)]
    ausgaben_2 = ausgaben_2[ausgaben_2['Federal States'].isin(federal_state)]
    ausgaben_3 = ausgaben_3[ausgaben_3['Federal States'].isin(federal_state)]

    ausgaben_1 = ausgaben_1.rename(columns={ausgaben_1.columns[1]: 'Allg bildende Schulen',
                                               ausgaben_1.columns[2]: 'Berufliche Schulen Insgesamt',
                                               ausgaben_1.columns[3]: 'darunter: im Dualen System',
                                               ausgaben_1.columns[4]: 'Alle Schularten'})

    ausgaben_2 = ausgaben_2.rename(columns={ausgaben_2.columns[1]: 'Grund schulen',
                                               ausgaben_2.columns[2]: 'Hauptschulen',
                                               ausgaben_2.columns[3]: 'Schulen mit mehreren Bildungsgängen',
                                               ausgaben_2.columns[4]: 'Realschulen',
                                               ausgaben_2.columns[5]: 'Gymnasien',
                                               ausgaben_2.columns[6]: 'Integrierte Gesamt schulen'})

    ausgaben_3 = ausgaben_3.rename(columns={ausgaben_3.columns[1]: 'Personalausgaben',
                                               ausgaben_3.columns[2]: 'Laufender Sach-aufwand',
                                               ausgaben_3.columns[3]: 'Investi-tionsaus-gaben',
                                               ausgaben_3.columns[4]: 'Gesamtausgaben',
                                               ausgaben_3.columns[5]: 'darunter: von staatlicher Ebene'})

    #merge the different sheets for each year
    ausgaben = pd.merge(ausgaben_1, ausgaben_2, on="Federal States")
    ausgaben = pd.merge(ausgaben, ausgaben_3, on="Federal States")

    # apply lambda function to remove spaces
    ausgaben.iloc[:, 1:] = ausgaben.iloc[:, 1:].applymap(lambda x: str(x).replace(' ', ''))

    # Replace forward slashes with empty strings
    ausgaben = ausgaben.applymap(lambda x: x.replace('/', '0'))

    # convert all numeric values to float to be able to convert to int
    ausgaben.iloc[:, 1:15] = ausgaben.iloc[:, 1:15].astype('float')

    # Convert the 'year' column to datetime format
    ausgaben['year'] = pd.to_datetime(ausgaben['year'], format='%Y')

    # now convert all to int
    ausgaben.iloc[:, 1:15] = ausgaben.iloc[:, 1:15].astype('Int64')

    return ausgaben


# Load data for ausgaben each year
ausgaben_2010 = load_ausgaben_data(2010)
ausgaben_2011 = load_ausgaben_data(2011)
ausgaben_2012 = load_ausgaben_data(2012)
ausgaben_2013 = load_ausgaben_data(2013)
ausgaben_2014 = load_ausgaben_data(2014)
ausgaben_2015 = load_ausgaben_data(2015)
ausgaben_2016 = load_ausgaben_data(2016)
ausgaben_2017 = load_ausgaben_data(2017)
ausgaben_2019 = load_ausgaben_data(2019)

ausgaben_concat = pd.concat([ausgaben_2010 ,ausgaben_2011, ausgaben_2012,
                             ausgaben_2013, ausgaben_2014, ausgaben_2015,
                             ausgaben_2016, ausgaben_2017, ausgaben_2019],
                             ignore_index=False)