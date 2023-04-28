import pandas as pd

#input custom functions
import add_year

def load_teachers_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    
    ###############################################
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

def load_students_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    ###############################################
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

def load_students_per_teacher_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    ###############################################
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


    return students_per_teacher

def load_hours_per_student_data(Year):
    # Construct the file path
    file_path = f'/Users/kamilkarim/neuefische/capstone_project_hh_23_1/testing_data/SKL_Teil_Z_Zusammenfassung_{Year}.xlsx'
    ###############################################
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

    # drop unneeded columns
    hours_per_student.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

    # Add the 'year' column
    hours_per_student = add_year.add_year(hours_per_student, 'Year', Year)

    hours_per_student.rename(columns={'TH': 'Thüringen', 'BW': 'Baden-Wüttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                      'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                      'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz',
                      'SL': 'Saarland', 'SN': 'Sachsen', 'ST': 'Sachsen-Anhalt', 'SH': 'Schleswig-Holstein'}, inplace=True)

    return hours_per_student



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