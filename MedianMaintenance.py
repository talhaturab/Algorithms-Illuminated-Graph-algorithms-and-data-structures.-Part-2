import csv
from collections import defaultdict
from ipaddress import summarize_address_range
from operator import length_hint
from re import A
import sys
from heapq import heappop, heappush, heapify
import heapq

sys.setrecursionlimit(10**6)

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    next(tsv)
    next(tsv)
    A = []
    for node in tsv:
        calculate_median(int(node[0]))
    print("dONE")

heap1 = [-2793]
heap2 = [6331]
heapify(heap1)
heapify(heap2)
sum_of_medians = 2793 + 6331
# sum_of_medians = 27 + 25

def calculate_median(i):
    global sum_of_medians
    max = -heap1[0]
    min = heap2[0]
    if i < max:
        heappush(heap1, -i)
    elif i > min:
        heappush(heap2, i)
    else:
        heappush(heap2, i)
    
    length_heap1 = len(heap1)
    length_heap2 = len(heap2)
    total_length = length_heap1 + length_heap2
    difference = length_heap1 - length_heap2

    if difference == 2:
        element = heappop(heap1)
        heappush(heap2, -element)
    elif difference == -2:
        element = heappop(heap2)
        heappush(heap1, -element)

    # print(heap1)
    # print(heap2)
    if total_length % 2 == 0:
        median = -heap1[0]
        print(median)
        sum_of_medians += median
    else:
        median_number = (total_length + 1) / 2
        if median_number == length_heap1:
            sum_of_medians += (-heap1[0])
            print(-heap1[0])
        else:
            sum_of_medians += (heap2[0])
            print(heap2[0])

read_graph('Median.txt')
# print(sum_of_medians % 10000)
print(sum_of_medians % 10000)