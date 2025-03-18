import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_graph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=22)
    G.add_edge('A', 'C', weight=9)
    G.add_edge('A', 'D', weight=12)
    G.add_edge('B', 'C', weight=35)
    G.add_edge('B', 'F', weight=36)
    G.add_edge('B', 'H', weight=34)
    G.add_edge('C', 'D', weight=4)
    G.add_edge('C', 'E', weight=65)
    G.add_edge('C', 'F', weight=42)
    G.add_edge('D', 'E', weight=33)
    G.add_edge('D', 'I', weight=30)
    G.add_edge('E', 'F', weight=18)
    G.add_edge('E', 'G', weight=23)
    G.add_edge('F', 'G', weight=39)
    G.add_edge('F', 'H', weight=24)
    G.add_edge('G', 'H', weight=25)
    G.add_edge('G', 'I', weight=21)
    G.add_edge('H', 'I', weight=19)
    return G

def dijkstra_shortest_path_tree(G, start_node):
    # finds shortest path tree using Dijkstra
    length, path = nx.single_source_dijkstra(G, start_node)
    return length, path

def minimum_spanning_tree(G):
    # generates the minimum spanning tree using Kruskal
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    return mst

def draw_graph(G, path, title):
    pos = nx.spring_layout(G)

    if title == "Shortest Path Tree":
        plt.figure(figsize=(10, 8))
        
        # original graph
        plt.subplot()
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        # shortest path tree
        edges_in_path = [(path[node][i], path[node][i+1]) for node in path for i in range(len(path[node])-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    else:
        plt.figure(figsize=(10, 5))

        # original graph
        plt.subplot(121)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Original Graph")

        # minimum spanning tree
        plt.subplot(122)
        nx.draw(mst, pos, with_labels=True, node_color='lightblue', edge_color='red')
        labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)

    plt.title(title)
    plt.show()


G = create_weighted_graph()
inp = int(input("1 for shortest path, 2 for minimum spanning tree\n> "))

if inp == 1:
    start_node = 'A'
    length, path = dijkstra_shortest_path_tree(G, start_node)
    draw_graph(G, path, "Shortest Path Tree")

elif inp == 2:
    mst = minimum_spanning_tree(G)
    draw_graph(G, mst, "Minimum Spanning Tree")