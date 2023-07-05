from welding import count_seat, fips, latlng, phylodiversity, population
import pandas as pd
from monthly_data import final
from hourly_data import extremes
import time_add
df = pd.read_csv("illinois_county_level_data_2018_2022_combine.csv")


def weld_dataframes(df):
    df = count_seat.add_seats(df)
    df = latlng.get_latlng(df)
    df = population.get_population(df)
    df = fips.get_fips(df)
    df = phylodiversity.get_phylo(df)

    return df


df = weld_dataframes(df)

df = time_add.add_time(df)

df = final.do(df)
 

df = extremes.do(df)

df.drop("keys", inplace = True, axis = 1)

df.drop("Keys", inplace = True, axis = 1)
df.to_csv("output.csv", index=False)


