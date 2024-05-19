import networkx as nx
import random
import numpy as np
from attrs import define


@define
class TriangularMatrix:
    num_nodes: int = 100

    def generate_random_graph(self, mult: int = 10) -> nx:
        num_edges = random.randint(self.num_nodes, mult * self.num_nodes)
        graph = nx.Graph()
        graph.add_nodes_from(range(self.num_nodes))

        while len(graph.edges) < num_edges:
            n1 = random.randint(0, self.num_nodes - 1)
            n2 = random.randint(0, self.num_nodes - 1)
            if n1 != n2 and not graph.has_edge(n1, n2):
                graph.add_edge(n1, n2)
        return graph

    def binary_adjacency_matrix(self, graph: nx) -> np:
        adj_matrix = np.zeros((self.num_nodes, self.num_nodes), dtype=int)
        for n1, n2 in graph.edges:
            adj_matrix[n1][n2] = 1
            adj_matrix[n1][n2] = 1

        return adj_matrix

    def matrix_to_array(self, adj_matrix: np) -> np:
        elements = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                elements.append(adj_matrix[i, j])
        elements = np.array(elements)
        return elements

    def index_array(self, elements: np) -> list:
        return [idx for idx, value in enumerate(elements) if value == 1]

    def array_to_matrix(self, idx_array: list) -> np:
        adj_matrix = np.zeros((self.num_nodes, self.num_nodes), dtype=int)
        for idx in idx_array:
            n1, n2 = [0][idx], [1][idx]
            adj_matrix[n1][n2] = 1
            adj_matrix[n1][n2] = 1

        return adj_matrix

    def generate_graph_by_matrix(self, adj_matrix: np) -> nx:
        graph = nx.Graph()
        graph.add_nodes_from(range(self.num_nodes))
        for n1 in range(self.num_nodes):
            for n2 in range(n1 + 1, self.num_nodes):
                if adj_matrix[n1, n2] == 1:
                    graph.add_edge(n1, n2)
        return graph
