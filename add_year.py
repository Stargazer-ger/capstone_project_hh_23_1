def add_year(df, year, column_value):
    # Add a new column with specified name and value
    df[year] = column_value

    return df