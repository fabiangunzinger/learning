
# Import libraries and assign aliases
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset (background: http://www.dicook.org/files/jsm19/slides#1)
iris = sns.load_dataset('iris')
print(iris.head())
print(iris.describe())
print(iris.species.unique())

%matplotlib inline

# Create a basic swarm plot
sns.set()
sns.swarmplot(x='species', y='petal_length', data=iris)
plt.show()

# Create an ECDF for setosa
setosa_sepal_length = iris.sepal_length[iris.species=='setosa']
pcentiles = np.array([2.5, 25, 50, 75, 97.5])
setosa_pcentiles = np.percentile(setosa_sepal_length, pcentiles)
print(setosa_pcentiles)

def ecdf(data):
	"""Compute x and y axes of empirical CDF for a one-dimensional array"""
	n = len(data)
	x = np.sort(data)
	y = np.arange(1, n+1)/n
	return x, y

x_setosa, y_setosa = ecdf(setosa_sepal_length)
plt.plot(x_setosa, y_setosa, marker='.', linestyle='none')
plt.plot(setosa_pcentiles, pcentiles/100, marker='D', linestyle='none')
plt.xlabel('Sepal length (cm)')
plt.ylabel('ECDF')
plt.show()