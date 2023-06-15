import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=700, centers=4,
                       cluster_std=0.50, random_state=0) #X - dataset ,y_true - target label 
plt.scatter(X[:, 0], X[:, 1], s=50)

from sklearn.cluster import KMeans #importing model
kmeans = KMeans(n_clusters=4) 
kmeans.fit(X) #giving dataset 
y_kmeans = kmeans.predict(X) #predicting

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='inferno') #plasma inferno verdis
centers = kmeans.cluster_centers_ #getting center of the k mean clusterin
print(centers)
plt.scatter(centers[:, 0], centers[:, 1], c='green', s=200, alpha=0.5)

import pandas as pd
import numpy as np
heartDisease = pd.read_csv('/content/drive/MyDrive/ML data/k_means.csv')
heartDisease = heartDisease.replace('?',np.nan)
heartDisease.head()

trestbpsX = heartDisease.loc[:,'trestbps']
cholY = heartDisease.loc[:,'chol']
plt.scatter(trestbpsX, cholY, s=50)

kmeans2 = KMeans(n_clusters=2)
combined_list = list(zip(trestbpsX, cholY))
kmeans2.fit(combined_list)
y_kmeans2 = kmeans2.predict(combined_list)

plt.scatter(trestbpsX, cholY, c=y_kmeans2, s=50, cmap='viridis')

centers = kmeans2.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
