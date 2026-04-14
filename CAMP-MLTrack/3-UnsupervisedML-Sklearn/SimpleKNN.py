"""Predicting the class of the irish dataset"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from environment import prepare_environment, hprint
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# Setting the seed
prepare_environment()

# Reading the data
hprint('Reading the data')
df, _ = load_iris(return_X_y=True, as_frame=True)
X = df.values
print(df.head())

# Instantiate the model
hprint('Modeling the data')
model = KMeans(n_clusters=3)
model.fit(df)

labels = model.predict(df)
centroids = model.cluster_centers_

# print(np.unique(labels, return_counts=True))  # (array([0, 1, 2]), array([39, 50, 61], dtype=int64))  # noqa
print('Detected Clusters:',
      dict(np.asarray(np.unique(labels, return_counts=True)).T))  # {0: 39, 1: 50, 2: 61}  # noqa

# Predicting over the new samples
hprint('Predict for new samples')
new_samples = pd.DataFrame(
    columns=df.columns,
    data=[
        [5.7, 4.4, 1.5, 0.4],
        [6.5, 3.0, 5.5, 1.8],
        [5.8, 2.7, 5.1, 1.9],
    ]
)
new_labels = model.predict(new_samples)
print(new_labels)

# Plotting the relation between sepal length (cm) and petal length (cm)
hprint('Visualizing the relation between sepal and petal length')
plt.figure()
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=labels)
plt.title('Iris Dataset')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.show()
