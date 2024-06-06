import networkx as nx
import random
import math
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
            adj_matrix[n2][n1] = 1
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
        array_upper_triangular = [0] * int(self.num_nodes * (self.num_nodes - 1) / 2)

        for idx in idx_array:
            array_upper_triangular[idx] = 1
        k = 0
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                adj_matrix[i][j] = array_upper_triangular[k]
                adj_matrix[j][i] = array_upper_triangular[k]
                k += 1
        return adj_matrix

    def generate_graph_by_matrix(self, adj_matrix: np) -> nx:
        graph = nx.Graph()
        graph.add_nodes_from(range(self.num_nodes))
        for n1 in range(self.num_nodes):
            for n2 in range(n1 + 1, self.num_nodes):
                if adj_matrix[n1, n2] == 1:
                    graph.add_edge(n1, n2)
        return graph

    def mapeamento_matrizAdjacencia(self, linha, coluna):
        contadorIteracao = 0
        chegou = False

        if (
            linha >= coluna
            or linha < 0
            or linha > self.num_nodes
            or coluna < 0
            or coluna > self.num_nodes
        ):
            print("Entrada invalida")
            return

        calculo = (linha * (2 * self.num_nodes - linha - 1)) // 2 + (coluna - linha - 1)
        print("\nPosicao no vetor", calculo)

        for i in range(0, self.num_nodes):
            for j in range(0, self.num_nodes):
                if j > i and not chegou:
                    contadorIteracao += 1
                if linha == i and coluna == j:
                    chegou = True

        print("\nPosicao no vetor por interacao:", contadorIteracao)
        print(
            "\nPosicao no vetor por recursao:",
            self.recursao_matrizAdjacencia(linha, coluna, 1, 1, 0),
        )

    def recursao_matrizAdjacencia(self, linha, coluna, i, j, indice):
        if j > i:
            indice += 1
        if linha == i and coluna == j:
            return indice
        if j <= self.num_nodes:
            return self.recursao_matrizAdjacencia(linha, coluna, i, j + 1, indice)
        elif i < self.num_nodes:
            return self.recursao_matrizAdjacencia(linha, coluna, i + 1, i + 1, indice)
        else:
            return -1

    def reverse_mapping_analytical(self, k):
        i = math.floor((-1 + math.sqrt(1 + 8 * k)) / 2)
        j = k - (i * (i + 1)) // 2
        return i, j

    def reverse_mapping_iterative(self, k):
        i = 0
        s = self.num_nodes - 1
        while k >= s:
            i += 1
            s -= 1
        j = k - s
        return i, j

    def mapeamentoInverso_matrizAdjacencia(self, k):
        i_analytical, j_analytical = self.reverse_mapping_analytical(k)
        i_iterative, j_iterative = self.reverse_mapping_iterative(k)
        print(f"Mapeamento analítico: (i, j) = ({i_analytical}, {j_analytical})")
        print(f"Mapeamento iterativo: (i, j) = ({i_iterative}, {j_iterative})")

    def OperacaoDuasMatrizes(self, matriz1, matriz2, matrizTam, vetTam):
        vetContador = 0
        vetorMat1 = [0] * vetTam
        vetorMat2 = [0] * vetTam
        vetorMatSoma = [0] * vetTam
        linha = [0] * matrizTam
        matrizProduto = [linha[:] for _ in range(matrizTam)]

        vetCont = 0

        for i in range(matrizTam):
            for j in range(matrizTam):
                if i < j:
                    matriz1[j][i] = matriz1[i][j]
                    matriz2[j][i] = matriz2[i][j]
                    vetorMat1[vetContador] = matriz1[i][j]
                    vetorMat2[vetContador] = matriz2[i][j]
                    vetContador += 1

        print("\nMatriz 1: ")
        for i in range(matrizTam):
            print(" ".join(f"{matriz1[i][j]:3}" for j in range(matrizTam)))

        print("\nMatriz 2: ")
        for i in range(matrizTam):
            print(" ".join(f"{matriz2[i][j]:3}" for j in range(matrizTam)))

        print("\nVetor da Matriz 1: ")
        print(" ".join(f"{vetorMat1[i]:3}" for i in range(vetTam)))

        print("\nVetor da Matriz 2: ")
        print(" ".join(f"{vetorMat2[i]:3}" for i in range(vetTam)))

        for i in range(vetTam):
            vetorMatSoma[i] = vetorMat1[i] + vetorMat2[i]

        print("\nSoma da Matriz 1 + 2: ")
        print(" ".join(f"{vetorMatSoma[i]:3}" for i in range(vetTam)))

        print("\nProduto da Matriz 1 * 2: ")
        for i in range(matrizTam):
            for j in range(matrizTam):
                for k in range(matrizTam):
                    matrizProduto[i][j] += matriz1[i][k] * matriz2[k][j]
                print(f"{matrizProduto[i][j]:3}", end=" ")
            print()
