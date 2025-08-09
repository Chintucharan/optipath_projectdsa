import os
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, path):
    print("Drawing graph...")
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path and len(path) > 1:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    if not os.path.exists('static'):
        os.makedirs('static')
        print("Created 'static' folder")

    plt.savefig('static/path.png')
    plt.close()
    print("Saved image at static/path.png")
