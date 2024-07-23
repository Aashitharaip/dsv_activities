                                   #STOCK TRENDS

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

# Use TkAgg backend for interactive plots
matplotlib.use('TkAgg')

# Load data
google = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/GOOGL_data.csv')
facebook = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/FB_data.csv')
apple = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/AAPL_data.csv')
amazon = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/AMZN_data.csv')
microsoft = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/MSFT_data.csv')

# Convert 'date' column to datetime
google['date'] = pd.to_datetime(google['date'])
facebook['date'] = pd.to_datetime(facebook['date'])
apple['date'] = pd.to_datetime(apple['date'])
amazon['date'] = pd.to_datetime(amazon['date'])
microsoft['date'] = pd.to_datetime(microsoft['date'])

# Create figure
plt.figure(figsize=(16, 8), dpi=300)

# Plot data
plt.plot(google['date'], google['close'], label='Google')
plt.plot(facebook['date'], facebook['close'], label='Facebook')
plt.plot(apple['date'], apple['close'], label='Apple')
plt.plot(amazon['date'], amazon['close'], label='Amazon')
plt.plot(microsoft['date'], microsoft['close'], label='Microsoft')

# Specify ticks for x- and y-axis
plt.xticks(rotation=70)
plt.yticks(np.arange(0, 1450, 100))

# Add title and label for y-axis
plt.title('Stock trend', fontsize=16)
plt.ylabel('Closing price in $', fontsize=14)

# Add grid
plt.grid()

# Add legend
plt.legend()

# Show plot
plt.show()