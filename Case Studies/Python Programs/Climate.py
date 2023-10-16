import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
data = pd.read_csv("/home/shriram/Documents/Data Analytics/Case Studies/vjaFRMXv.csv")
data.head(15)

data.describe

data.info

#filtereing out the relevent coulmns:

# Select columns based on your criteria
print(data.columns)

relevant_columns = ['DateTime', 'SSP1-2.6 Median', 'SSP2-4.5 Median', 'SSP5-8.5 Median']
filtered_data = data[relevant_columns]

import matplotlib.pyplot as plt

# Plot time series data for each scenario
for column in filtered_data.columns[1:]:
    plt.plot(filtered_data['DateTime'], filtered_data[column], label=column)

plt.xlabel('Time')
plt.ylabel('Tmin < -15°C')
plt.title('Temperature Data under Different Scenarios')
plt.legend()
plt.show()

for scenario in ['SSP1-2.6', 'SSP2-4.5', 'SSP5-8.5']:
    for percentile in ['Median', 'Range (low)', 'Range (high)']:
        column_name = f'{scenario} {percentile}'
        plt.plot(data['DateTime'], data[column_name], label=f'{scenario} {percentile}')

plt.xlabel('Time')
plt.ylabel('Temperature Data')
plt.title('Temperature Data under Different Scenarios and Percentiles')
plt.legend()
plt.show()


plt.savefig('temperature_time_series.png')


historical_data = data['Modeled Historical']
days_below_minus_15_1= (historical_data < -15).sum()

print(days_below_minus_15)

# Filter data for the specific scenario (e.g., SSP1-2.6)
scenario_data = data['SSP1-2.6 Median']  # Use the appropriate column name

days_below_minus_15_2 = (scenario_data < -15).sum()

print(days_below_minus_15_2)


#Filtering based on the senario that it will not live more than 4 days in -15 degrees
if days_below_minus_15 < 4:
    print("The location is suitable for aquaculture.")
else:
    print("The location is not suitable for aquaculture.")


