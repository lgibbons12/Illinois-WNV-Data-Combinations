#imports
import pandas as pd

#get dataset

def get_latlng(df):

    #clean up county seats data
    county_seats = pd.read_csv("USA_county_seats.csv", skipinitialspace=True)
    county_seats = county_seats[county_seats["State_Code"] == "IL"]
    county_seats = county_seats.iloc[:, 1:]
    county_seats["County"] = [x.lower() for x in county_seats["County"]]

    #map the latitude
    lat_keys = pd.Series(county_seats["Latitude"].values, index = county_seats['County']).to_dict()

    df["Latitude"] = df["County"].map(lat_keys)


    #map the longitutde
    lng_keys = pd.Series(county_seats["Longitude"].values, index = county_seats['County']).to_dict()

    df["Longitude"] = df["County"].map(lng_keys)


    #save to csv
    return df