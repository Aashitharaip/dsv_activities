import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os
import matplotlib.image as mpimg

# Use TkAgg backend for interactive plots
matplotlib.use('TkAgg')

img_filenames = sorted(os.listdir('c:/Users/Aashitha/Downloads/Datasets/Datasets/images'))
img_path = "c:/Users/Aashitha/Downloads/Datasets/Datasets/images"
imgs = []
for file in img_filenames:
    read_img = mpimg.imread(os.path.join(img_path, file)) 
    imgs.append(read_img)

gray=lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
img=gray(imgs[0])

# Create subplot
fig, axes = plt.subplots(2, 2)
fig.figsize = (6, 6)
fig.dpi = 150
axes = axes.ravel()
# Specify labels
labels = ['coast', 'beach', 'building', 'city at night']
# Plot images
for i in range(len(imgs)):
    axes[i].imshow(imgs[i])
    axes[i].set_xticks([])
    axes[i].set_yticks([])
    axes[i].set_xlabel(labels[i])
plt.show()