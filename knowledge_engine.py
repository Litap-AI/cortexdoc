import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

def add_relationship(entity1, entity2):

    graph.add_node(entity1)

    graph.add_node(entity2)

    graph.add_edge(entity1, entity2)

def visualize_graph():

    plt.figure(figsize=(12,8))

    nx.draw(
        graph,
        with_labels=True,
        node_size=3000,
        font_size=10
    )

    plt.savefig(
        "outputs/knowledge_graph.png"
    )

    print("Knowledge graph saved!")
    