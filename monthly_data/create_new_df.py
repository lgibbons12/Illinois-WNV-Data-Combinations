
import pandas as pd
import numpy as np

#creates new dataframe with keys
def new_df(entered_df):
    df = entered_df
    keys = np.arange(len(df))
    df['keys'] = keys
    new_df = pd.DataFrame()
    new_df['Latitude'] = df['Latitude']
    new_df['Longitude'] = df['Longitude']
    new_df['Time'] = df['Time']
    keys = np.arange(len(new_df))
    new_df['keys'] = keys
    return new_df