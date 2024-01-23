## Expectation Maximization

For this project, K Means Clustering, Gaussian Mixture Models, and a metric called Bayesian Information Criterion are implemented. Read ahead to learn about these algorithms and the criterion.

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

At this step, two auxilliary variables are defined: z_ik and gamma_z_ik.  

z_ik is an indicator variable equal to 1 if x_i is in class k and 0 otherwise.  

z_ik = pi_k * N(x_i | mu_k, sigma_k) = P(z_k) * P(x_i | z_ik = 1)

gamma_z_ik = P(z_ik = 1 | x_i)

gamma_z_ik is the probability a given observation x_i is in class k. This is obtained using Bayes' Theorem.

Upon taking derivatives, we are left with the following formulas for mu_k, sigma_k, and pi_k.  

u_k = (1/N_k) sum((i = 1 to N), gamma_z_ik*x_i)  

sigma_k = (1/N_k) sum((i = 1 to N), gamma_z_ik*(x_i - mu_k)*(x_i - mu_k).T)  

pi_k = N_k / N, where N_k = sum((i=1 to N), gamma_z_ik)

There is a circular dependence in these formulas.  

mu_k, sigma_k, and pi_k depend on gamma, and gamma depends on mu_k, sigma_k, and pi_k.

In order to solve for these variables, we use the expectation maximization algorithm.

#### Expectation Maximization Algorithm

1. Initialize mu_k, sigma_k, and pi_k
2. compute gamma_z_ik's for all datapoints
3. recompute mu_k, sigma_k, and pi_k until convergence

### Bayesian Information Criterion

This criterion is used to prevent overfitting. It penalizes models based on the number of parameters they use. In the case of the Gaussian Mixture Model, the number of criterions per cluster (which are mu_k, sigma_k, and pi_k) times the number of clusters.
