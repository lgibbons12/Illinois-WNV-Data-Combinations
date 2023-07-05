Welcome!

This repository houses all of the code used in my project of getting Illinois data to study the West Nile Virus. 

**Welding:**

The "welding" folder houses code that "welds" together multiple dataframes. It takes the original WNV data and adds in extra data coming from other dataframes!

The main file goes through each file in order and runs its main function. Each main function takes the external dataframe and puts the data into a dictionary with county names. Then, that dictionary is mapped to the growing dataframe to create a new column. With each successive file, more data is added, welding together all of the dataframes.

---
**Monthly Data:**

The "monthly_data" folder houses code that uses monthly weather data downloaded from Copernicus and maps it to the existing dataframe

The "final.py" file downloads the climate data from the "download.nc" file, and then uses xarray to comb through it. For each of four different variables, xarray selects the the data, and maps it to each row's latitude, longitude, and time data. This mapping corresponds to a key for each row, which is then used to map the new data to the growing dataframe.

---
**Hourly Data:**

The "hourly_data" folder connects to the CDSAPI to get hourly data for Illinois, and then scans through all of it and adds the extreme values for each variable to the existing dataframe!

The "extremes.py" file first downloads all of the hourly data from the CDSAPI, and then it creates dictionaries for the maximums and minimums for each variable. The code then loops through each dataset that was downloaded and selects the maximum and minimum values for each key from the exisiting dataset, and adds it to a dictionary. Once all of the dictionaries are finished, the file maps all of the dictionaries to the growing dataset.

---
Finally, pandas stitches it all together and produces one formatted and complete dataframe that is ready for analysis.
