#all of the imports
import xarray as xr
import numpy as np
import pandas as pd
from hourly_data import check, api_downloads




def arrange_dfs(entered_df):
    #read in the data
    df = entered_df
    keys = np.arange(len(df))
    df["Keys"] = keys


    #create temporary dataframe and set up keys // subject to change when we figure out what to do with the keys
    df_temporary = df[["Time", "Latitude", "Longitude", "Keys"]]

    return (df, df_temporary)




#create the dictionaries that we will use to map the data
temp_max_dict = {}
temp_min_dict = {}

uwind_max_dict = {}
uwind_min_dict = {}

vwind_max_dict = {}
vwind_min_dict = {}

laihv_max_dict = {}
laihv_min_dict = {}

lailv_max_dict = {}
lailv_min_dict = {}

src_max_dict = {}
src_min_dict = {}

sd_max_dict = {}
sd_min_dict = {}

dicts_list = [temp_max_dict, temp_min_dict, uwind_max_dict, uwind_min_dict,
              vwind_max_dict, vwind_min_dict, laihv_max_dict, laihv_min_dict,
              lailv_max_dict, lailv_min_dict, src_max_dict, src_min_dict,
              sd_max_dict, sd_min_dict]

#variables in netcdf file
variables = ['u10', 'v10', 't2m', 'lai_hv', 'lai_lv', 'src', 'sde']

#for right now we are going to go a month at time // later maybe merge the datasets?

months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
months_strs = [check.get_month(x) for x in months]
years = [2018, 2019, 2020, 2021, 2022]

def looping(df, df_temporary):
    for YEAR in years:
        #loop through each month
        for idx, month in enumerate(months):
            
            if month == 12:
                YEAR -= 1

            #open dataset for that month 
            ds = xr.open_dataset(f"hourly_data/data/{months_strs[idx]}_{YEAR}.nc")
            
            


            #query the dataframe to get just the times we want
            time = f"{YEAR}-{months_strs[idx]}"
            series = df_temporary[df_temporary["Time"] == time]
            
            #if no times, go to next month
            if series.empty:
                if month == 12:
                    YEAR += 1
                continue
            
            
            
            #make it an xarray to query it from the netcdf file
            series_array = series.to_xarray()

            for idx, variable in enumerate(variables):
                #get only temperature
                info = ds[variable]
                
                #create new xarray with only the latitude and longitudes from the dataframe
                info = info.sel(latitude = series_array["Latitude"], longitude = series_array['Longitude'], method = "nearest")
                
                dicts_list[idx*2].update(create_dict(series_array, info, "max"))

                
                
                dicts_list[idx*2 + 1].update(create_dict(series_array, info, "min"))

            if month == 12:
                YEAR += 1
            
            ds.close()

def create_dict(inputs, temp, type):
    
    
    if type == "max":
        #grab the maxes, put them to a dictionary, ansd add it to the larger dict
        maxes = temp.max(dim="time").values

        temps_max_dict = pd.DataFrame({"Keys": inputs["Keys"], 'Temps': maxes}).set_index("Keys")["Temps"].to_dict()

        return temps_max_dict

    if type == "min":
        #same with the mins dict
        mins = temp.min(dim="time").values

        temps_min_dict = pd.DataFrame({"Keys": inputs["Keys"], 'Temps': mins}).set_index("Keys")["Temps"].to_dict()

        return temps_min_dict

    else:
        raise ValueError("Not asking for a min or a max")

variable_pretty_names = ["Maximum Temperature", "Minimum Temperature", "Maximum 10 Meter U Wind", 
                         "Minimum 10 Meter U Wind", "Maximum 10 Meter V Wind", "Minimum 10 Meter V Wind",
                         "Maximum Leaf Area Index High Vegetation", "Minimum Leaf Area Index High Vegetation",
                         "Maximum Leaf Area Index Low Vegetation", "Minimum Leaf Area Index Low Vegetation",
                         "Maximum Skin Reservoir Content", "Minimum Skin Reservoir Content",
                         "Maximum Snow Depth", "Minimum Snow Depth"]
    
def do(df):
    #api_downloads.download()
    df, df_temporary = arrange_dfs(df)
    looping(df, df_temporary)

    for idx, variable in enumerate(variable_pretty_names):
        #map the final dicts to the dataframe and save it to a csv
        df[variable] = df["Keys"].map(dicts_list[idx])

        

    return df

