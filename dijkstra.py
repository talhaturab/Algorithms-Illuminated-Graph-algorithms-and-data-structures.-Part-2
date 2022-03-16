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
    dist = {}
    open_list = [vertex]
    explored = [vertex]
    dist[vertex] = 0

    while (len(open_list) > 0):
        current = open_list[0]
        del open_list[0]

        for neighbour in G[current].keys():
            if neighbour not in explored:
                explored.append(neighbour)
                open_list.append(neighbour)
                dist[neighbour] = G[current][neighbour] + dist[current]
            elif (dist[neighbour]) > (G[current][neighbour] + dist[current]):
                open_list.append(neighbour)
                dist[neighbour] = G[current][neighbour] + dist[current]

    # print(dist)
    # print(G)
    print(dist[7],dist[37],dist[59],dist[82],dist[99],dist[115],dist[133],dist[165],dist[188],dist[197])

# Read the marvel comics graph
straightG = read_graph('dijkstraData.txt')
dijkstra(1, straightG)

# prev ans(3024 3684 2947 2660 2367 2399 3879 2442 2610 5130)
# (2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068)
