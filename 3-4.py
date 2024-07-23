import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

# Use TkAgg backend for interactive plots
matplotlib.use('TkAgg')

# Load dataset
sales = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/smartphone_sales.csv')

# Create figure
plt.figure(figsize=(10, 6), dpi=300)
# Create stacked area chart
labels = sales.columns[2:]
plt.stackplot('Quarter', 'Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO', data=sales, labels=labels)
# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Quarters')
plt.ylabel('Sales units in thousands')
plt.title('Smartphone sales units')
# Show plot
plt.show()