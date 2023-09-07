import pandas as pd
import matplotlib.pyplot as plt

gdp_per_capita = pd.read_csv('gdp_per_capita.csv')
internet_growth = pd.read_csv('Final.csv')

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
    country_gdp_data = gdp_per_capita[gdp_per_capita['Country Name'] == country]
    country_gdp_data = country_gdp_data.loc[:, f'{start_year}':f'{end_year}']
    country_internet_data["Percentage Increase"] = country_internet_data['Internet Users(%)'].diff()
    peak_gdp = country_gdp_data.max().max()
    year_peak_gdp = country_gdp_data.max().idxmax()
    peak_internet = country_internet_data['Percentage Increase'].max()
    year_peak_internet = country_internet_data.loc[
        country_internet_data['Percentage Increase'] == peak_internet, 'Year']
    peak_growth_data.append([country, peak_internet, year_peak_internet, peak_gdp, year_peak_gdp])

# Create a new DataFrame
columns = ['country', 'peak internet', 'year peak internet', 'peak gdp', 'year peak gdp']
peak_dataframe = pd.DataFrame(peak_growth_data, columns=columns)

# Save the new DataFrame to a CSV file
peak_dataframe.to_csv('peak_growth_data.csv')
peak_dataframe = peak_dataframe[(peak_dataframe['peak internet'] < 50) & (peak_dataframe['peak gdp'] < 70)]

print(peak_dataframe)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(peak_dataframe['year peak gdp'], peak_dataframe['peak gdp'], color='blue')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Peak GDP')
plt.title('Peak GDP over the years')

plt.show()
