import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph: nx) -> None:
    plt.figure(figsize=(5, 5))
    nx.draw(
        graph,
        with_labels=True,
        node_color="lightgreen",
        node_size=50,
        edge_color="gray",
    )
    plt.show()
