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

A Gaussian Mixture Model is a probabilistic model that represents data as a mixture of multiple gaussian distribution. Each gaussian distribution represents a cluster in the data. The number of clusters is predetermined. The gaussian mixture model tries to optimize three parameters--mu, sigma, and pi--to best fit our data. Mu is the mean of the normal distribution. Sigma is a measure of how spread out the distribution is. A high sigma means that it is very spread out. Pi tells us the probability of a datapoint fitting into each of the clusters. The objective of this model is to maximize the probability of seeing all the datapoints, given pi, sigma, and mu. This probability is shown below.

P(X | pi, mu, sigma) = prod[(i=1 to N), sum((k=1 to K), pi_k * N(x_i | mu_k, sigma_k))],  

where i is the index of the datapoints, k is the index of the clusters, and N(x_i | mu_k, sigma_k) is the normal distribution of that cluster.  
We maximize this probability by taking its derivative, equating it to zero, and solving for mu_k, sigma_k, and pi_k.

