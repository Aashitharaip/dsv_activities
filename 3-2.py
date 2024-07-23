                                #MOVIE COMPARISON(DOUBLE BAR-GRAPH)

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

# Use TkAgg backend for interactive plots
matplotlib.use('TkAgg')

# Load dataset
movie_scores = pd.read_csv('c:/Users/Aashitha/Downloads/Datasets/Datasets/movie_scores.csv')

# Create figure
plt.figure(figsize=(10, 5), dpi=300)

# Create bar plot
pos = np.arange(len(movie_scores['MovieTitle']))
width = 0.3
plt.bar(pos - width / 2, movie_scores['Tomatometer'], width, label='Tomatometer')
plt.bar(pos + width / 2, movie_scores['AudienceScore'], width, label='Audience Score')

# Specify ticks
plt.xticks(pos, movie_scores['MovieTitle'], rotation=10)
plt.yticks(np.arange(0, 101, 20))  # y-ticks from 0 to 100%

# Get current Axes for setting tick labels and horizontal grid
ax = plt.gca()

# Add minor ticks for y-axis in the interval of 5
ax.set_yticks(np.arange(0, 101, 5), minor=True)  # y-ticks from 0 to 100% for minor ticks

# Add major horizontal grid with solid lines
ax.yaxis.grid(which='major')

# Add minor horizontal grid with dashed lines
ax.yaxis.grid(which='minor', linestyle='--')

# Add title
plt.title('Movie comparison')

# Add legend
plt.legend()

# Show plot
plt.show()