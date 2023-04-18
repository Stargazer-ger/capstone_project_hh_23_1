import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

#input custom functions
import eda_express
import add_year
import exams_total

# noten 2010
noten_2010 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2010/Noten-Table 1.csv')
noten_2010 = add_year.add_year(noten_2010, 'year', 2010)

# noten 2011
noten_2011 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2011/Noten-Table 1.csv')
noten_2011 = add_year.add_year(noten_2011, 'year', 2011)

# noten 2012
noten_2012 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2012/Noten-Table 1.csv')
noten_2012 = add_year.add_year(noten_2011, 'year', 2012)

# noten 2013
noten_2013 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2013/Noten-Table 1.csv')
noten_2013 = add_year.add_year(noten_2013, 'year', 2013)

# noten 2014
noten_2014 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2014/Noten-Table 1.csv')
noten_2014 = add_year.add_year(noten_2014, 'year', 2014)

# noten 2016
noten_2015 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2015/Noten-Table 1.csv')
noten_2015 = add_year.add_year(noten_2015, 'year', 2015)

# noten 2016
noten_2016 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2016/Noten-Table 1.csv')
noten_2016 = add_year.add_year(noten_2016, 'year', 2016)

# noten 2017
noten_2017 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2017/Noten-Table 1.csv')
noten_2017 = add_year.add_year(noten_2017, 'year', 2017)

# noten 2018
noten_2018 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2018/Noten-Table 1.csv')
noten_2018 = add_year.add_year(noten_2018, 'year', 2018)

# noten 2019
noten_2019 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2019/Noten-Table 1.csv')
noten_2019 = add_year.add_year(noten_2019, 'year', 2019)

# noten 2020
noten_2020 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2020/Noten-Table 1.csv')
noten_2020 = add_year.add_year(noten_2020, 'year', 2020)

# noten 2021
noten_2021 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2021/Noten-Table 1.csv')
noten_2021 = add_year.add_year(noten_2021, 'year', 2021)

# noten 2022
noten_2022 = eda_express.read_csv_file('./data/Converted to CSV/Aus_Abiturnoten_2022/Noten-Table 1.csv')
noten_2022 = add_year.add_year(noten_2022, 'year', 2022)