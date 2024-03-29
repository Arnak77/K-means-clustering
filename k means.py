# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset=pd.read_csv(r"D:\NIT\JANUARY\20 jan(clustring)\20th- Clustering\2.K-MEANS CLUSTERING\Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values


from sklearn.cluster import KMeans 

wcss = [] 


for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
print(len(y_kmeans))


d2=pd.concat([dataset,pd.Series(y_kmeans)],axis = 1)
d2.rename({0:'new'}, axis=1)





# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()








dataset1=pd.read_csv(r"D:\NIT\JANUARY\20 jan(clustring)\20th- Clustering\2.K-MEANS CLUSTERING\Mall_Customers.csv")

d3 = dataset1.copy()

dataset1 = dataset1.iloc[:, [3,4]].values

from sklearn.cluster import KMeans
sc = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
sc.fit(dataset1)

d3['pred']=sc.predict(dataset1)


