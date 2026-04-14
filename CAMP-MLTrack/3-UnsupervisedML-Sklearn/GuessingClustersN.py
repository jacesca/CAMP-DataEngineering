"""Guessing number of clusters"""
import numpy as np
import matplotlib.pyplot as plt

from environment import prepare_environment, hprint
from sklearn.cluster import KMeans


# Preparing the environment
prepare_environment()

# Reading the data
hprint('Predict for new samples')
points = np.genfromtxt('points.csv', delimiter=',', skip_header=1)
print(points)

# Plotting the data
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1])
plt.title('Points')
plt.xlabel('xs')
plt.ylabel('ys')

# Instantiate the model
hprint('Modeling the data')
model = KMeans(n_clusters=3)
labels = model.fit_predict(points)
centroids = model.cluster_centers_

# print(np.unique(labels, return_counts=True))  # (array([0, 1, 2]), array([39, 50, 61], dtype=int64))  # noqa
print('Detected Clusters:',
      dict(np.asarray(np.unique(labels, return_counts=True)).T))  # {0: 39, 1: 50, 2: 61}  # noqa

# Plotting the detected clusters
plt.subplot(1, 2, 2)
plt.scatter(points[:, 0], points[:, 1], c=labels, alpha=0.25)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50, marker='D')
plt.title('Found Clusters')
plt.xlabel('xs')
plt.ylabel('ys')

# Plotting the graph
plt.tight_layout()
plt.show()
