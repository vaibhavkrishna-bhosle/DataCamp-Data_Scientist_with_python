'''In the FIFA 18 dataset, we have concentrated on defenders in previous exercises. Let us try to focus on attacking attributes of a player. Pace (pac), Dribbling (dri) and Shooting (sho) are features that are present in attack minded players. In this exercise, k-means clustering has already been applied on the data using the scaled values of these three attributes. Try some basic checks on the clusters so formed.

The data is stored in a Pandas data frame, fifa. The scaled column names are present in a list scaled_features. The cluster labels are stored in the cluster_labels column. Recall the .count() and .mean() methods in Pandas help you find the number of observations and mean of observations in a data frame.'''

import pandas as pd
from scipy.cluster.vq import kmeans, vq
import matplotlib.pyplot as plt

fifa = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/26-Cluster Analysis in Python /Introduction to Clustering /fifa.csv')

# Print the size of the clusters
print(fifa.groupby('cluster_labels')['ID'].count())

# Print the mean value of wages in each cluster
print(fifa.groupby('cluster_labels')['eur_wage'].mean())

# Create centroids with kmeans for 2 clusters
cluster_centers,_ = kmeans(fifa['scaled_features'], 2)

# Assign cluster labels and print cluster centers
fifa['cluster_labels'], _ = vq(fifa['scaled_features'], cluster_centers)
print(fifa.groupby('cluster_labels')['scaled_features'].mean())

# Plot cluster centers to visualize clusters
fifa.groupby('cluster_labels')['scaled_features'].mean().plot(legend=True, kind='bar')
plt.show()

# Get the name column of top 5 players in each cluster
for cluster in fifa['cluster_labels'].unique():
    print(cluster, fifa[fifa['cluster_labels'] == cluster]['name'].values[:5])