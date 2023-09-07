import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

# Load CSV file
internet_growth = pd.read_csv('Final.csv')
gdp_growth = pd.read_csv("gdp_growth.csv")
gdp_per_capita = pd.read_csv('gdp_per_capita.csv')

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
    capita_data = gdp_per_capita[gdp_per_capita['Country Name'] == country]['2020']
    if not capita_data.empty:
        capita_data = capita_data.iloc[0]
    else:
        capita_data = 0
    country_internet_data["Percentage Increase"] = country_internet_data['Internet Users(%)'].diff()
    peak_gdp = country_gdp_data.max().max()
    year_peak_gdp = country_gdp_data.max().idxmax()
    peak_internet = country_internet_data['Percentage Increase'].max()
    year_peak_internet = country_internet_data.loc[
        country_internet_data['Percentage Increase'] == peak_internet, 'Year']
    if not year_peak_internet.empty:
        year_peak_internet = year_peak_internet.iloc[0]
    else:
        year_peak_internet = 0
    peak_growth_data.append([country, peak_internet, year_peak_internet, peak_gdp, year_peak_gdp, capita_data])


# Create a new DataFrame
columns = ['country', 'peak internet', 'year peak internet', 'peak gdp', 'year peak gdp', 'current capita']
peak_dataframe = pd.DataFrame(peak_growth_data, columns=columns)
print(peak_dataframe.dtypes)

# Save the new DataFrame to a CSV file
peak_dataframe.to_csv('peak_growth_data.csv')
peak_dataframe = peak_dataframe[(peak_dataframe['peak internet'] < 50) & (peak_dataframe['peak gdp'] < 70)]

# Convert the 'year peak gdp' column to integers
peak_dataframe.fillna(0)
peak_dataframe['year peak internet'] = peak_dataframe['year peak internet'].astype(int)
# peak_dataframe['current capita'] = peak_dataframe['current capita'].astype(int)

# Sort the DataFrame by the 'Year' column
peak_dataframe = peak_dataframe.sort_values(by='year peak internet')

# Calculate correlation coefficient
correlation_coefficient = peak_dataframe['peak gdp'].corr(peak_dataframe['peak internet'])

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(peak_dataframe['peak internet'], peak_dataframe['peak gdp'], alpha=0.7, label='Countries')
plt.xlabel('Highest percentage growth in internet users')
plt.ylabel('Highest percentage growth in gdp')
plt.title("Highest % growth in GDP vs Highest % growth in internet users")

# Create custom bins for grouping by every 5 years
bins = range(start_year, end_year + 5, 5)  # +6 to ensure the last bin includes the max year
custom_labels = ['1991-1995', '1996-2000', '2001-2005', '2006-2010', '2011-2015', '2016-2020']

# Group the data by these bins
peak_dataframe['Year Group'] = pd.cut(peak_dataframe['year peak internet'], bins=bins, right=False)

# Aggregate the data within each group (e.g., taking the mean of 'Peak GDP')
grouped_data = peak_dataframe.groupby('Year Group')['current capita'].mean()

# Plot the bar chart
plt.figure(figsize=(10, 6))
bar = grouped_data.plot(kind='bar', color='blue')
bar.set_xticklabels(custom_labels)
bar.set_xlabel('Year of highest growth in internet users')
bar.set_ylabel('Current GDP per capita')
plt.title("Current GDP per capita and year of highest internet adoption")
plt.xticks(rotation=0)

# Add tooltips using mplcursors
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(peak_dataframe['country'].iloc[sel.target.index]))

plt.legend()
plt.grid(True)
plt.show()
print(correlation_coefficient)  # -0.07085753072819657
print(peak_dataframe)
