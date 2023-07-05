from uszipcode import SearchEngine
import pandas as pd

#CONSTANTS
IL_NUM_OF_ZIPCODES = 1259


def get_population(df):
    #create a search engine
    search = SearchEngine()

    Illinois = search.by_state("il", returns = IL_NUM_OF_ZIPCODES)

    population_dict = dict()
    county_already_found = False

    #for every zipcode get the county name
    for zipcode in Illinois:
        county = zipcode.county.split(" ")[0].lower()

        #only add info if the county is already in the dictionary
        for key in population_dict:
            if key == county and zipcode.population is not None and population_dict[key] is not None:
                population_dict[key] = population_dict[key] + zipcode.population
                county_already_found = True
            
        if not county_already_found:
            population_dict[county] = zipcode.population
        county_already_found = False
    
    #map
    df["Population"] = df["County"].map(population_dict)

    return df


