import pandas as pd

# Load CSV file
internet_growth = pd.read_csv('Final.csv')


# Calculate peak growth of internet users for each country
peak_growth_data = []

for country in internet_growth['Entity'].unique():
    country_data = internet_growth[internet_growth['Entity'] == country]
    peak_growth = country_data['Percentage Increase'].max()
    year_of_peak_growth = country_data.loc[country_data['Percentage Increase'] == peak_growth, 'Year'].values[0]
    peak_growth_data.append([country, year_of_peak_growth, peak_growth])

# Create a new DataFrame
new_columns = ['Country', 'Year', 'Peak Growth of Internet Users']
new_df = pd.DataFrame(peak_growth_data, columns=new_columns)

# Save the new DataFrame to a CSV file
new_df.to_csv('peak_growth_data.csv', index=False)

print("New CSV file 'peak_growth_data.csv' created.")
