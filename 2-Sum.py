import csv
from collections import defaultdict
from operator import length_hint
import sys

sys.setrecursionlimit(10**6)


def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    dict = {}
    for node in tsv:
        dict[int(node[0])] = ""
    print("dONE")
    return dict

A = read_graph('algo1-programming_prob-2sum.txt')

number = 0
count = 0
for t in range(-10000, 10001):
    count += 1
    sys.stdout.flush()
    sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * count / 20000))
    for i in A.keys():
        y = t - i
        if y in A:
            if y != i:
                number += 1
                print("yans")
                break

print(number)