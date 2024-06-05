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

    def mapeamento_matrizAdjacencia(linha, coluna):
        n = 100
        contadorIteracao = 0
        chegou = False
    
        if linha > coluna or linha < 1 or linha > 100 or coluna < 1 or coluna > 100:
            print("Entrada invalida")
            return
    
        calculo = linha * n - n - ((linha * (linha - 1)) // 2) + (coluna - linha)
        print("\nPosicao no vetor", calculo)
    
        for i in range(1, 101):
            for j in range(1, 101):
                if j > i and not chegou:
                    contadorIteracao += 1
                if linha == i and coluna == j:
                    chegou = True
    
        print("\nPosicao no vetor por interacao:", contadorIteracao)
        print("\nPosicao no vetor por recursao:", recursao_matrizAdjacencia(linha, coluna, 1, 1, 0))

    def recursao_matrizAdjacencia(linha, coluna, i, j, indice):
        if j > i:
            indice += 1
        if linha == i and coluna == j:
            return indice
        if j <= 100:
            return recursao_matrizAdjacencia(linha, coluna, i, j + 1, indice)
        elif i < 100:
            return recursao_matrizAdjacencia(linha, coluna, i + 1, i + 1, indice)
        else:
            return -1

    def mapeamentoInverso_matrizAdjacencia(vetorCompactado, pos):
        cont = 1
        k = pos
        encontrou = False
    
        if not (0 <= k < len(vetorCompactado)):
            print("\nPosicao invalida.")
            return
    
        for i in range(100):
            for j in range(100):
                if i < j:
                    cont += 1
                if cont == vetorCompactado[k]:
                    print(f"\n\nLinha e coluna da matriz na posicao {k} :")
                    print(f"i={i}\nj={j}")
                    encontrou = True
                    break
            if encontrou:
                break

    def OperacaoDuasMatrizes(matriz1, matriz2, matrizTam, vetTam):
        vetContador = 0
        vetorMat1 = [0] * vetTam
        vetorMat2 = [0] * vetTam
        vetorMatSoma = [0] * vetTam
        linha = [0]* matrizTam
        matrizProduto = [linha]*matrizTam
    
        for i in range(matrizTam):
            for j in range(matrizTam):
                if i < j:
                    matriz1[j][i] = matriz1[i][j]
                    matriz2[j][i] = matriz2[i][j]
                    vetorMat1[vetContador] = matriz1[i][j]
                    vetorMat2[vetContador] = matriz2[i][j]
                    vetCont += 1
                    matrizProduto
    
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
    