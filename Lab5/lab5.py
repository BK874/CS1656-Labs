#Brian Knotten
#CS166
#Lab 5
import networkx as nx
import matplotlib.pyplot as plt
import sys

def minMaxDegree(graph, num):
    maxDegree = 0
    minDegree = sys.maxsize
    for node in graph.nodes():
        if graph.degree(node) > maxDegree:
            maxDegree = graph.degree(node)
        if graph.degree(node) < minDegree:
            minDegree = graph.degree(node)
    print("Max graph", num, "degree:", maxDegree)
    print("Min graph", num, "degree:", minDegree)
    return [minDegree, maxDegree]

# Task 1: Given code generating three graphs, compute the degree for each node and
# report the highest and lowest degree over all nodes for each graph
graph1 = nx.barabasi_albert_graph(30, 4)
nx.draw(graph1, with_labels=True)
plt.show()

graph2 = nx.erdos_renyi_graph(30, 0.15)
nx.draw(graph2, with_labels=True)
plt.show()

graph3 = nx.complete_bipartite_graph(3, 5)
nx.draw(graph3, with_labels=True)
plt.show()

minMaxDegree(graph1, 1)
minMaxDegree(graph2, 2)
minMaxDegree(graph3, 3)

# Task 2: Create a directional graph with 5 nodes, 10 edges, and at least
# one node with a single outgoing edge and no incoming edges
DG = nx.DiGraph()
newnodes = (1,2,3,4,5)
newedges = [(1,2), (1,3), (1,4), (2,1), (2,3), (3,4), (3,2), (4,2), (4,3), (5,1)]
DG.add_nodes_from(newnodes)
DG.add_edges_from(newedges)
nx.draw_shell(DG, with_labels=True)
plt.show()

# Task 3: For each node in your generated graph, compute the number of nodes
# reachable using a BFS traversal starting at that node
for i in range(1, 6):
    print("Starting at node", i, "the reachable nodes are:")
    alledges = nx.bfs_edges(DG, i)
    edgelist = list(alledges)
    for u, v in edgelist:
        print(v)

    
