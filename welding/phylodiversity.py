import pandas as pd

def get_phylo(df):
    bird = pd.read_csv("avi_phylodiv_wnv_041822.csv")

    #create series
    fips = pd.Series(bird["STCO_FIPS"])
    phylo = pd.Series(bird["PD"])

    #create dictionary
    temp_df = pd.DataFrame({"FipsID": fips, "Phylodiversity": phylo})

    df_dict = temp_df.set_index("FipsID")['Phylodiversity'].to_dict()

    #map
    df["Phylodiversity"] = df["FipsID"].map(df_dict)


    return df