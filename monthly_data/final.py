#imports
import pandas as pd
import numpy as np
import xarray as xr
from monthly_data import create_new_df as cnd

def do(entered_df):
    #get all the data
    ds = xr.open_dataset("monthly_data/download.nc")
    df = entered_df
    new_df = cnd.new_df(entered_df)
    keys = np.arange(len(df))
    df['Keys'] = keys

    #format the data into xarray and take out the nulls of ds
    inputs = new_df.to_xarray()
    ds = ds.sel(expver = 1)

    list = ["t2m", "tp", "lai_hv", "lai_lv"]
    def return_the_four(entered):
        temp = ds[entered]

        selected_values = temp.sel(time = inputs['Time'], latitude = inputs['Latitude'], longitude = inputs['Longitude'], method="nearest")
        

        cleaned_info = pd.DataFrame({"keys": keys, entered: selected_values.values})
        df_dict = cleaned_info.set_index("keys")[entered].to_dict()

        df[entered] = df["keys"].map(df_dict)
        df.drop("Keys", axis=1)

    for var in list:
        return_the_four(var)

    return df

