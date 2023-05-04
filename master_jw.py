import pandas as pd

#input custom functions
import add_year

def load_teachers_data(Year):
    # Construct the file path
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    # Path Johannes '/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Realativ path 'testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Original Kamil Path '/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
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
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'

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
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
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
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'

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
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/Bildungsausgaben/Ausgaben_{year}.xlsx'
    
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
                             ausgaben_2016, ausgaben_2017, ausgaben_2019],
                             ignore_index=False)



#####################################

# Veränderung für Vorschulen und den zusammenhang zum Educations Level

def load_preschool(Year):
    # Construct the file path
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    # Path Johannes '/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Realativ path 'testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Original Kamil Path '/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
    #Extract number of students from  the excel file
    df5 = pd.read_excel(file_path, sheet_name='Z5.2', header=4) #, skipfooter =)

    # Make a copy
    preschool = df5.copy()

    # Rename columns
    preschool = preschool.rename(columns={'D': 'Deutschland'}) #, preschool.columns[1]: 'SchoolType'})

    # Filter by school types
    # school_types = ['Allgemein bildende Schulen', 'Sekundarbereich I', 'Sekundarbereich II', 
    #                'Allgemeinbildende Schulen', 'Sekundarstufe I', 'Sekundarstufe II']
    # teachers = teachers[teachers['SchoolType'].isin(school_types)]

    # drop unneeded columns
    preschool.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    preschool = add_year.add_year(preschool, 'Year', Year)

    # Rename the columns 
    preschool.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)
    
    return preschool


# Load data for preschool each year

preschool_2011 = load_preschool(2011)
preschool_2012 = load_preschool(2012)
preschool_2013 = load_preschool(2013)
preschool_2014 = load_preschool(2014)
preschool_2015 = load_preschool(2015)
preschool_2016 = load_preschool(2016)
preschool_2017 = load_preschool(2017)
preschool_2018 = load_preschool(2018)
preschool_2019 = load_preschool(2019)
preschool_2020 = load_preschool(2020)
preschool_2021 = load_preschool(2021)


def load_abschluss(Year):
    # Construct the file path
    file_path = f'/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    # Path Johannes '/Users/jw/Documents/Neue_Fische_Bootcamp/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Realativ path 'testing_data/SKL_Teil_Z_Zusammenfassung_2011.xlsx'
    # Original Kamil Path '/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
    #Extract number of students from  the excel file
    df6 = pd.read_excel(file_path, sheet_name='Z10.2', header=4) #, skipfooter =)

    # Make a copy
    abschluss = df6.copy()

    # Rename columns
    abschluss = abschluss.rename(columns={'D': 'Deutschland', abschluss.columns[1]: 'SchoolType'})

    # Filter by school types
    #school_types = ['Abgänger nach Beendigung der Vollzeitschulpflicht ohne Hauptschulabschluss', 'Absolventen nach Beendigung der Vollzeitschulpflicht mit Hauptschulabschluss', 'Absolventen mit mittlerem Abschluss und entsprechenden Abschlüssen', 
    #                'Absolventen mit Hochschul- und Fachhochschulreife', 'Abgänger/-innen nach Beendigung der Vollzeitschulpflicht ohne Hauptschulabschluss', 'Absolventen/-innen nach Beendigung der Vollzeitschulpflicht mit Hauptschulabschluss', 'Absolventen/-innen mit mittlerem Abschluss und entsprechenden Abschlüssen', 'Absolventen/-innen mit Hochschul- und Fachhochschulreife', 'Abgehende nach Beendigung der Vollzeitschulpflicht ohne Hauptschulabschluss', 'Absolvierende nach Beendigung der Vollzeitschulpflicht mit Hauptschulabschluss', 'Absolvierende mit mittlerem Abschluss und entsprechenden Abschlüssen', 'Absolvierende mit Hochschul- und Fachhochschulreife']
    #abschluss = abschluss[abschluss['SchoolType'].isin(school_types)]

    # drop unneeded columns
    abschluss.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    abschluss = add_year.add_year(abschluss, 'Year', Year)

    # Rename the columns 
    abschluss.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)
    

    return abschluss


# Load data for abschluss each year

abschluss_2011 = load_abschluss(2011)
abschluss_2012 = load_abschluss(2012)
abschluss_2013 = load_abschluss(2013)
abschluss_2014 = load_abschluss(2014)
abschluss_2015 = load_abschluss(2015)
abschluss_2016 = load_abschluss(2016)
abschluss_2017 = load_abschluss(2017)
abschluss_2018 = load_abschluss(2018)
abschluss_2019 = load_abschluss(2019)
abschluss_2020 = load_abschluss(2020)
abschluss_2021 = load_abschluss(2021)