import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_graph():
    G = nx.Graph()
    # Add edges along with their weights
    G.add_edge('A', 'B', weight=4)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('B', 'D', weight=5)
    G.add_edge('C', 'D', weight=8)
    G.add_edge('C', 'E', weight=10)
    G.add_edge('D', 'E', weight=2)
    G.add_edge('D', 'F', weight=6)
    G.add_edge('E', 'F', weight=3)
    return G

def dijkstra_shortest_path_tree(G, start_node):
    # finds shortest path tree using Dijkstra
    length, path = nx.single_source_dijkstra(G, start_node)
    return length, path

def minimum_spanning_tree(G):
    # generates the minimum spanning tree using Kruskal
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    return mst

def draw_graph(G, path=None):
    if path is not None:
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 8))
        
        # original graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        # shortest path tree
        edges_in_path = [(path[node][i], path[node][i+1]) for node in path for i in range(len(path[node])-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='r', width=2)
        
        plt.title("Shortest Path Tree using Dijkstra's Algorithm")
        plt.show()
    else:
        pos = nx.spring_layout(G)  # Positions for all nodes
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("title")
        plt.show()


G = create_weighted_graph()
inp = int(input("1 for shortest path, 2 for minimum spanning tree\n> "))

if inp == 1:
    start_node = 'A'
    length, path = dijkstra_shortest_path_tree(G, start_node)
    draw_graph(G, path)

elif inp == 2:
    mst = minimum_spanning_tree(G)
    draw_graph(G)
    draw_graph(mst)