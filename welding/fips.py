import pandas as pd

def get_fips(final_df):
    df = pd.read_csv("fips2county.tsv", sep="\t", dtype=str)

    df = df[df["StateAbbr"] == "IL"]

    #get 2 series which we can use to map
    fips = pd.Series(df["CountyFIPS"])
    county = pd.Series([x.lower() for x in df["CountyName"]])

    fips = fips.reset_index(drop=True)
    county = county.reset_index(drop=True)

    #create dictionary
    cleaned_df = pd.DataFrame({"County": county, "FipsID": fips})

    df_dict = cleaned_df.set_index("County")['FipsID'].to_dict()

    #map
    final_df["FipsID"] = final_df["County"].map(df_dict).astype('int64')

    return final_df