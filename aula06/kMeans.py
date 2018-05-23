# -*- coding: utf-8 -*-

from __future__ import division
from linear_algebra import squared_distance, vector_mean, distance
import math
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import csv


class KMeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k          # number of clusters
        self.means = None   # means of clusters

    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):

        self.means = random.sample(inputs, self.k)
        assignments = None
        print(self.k)
        while True:
            # Find new assignments
            new_assignments = map(self.classify, inputs)

            # If no assignments have changed, we're done.
            if assignments == new_assignments:
                return

            # Otherwise keep the new assignments,
            assignments = new_assignments

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                # avoid divide-by-zero if i_points is empty
                if i_points:
                    self.means[i] = vector_mean(i_points)


def squared_clustering_errors(inputs, k):
    """finds the total squared error from k-means clustering the inputs"""
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)

    return sum(squared_distance(input, means[cluster])
               for input, cluster in zip(inputs, assignments))


if __name__ == "__main__":

    # inputs = np.array([[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]])
    # data = pd.read_csv('austin_crime02.csv', names=["clearance_date", "timestamp", "time", "clearance_code",
    #                                                "clearance_status", "description_code", "description", "district_code", "district", "latitude", "longitude"])
    # clearance_date, timestamp, time, clearance_code, clearance_status, description_code, description, district_code, district, latitude, longitude
    # 0,               1      ,  2   ,  3            ,  4             ,   5,                6          , 7           ,   8 

    # data = data.drop('clearance_date', axis=1)
    # data = data.drop('timestamp', axis=1)
    # data = data.drop('time', axis=1)
    # data = data.drop('clearance_code', axis=1)
    # data = data.drop('clearance_status', axis=1)
    # data = data.drop('description_code', axis=1)
    # data = data.drop('description', axis=1)
    # data = data.drop('district_code', axis=1)
    # data = data.drop('district', axis=1)2
    # data = data.drop('latitude', axis=1)
    # data = data.drop('longitude', axis=1)

    inputs=[]
    x= []
    y= []

    with open('austin_crime02.csv') as csvfile:
        readCSV=csv.reader(csvfile, delimiter = ',')
#        x= [row[4] for row in readCSV]
#        y= [row[5] for row in readCSV]

        a=input("Insira a primeira coluna para o Kmeans: ")
        b=input("Insira a segunda coluna para o Kmeans: ")

        for row in readCSV:
            x.append(int(row[a]))
            y.append(int(row[b]))

    for i in range(len(x)):
        inputs.append([x[i], y[i]])

    plt.scatter(x, y)
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    ks = range(1, 10)
    errors = [squared_clustering_errors(inputs, k) for k in ks]
    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show()

    random.seed(0)
    clusterer=KMeans(2)
    clusterer.train(inputs)
    print "2-means:"
    print clusterer.means
    print

    plt.plot(x, y, 'b*')
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    clusterX=[row[0] for row in clusterer.means]
    clusterY=[row[1] for row in clusterer.means]
    plt.plot(clusterX, clusterY, 'rs')
    plt.show()

    random.seed(0)  # so you get the same results as me
    clusterer=KMeans(3)
    clusterer.train(inputs)
    print "3-means:"
    print clusterer.means
    print

    plt.plot(x, y, 'b*')
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    clusterX=[row[0] for row in clusterer.means]
    clusterY=[row[1] for row in clusterer.means]
    plt.plot(clusterX, clusterY, 'rs')
    plt.show()

    random.seed(0)  # so you get the same results as me
    clusterer=KMeans(5)
    clusterer.train(inputs)
    print "5-means:"
    print clusterer.means
    print

    plt.plot(x, y, 'b*')
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    clusterX=[row[0] for row in clusterer.means]
    clusterY=[row[1] for row in clusterer.means]
    plt.plot(clusterX, clusterY, 'rs')
    plt.show()

