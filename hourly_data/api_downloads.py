import cdsapi
from hourly_data import check
import os

c = cdsapi.Client()

def download():
    
    counter = 0

    months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    years = [2018, 2019, 2020, 2021, 2022]
    for YEAR in years:
        for i, month in enumerate(months):
            
            if month == 12:
                YEAR -= 1
            month_str = check.get_month(month)
            
            counter += 1
            retrieve(YEAR, month_str, month)
            
            
            percent = round(counter / 60, 3) * 100
            print(f"*********************************       {percent}% DONE!          *********************************")
            if month == 12:
                YEAR += 1
    
   
            

def retrieve(YEAR, month_str, month):
    if month < 0 or month > 12:
        raise ValueError("Incorrect month")
    if int(month_str) != month:
        raise ValueError("Month string and month do not equal each other")
    c.retrieve(
                'reanalysis-era5-land',
                {
                    'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
            'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'skin_reservoir_content',
            'snow_depth',
        ],
                    'year': str(YEAR),
                    'month': month_str,
                    'day': check.days_check(month, YEAR),
                    'time': [
                        '05:00', '15:00',
                    ],
                    'area': [
                        43, -92, 37,
                            -87,
                    ],
                    'format': 'netcdf',
                },
                'download.nc')
    
    os.rename("download.nc", f"hourly_data/data/{month_str}_{YEAR}.nc")

if __name__ == "__main__":
    download()
