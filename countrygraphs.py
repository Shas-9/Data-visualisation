import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
internet_growth = pd.read_csv('Final.csv')
gdp_growth = pd.read_csv("gdp_growth.csv")

# Select only the desired columns
selected_columns = ['Entity', 'Year', 'Internet Users(%)']

# Filter data for the desired years
start_year = 1990
end_year = 2020

for country in internet_growth['Entity'].unique():
    internet_growth = internet_growth[(internet_growth['Year'] >= start_year) & (internet_growth['Year'] <= end_year)]
    internet_growth = internet_growth[selected_columns]
    country_internet_data = internet_growth[internet_growth['Entity'] == country]
    country_gdp_data = gdp_growth[gdp_growth['Country Name'] == country]
    country_gdp_data = country_gdp_data.loc[:, f'{start_year}':f'{end_year}']
    country_internet_data["Percentage Increase"] = country_internet_data['Internet Users(%)'].diff()
    peak_gdp = country_gdp_data.max().max()
