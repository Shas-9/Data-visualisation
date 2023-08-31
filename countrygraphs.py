import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np


# Load CSV file
internet_growth = pd.read_csv('Final.csv')
gdp_growth = pd.read_csv("gdp_growth.csv")

# Select only the desired columns
selected_columns = ['Entity', 'Year', 'Internet Users(%)']

# Filter data for the desired years
start_year = 1990
end_year = 2020

peak_growth_data = []

for country in internet_growth['Entity'].unique():
    internet_growth = internet_growth[(internet_growth['Year'] >= start_year) & (internet_growth['Year'] <= end_year)]
    internet_growth = internet_growth[selected_columns]
    country_internet_data = internet_growth[internet_growth['Entity'] == country]
    country_gdp_data = gdp_growth[gdp_growth['Country Name'] == country]
    country_gdp_data = country_gdp_data.loc[:, f'{start_year}':f'{end_year}']
    country_internet_data["Percentage Increase"] = country_internet_data['Internet Users(%)'].diff()
    peak_gdp = country_gdp_data.max().max()
    year_peak_gdp = country_gdp_data.max().idxmax()
    peak_internet = country_internet_data['Percentage Increase'].max()
    year_peak_internet = country_internet_data.loc[country_internet_data['Percentage Increase'] == peak_internet, 'Year']
    peak_growth_data.append([country, peak_internet, year_peak_internet, peak_gdp, year_peak_gdp])

# Create a new DataFrame
columns = ['country', 'peak internet', 'year peak internet', 'peak gdp', 'year peak gdp']
peak_dataframe = pd.DataFrame(peak_growth_data, columns=columns)

# Save the new DataFrame to a CSV file
peak_dataframe.to_csv('peak_growth_data.csv')
peak_dataframe = peak_dataframe[(peak_dataframe['peak internet'] < 50) & (peak_dataframe['peak gdp'] < 70)]

# Calculate covariance
correlation_coefficient = peak_dataframe['peak gdp'].corr(peak_dataframe['peak internet'])

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(peak_dataframe['peak internet'], peak_dataframe['peak gdp'], alpha=0.7, label='Countries')
plt.xlabel('Peak Internet')
plt.ylabel('Peak GDP')
plt.title('Scatter Plot of Peak Internet vs Peak GDP')

# Add tooltips using mplcursors
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(peak_dataframe['country'].iloc[sel.target.index]))

plt.legend()
plt.grid(True)
plt.show()
print(correlation_coefficient)  # -0.07085753072819657

