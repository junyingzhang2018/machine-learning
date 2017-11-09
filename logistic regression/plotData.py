
# coding: utf-8

# In[ ]:

def plotData(X, y):
#PLOTDATA Plots the data points X and y into a new figure 
#   PLOTDATA(x,y) plots the data points with + for the positive examples
#   and o for the negative examples. X is assumed to be a Mx2 matrix.

    import matplotlib.pyplot as plt
    import numpy as np

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the positive and negative examples on a
#               2D plot, using the option 'k+' for the positive
#               examples and 'ko' for the negative examples.
#

    # Find Indices of Positive and Negative Examples
    pos = np.where(y==1)
    neg = np.where(y==0)

    # plot! [0] indexing at end necessary for proper legend creation in ex2.py
    plt.scatter(X[pos,0], X[pos,1], marker='+', markersize=9, color='k')
    plt.scatter(X[neg,0], X[neg,1], marker='o', markersize=7, color='y')
    plt.legend((p1,p2),('y = 1', 'y = 0'), numpoints=1, handlelength=0)

