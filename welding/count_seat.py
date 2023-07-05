import pandas as pd


def add_seats(df):
    df["Year"] = df["Year"].astype('int64')
    county_seats = pd.read_csv("USA_county_seats.csv", skipinitialspace=True)

    county_seats = county_seats[county_seats["State_Code"] == "IL"]
    county_seats = county_seats.iloc[:, 1:]
    county_seats["County"] = [x.lower() for x in county_seats["County"]]

    seat_keys = pd.Series(county_seats["County_Seat"].values, index = county_seats['County']).to_dict()

    df['County Seats'] = df["County"].map(seat_keys)

    return df