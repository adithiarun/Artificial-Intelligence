## Expectation Maximization

For this project, K Means Clustering, Gaussian Mixture Models, and a metric called Bayesian Information Criterion are implemented.

### K-means Clustering
This is an unsupervised learning algorithm which groups datapoints based on their similarity to each other.

#### K-means clustering steps:

1. Specify the number of clusters (k)
2. Initialize centroids by randomly selecting k datapoints from the dataset without replacement
3. Repeat the following step until there are no changes to the centroids:  
&nbsp; i. compute the distance between the datapoints and all the centroids  
&nbsp; ii. assign each datapoint to the closest cluster  
&nbsp; iii. compute new centroids by taking the average of all data points belonging to the cluster  

In this project, k means clustering is used to segment a color image.

### Multivariate Gaussian Mixture Model
