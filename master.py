import pandas as pd

#input custom functions
import add_year
import update_states_name

def load_teachers_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
    #Extract number of students from  the excel file
    df = pd.read_excel(file_path, sheet_name='Z3.2', header=4) #, skipfooter =)

    # Make a copy
    teachers = df.copy()

    # Rename columns
    teachers = teachers.rename(columns={'D': 'Deutschland', teachers.columns[1]: 'SchoolType'})

    # Filter by school types
    school_types = ['Allgemein bildende Schulen', 'Sekundarbereich I', 'Sekundarbereich II', 
                    'Allgemeinbildende Schulen', 'Sekundarstufe I', 'Sekundarstufe II']
    teachers = teachers[teachers['SchoolType'].isin(school_types)]

    # drop unneeded columns
    teachers.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    teachers = add_year.add_year(teachers, 'Year', Year)

    # Rename the columns 
    teachers.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)
    return teachers

###############################################

def load_students_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'

    #Extract number of students from  the excel file
    df1 = pd.read_excel(file_path, sheet_name='Z1.2', header=4) #, skipfooter =)

    # Make a copy
    students = df1.copy()

    # Rename columns
    students = students.rename(columns={'D': 'Deutschland', students.columns[1]: 'SchoolType'})

    # Filter by school types
    school_types = ['Allgemein bildende Schulen', 'Sekundarbereich I', 'Sekundarbereich II', 
                    'Allgemeinbildende Schulen', 'Sekundarstufe I', 'Sekundarstufe II']
    students = students[students['SchoolType'].isin(school_types)]

    # drop unneeded columns
    students.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    students = add_year.add_year(students, 'Year', Year)

    # Rename the columns 
    students.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)

    return students

###############################################

def load_students_per_teacher_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
    #Extract number of students from  the excel file
    df2 = pd.read_excel(file_path, sheet_name='Z6.2 ', header=4) #, skipfooter =)

    # Make a copy
    students_per_teacher = df2.copy()

    # Rename columns
    students_per_teacher = students_per_teacher.rename(columns={'D': 'Deutschland', students_per_teacher.columns[1]: 'SchoolType'})

    # Filter by school types
    school_types = ['Allgemein bildende Schulen', 'Sekundarbereich I', 'Sekundarbereich II', 
                    'Allgemeinbildende Schulen', 'Sekundarstufe I', 'Sekundarstufe II']
    students_per_teacher = students_per_teacher[students_per_teacher['SchoolType'].isin(school_types)]

    # drop unneeded columns
    students_per_teacher.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    students_per_teacher = add_year.add_year(students_per_teacher, 'Year', Year)

    students_per_teacher.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)
    # Convert the 'year' column to datetime format
    students_per_teacher['Year'] = pd.to_datetime(students_per_teacher['Year'], format='%Y')
    return students_per_teacher

###############################################

def load_hours_per_student_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'

    #Extract number of students from  the excel file
    df3 = pd.read_excel(file_path, sheet_name='Z7.2', header=4) #, skipfooter =)

    # Make a copy
    hours_per_student = df3.copy()

    # Rename columns
    hours_per_student = hours_per_student.rename(columns={'D': 'Deutschland', hours_per_student.columns[1]: 'SchoolType'})

    # Filter by school types
    school_types = ['Allgemein bildende Schulen', 'Sekundarbereich I', 'Sekundarbereich II', 
                    'Allgemeinbildende Schulen', 'Sekundarstufe I', 'Sekundarstufe II', 'Förderschulen']
    hours_per_student = hours_per_student[hours_per_student['SchoolType'].isin(school_types)]

    # replacing some names to have consistency
    name_mapping = {'Sekundarbereich I': 'Sekundarstufe I',
                    'Sekundarbereich II':'Sekundarstufe I',
                    'Allgemein bildende Schulen':'Allgemeinbildende Schulen'}

    # Use the .replace() function to replace old names with new names
    hours_per_student['SchoolType'] = hours_per_student['SchoolType'].replace(name_mapping)

    # drop unneeded columns
    hours_per_student.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    hours_per_student = add_year.add_year(hours_per_student, 'Year', Year)

    hours_per_student.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)
    return hours_per_student

###############################################

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
    ausgaben.iloc[:, 1:] = ausgaben.iloc[:, 1:].applymap(lambda x: x.replace('-', '0'))

    # convert all numeric values to float to be able to convert to int
    ausgaben.iloc[:, 1:15] = ausgaben.iloc[:, 1:15].astype('float')

    # Convert the 'year' column to datetime format
    ausgaben['year'] = pd.to_datetime(ausgaben['year'], format='%Y')

    # now convert all to int
    ausgaben.iloc[:, 1:15] = ausgaben.iloc[:, 1:15].astype('Int64')
    return ausgaben


def load_exams_data(year):
    # Construct the file path
    file_path = f"/Users/kamilkarim/neuefische/capstone_project_hh_23_1/data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    
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


def load_noten_data(year):
    # Construct the file path
    file_path = f"/Users/kamilkarim/neuefische/capstone_project_hh_23_1/data/Converted to CSV/Aus_Abiturnoten_{year}/Noten-Table 1.csv"
    # Read the CSV file
    df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

    # Create a copy of the file with specific rows and columns
    noten_data = df.iloc[6:].copy()
    
    # Rename land to noten
    noten_data.rename(columns={'Land': ' '}, inplace=True)

    # Apply replace method to all columns except the first one
    noten_data.iloc[:, 1:] = noten_data.iloc[:, 1:].apply(lambda x: x.str.replace('.', ''))

    # Replace commas with dots in selected rows
    noten_data.replace(',', '.', regex=True, inplace=True)
    
    # Transposing the dataframe
    noten_data = noten_data.T
    
    # Extract the first row as column headers
    new_header = noten_data.iloc[0]
    
    # Set the first row as column headers
    noten_data.columns = new_header
    
    # Drop the first row from the DataFrame
    noten_data = noten_data[1:]

    # Add the 'year' column
    noten_data = add_year.add_year(noten_data, 'year', year)
    
    #Convert other columns to int data type
    noten_data.iloc[:, 0:] = noten_data.iloc[:, 0:].astype(int)

    # Create a new column with the name from the index
    noten_data['Federal States'] = noten_data.index

    # Replace the index with a default RangeIndex
    noten_data.index = pd.RangeIndex(len(noten_data.index))

    # Rearrange columns to have 'name' as the first column
    noten_data = noten_data[['Federal States'] + noten_data.columns[:-1].tolist()]

    # Convert the 'year' column to datetime format
    noten_data['year'] = pd.to_datetime(noten_data['year'], format='%Y')

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

# Load data for teachers each year
teachers_2011 = load_teachers_data(2011)
teachers_2012 = load_teachers_data(2012)
teachers_2013 = load_teachers_data(2013)
teachers_2014 = load_teachers_data(2014)
teachers_2015 = load_teachers_data(2015)
teachers_2016 = load_teachers_data(2016)
teachers_2017 = load_teachers_data(2017)
teachers_2018 = load_teachers_data(2018)
teachers_2019 = load_teachers_data(2019)
teachers_2020 = load_teachers_data(2020)
teachers_2021 = load_teachers_data(2021)

# Load data for students each year
students_2011 = load_students_data(2011)
students_2012 = load_students_data(2012)
students_2013 = load_students_data(2013)
students_2014 = load_students_data(2014)
students_2015 = load_students_data(2015)
students_2016 = load_students_data(2016)
students_2017 = load_students_data(2017)
students_2018 = load_students_data(2018)
students_2019 = load_students_data(2019)
students_2020 = load_students_data(2020)
students_2021 = load_students_data(2021)

# Load data for students_per_teacher each year
students_per_teacher_2011 = load_students_per_teacher_data(2011)
students_per_teacher_2012 = load_students_per_teacher_data(2012)
students_per_teacher_2013 = load_students_per_teacher_data(2013)
students_per_teacher_2014 = load_students_per_teacher_data(2014)
students_per_teacher_2015 = load_students_per_teacher_data(2015)
students_per_teacher_2016 = load_students_per_teacher_data(2016)
students_per_teacher_2017 = load_students_per_teacher_data(2017)
students_per_teacher_2018 = load_students_per_teacher_data(2018)
students_per_teacher_2019 = load_students_per_teacher_data(2019)
students_per_teacher_2020 = load_students_per_teacher_data(2020)
students_per_teacher_2021 = load_students_per_teacher_data(2021)

# Load data for hours_per_student each year
hours_per_student_2011 = load_hours_per_student_data(2011)
hours_per_student_2012 = load_hours_per_student_data(2012)
hours_per_student_2013 = load_hours_per_student_data(2013)
hours_per_student_2014 = load_hours_per_student_data(2014)
hours_per_student_2015 = load_hours_per_student_data(2015)
hours_per_student_2016 = load_hours_per_student_data(2016)
hours_per_student_2017 = load_hours_per_student_data(2017)
hours_per_student_2018 = load_hours_per_student_data(2018)
hours_per_student_2019 = load_hours_per_student_data(2019)
hours_per_student_2020 = load_hours_per_student_data(2020)
hours_per_student_2021 = load_hours_per_student_data(2021)

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
ausgaben_2020 = load_ausgaben_data(2020)
ausgaben_2021 = load_ausgaben_data(2021)


teachers_concat = pd.concat([  teachers_2011, teachers_2012, teachers_2013,
                            teachers_2014, teachers_2015, teachers_2016,
                            teachers_2017, teachers_2018, teachers_2019,
                            teachers_2020, teachers_2021], ignore_index=True)

students_concat = pd.concat([students_2011, students_2012, students_2013, students_2014,
                             students_2015, students_2016, students_2017, students_2018,
                             students_2019, students_2020, students_2021], ignore_index=True)

students_per_teacher_concat = pd.concat([students_per_teacher_2011, students_per_teacher_2012, students_per_teacher_2013,
                             students_per_teacher_2014, students_per_teacher_2015, students_per_teacher_2016,
                             students_per_teacher_2017, students_per_teacher_2018, students_per_teacher_2019,
                             students_per_teacher_2020, students_per_teacher_2021], ignore_index=True)

hours_per_student_concat = pd.concat([hours_per_student_2011, hours_per_student_2012, hours_per_student_2013,
                            hours_per_student_2014, hours_per_student_2015, hours_per_student_2016,
                            hours_per_student_2017, hours_per_student_2018, hours_per_student_2019,
                            hours_per_student_2020, hours_per_student_2021], ignore_index=True)

ausgaben_concat = pd.concat([ausgaben_2010 ,ausgaben_2011, ausgaben_2012,
                             ausgaben_2013, ausgaben_2014, ausgaben_2015,
                             ausgaben_2016, ausgaben_2017, ausgaben_2019,
                             ausgaben_2020, ausgaben_2021],
                             ignore_index=False)

exams_concat = pd.concat([exams_2010, exams_2011, exams_2012,
                          exams_2013, exams_2014, exams_2015,
                          exams_2016, exams_2017, exams_2018,
                          exams_2019, exams_2020, exams_2021,
                          exams_2022
                          ], ignore_index=True)
exams_concat = update_states_name.update_names(exams_concat)

noten_concat = pd.concat([noten_2010, noten_2011, noten_2012,
                          noten_2013, noten_2014, noten_2015,
                          noten_2016, noten_2017, noten_2018,
                          noten_2019, noten_2020, noten_2021,
                          noten_2022
                          ], ignore_index=True)