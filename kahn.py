from collections import deque, defaultdict
from typing import Deque, List, DefaultDict


class Graph:
    class not_an_acyclic_graph(Exception):
        pass

    def __init__(self, vertex_size: int) -> None:
        self.adjacency_matrix: DefaultDict[int, List[int]] = defaultdict(list)
        self.vertex_size = vertex_size

    def addEdge(self, u: int, v: int) -> None:
        self.adjacency_matrix[u].append(v)

    def topologicalSort(self) -> None:
        in_degree = [0]*(self.vertex_size)
        for node in self.adjacency_matrix.keys():
            for neighboringNode in self.adjacency_matrix[node]:
                in_degree[neighboringNode] += 1
        zero_nodes: Deque[int] = deque()
        for node in range(self.vertex_size):
            if in_degree[node] == 0:
                zero_nodes.append(node)
        visited_nodes: int = 0
        while zero_nodes:
            visited_node = zero_nodes.popleft()
            print(visited_node)
            for node in self.adjacency_matrix[visited_node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    zero_nodes.append(node)
            visited_nodes += 1
        if visited_nodes != self.vertex_size:
            raise self.not_an_acyclic_graph


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()
