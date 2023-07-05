import pandas as pd
from datetime import datetime

def add_time(df):
    # Assuming you have a DataFrame named df with 'Year' and 'Month' columns
    df = df
    # Define a function to convert year and month to a formatted date string
    def format_date(row):
        year = row['Year']
        month = row['Month']
        date_obj = datetime.strptime(f'{year}-{month}', '%Y-%m')
        return date_obj.strftime('%Y-%m')

    # Apply the function to create the 'times' column
    df['Time'] = df.apply(format_date, axis=1)

    return df
