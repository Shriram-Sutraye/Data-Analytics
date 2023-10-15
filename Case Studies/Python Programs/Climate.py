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
