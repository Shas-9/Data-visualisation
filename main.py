# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# gdp_growth = pd.read_csv("gdp_growth.csv")
# internet_user_growth = pd.read_csv("Final.csv")


import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
internet_growth = pd.read_csv('Final.csv')

index = 0

while True:
    # Select only the desired columns
    selected_columns = ['Entity', 'Year', 'Internet Users(%)']

    # Select data for the desired country
    selected_country = internet_growth.loc[index, "Entity"]
    internet_growth = df
    country_data = internet_growth[internet_growth['Entity'] == selected_country]
    country_data = country_data[selected_columns]

    # Filter data for the desired years
    start_year = 1990
    end_year = 2020
    selected_data = country_data[(country_data['Year'] >= start_year) & (country_data['Year'] <= end_year)]

    # Calculate percentage increase
    selected_data['Percentage_Increase'] = selected_data['Internet Users(%)'].diff()
    print(selected_data)

    # Create the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(selected_data['Year'], selected_data['Percentage_Increase'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Percentage Increase in Internet Users')
    plt.title(f'Percentage Increase in Internet Users for {selected_country} ({start_year}-{end_year})')
    plt.grid(True)
    plt.show()

    index += 41
    if index > 88:
        break







