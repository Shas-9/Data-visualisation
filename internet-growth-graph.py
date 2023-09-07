import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
internet_growth = pd.read_csv('Final.csv')
gdp_growth = pd.read_csv("gdp_growth.csv")

index = 0

while True:
    # Select only the desired columns
    selected_columns = ['Entity', 'Year', 'Internet Users(%)']

    # Select data for the desired country
    selected_country = internet_growth.loc[index, "Entity"]
    internet_growth = internet_growth[selected_columns]
    country_data = internet_growth[internet_growth['Entity'] == selected_country]

    # Filter data for the desired years
    start_year = 1990
    end_year = 2020
    selected_data = country_data[(country_data['Year'] >= start_year) & (country_data['Year'] <= end_year)]

    # Calculate percentage increase
    selected_data['Percentage_Increase'] = selected_data['Internet Users(%)'].diff().copy()

    # Create the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(selected_data['Year'], selected_data['Percentage_Increase'], marker='')
    plt.xlabel('Year')
    plt.ylabel('Percentage Increase in Internet Users')
    plt.title(f'Percentage Increase in Internet Users for {selected_country} ({start_year}-{end_year})')
    plt.grid(True)
    plt.show()

    index += 41
    if index > 88:
        break

# Create the line graph with two y-labels and different colors
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Internet Users Increase with blue color
    ax1.plot(['Year'], country_internet_data['Percentage Increase'], color='blue', marker='', label='Internet '
                                                                                                        'Users '
                                                                                                        'Increase')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Internet Users Increase (%)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()  # Create a second y-axis for GDP Increase

    # Plot GDP Increase with red color
    ax2.plot(country_gdp_data.columns[start_year:end_year],
             country_gdp_data.iloc[country_gdp_data.index[country_gdp_data['Country Name'] == country],
             start_year:end_year], color='red',
             marker='o', label='GDP Increase')
    ax2.set_ylabel('GDP Increase', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Title and Legends
    plt.title(f'Internet Users and GDP Increase for {country} ({start_year}-{end_year})')
    fig.tight_layout()
    fig.legend(loc='upper left')

    plt.grid(True)
    plt.show()
