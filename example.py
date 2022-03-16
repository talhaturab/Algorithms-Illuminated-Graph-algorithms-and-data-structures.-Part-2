from cmath import inf
import csv
from collections import defaultdict
from operator import length_hint
import sys

from numpy import Infinity

def make_link(G, node1, node2, length):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = length
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = length
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter="\t")
    G = {}
    for node in tsv:
        length = len(node) - 1
        for i in range(1, length):
            set = node[i].split(",")
            make_link(G, int(node[0]), int(set[0]), int(set[1]))
    return G
    

def dijkstra(vertex, G):
    X = [vertex]
    L = {}
    L[vertex] = 0
    loop = True
    while (loop == True):
        minDist = inf
        minV = ""
        loop = False
        for v in X:
            for neighbour in G[v].keys():
                if neighbour not in X:
                    loop = True
                    dist = L[v] + G[v][neighbour]
                    if dist < minDist:
                        minDist = dist
                        minV = neighbour
        if loop == True:
            X.append(minV)
            L[minV] = minDist

    # print("X", X)
    # print("L", L)
    # print(dist)
    # print(G)
    print(L[7],L[37],L[59],L[82],L[99],L[115],L[133],L[165],L[188],L[197])

# Read the marvel comics graph
straightG = read_graph('dijkstraData.txt')
dijkstra(1, straightG)

# prev ans(3024 3684 2947 2660 2367 2399 3879 2442 2610 5130)
# (2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068)
