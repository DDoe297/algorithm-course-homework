import sys
from typing import List


class Graph():

    def __init__(self, vertexSize: int, adjacencyMatrix: List[List[int]]):
        self.vertex_size = vertexSize
        self.adjacency_matrix = adjacencyMatrix

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.vertex_size):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
       


g = Graph(5, [[0, 2, 0, 6, 0],
              [2, 0, 3, 8, 5],
              [0, 3, 0, 0, 7],
              [6, 8, 0, 0, 9],
              [0, 5, 7, 9, 0]])

g.primMST()
