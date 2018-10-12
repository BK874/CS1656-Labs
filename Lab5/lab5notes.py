import networkx as nx
import matplotlib.pyplot as plt
import nltk

# Create simple undirectional graph
G = nx.Graph()
# Add nodes 4 and 8
G.add_node(4)
G.add_node(8)
# Add edge connecting 4 and 8
G.add_edge(4,8)
# View graph
# nx.draw(G, with_labels = True)
# plt.show()
# Add nodes and edges in bulk
mynodes = [1, 2, 3, 5, 6, 7]
myedges = [(1,2), (3,4), (5,6), (7, 8)]
G.add_nodes_from(mynodes)
G.add_edges_from(myedges)
# View graph
# nx.draw(G, with_labels = True)
# plt.show()
# Simple stats on graph
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
# View list of all nodes and edges
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))
# Get list of edges from a specific nodes or specific nodes
print("Edges in/out of node 4:", list(G.edges(4)))
print("Edges in/out of nodes 4 and 5:", list(G.edges([4,5])))
# Add more edges and nodes
myedges2 = [(1,3),(1,4),(2,5),(2,6),(2,7),(2,8)]
G.add_edges_from(myedges2)
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))
# Two ways to find nodes adjacent to a node
print("Nodes adjacent to node 1:", list(G.adj[1]))
print("Nodes neighboring node 1:", list(G.neighbors(1)))
# Find the degree of a node
print("Degree of nodes 1, 2:", G.degree([1, 2]))
# Add attributes to all nodes
for i in list(G.nodes()):
    print ("Node:",i)
    G.node[i]['color'] = 'Blue'
    print ("Node:",G.node[i])

# Create directed graph
DG = nx.DiGraph()
newnodes = (1,2,3,4,5,6,)
newedges = [(1,2),(2,3),(3,4),(4,3),(4,5),(5,6),(4,6),(3,6),(6,2)]
DG.add_nodes_from(newnodes)
DG.add_edges_from(newedges)
print("Nodes:", list(DG.nodes()))
print("Edges:", list(DG.edges()))
# View Directed graph
nx.draw_shell(DG, with_labels=True)
plt.show()
# Breadth-frist traversal of the directed graph from node 1
root = 1
all_edges = nx.bfs_edges(DG, root)
edgelist = list(all_edges)
print("Edge List:", edgelist)
# Easily understood version:
print(root)
for u, v in edgelist:
    print(v)
# Compact version
nodes = [root] + [v for u, v in edgelist]
print(nodes)
print(dict(nx.bfs_successors(DG, root)))

# NLTK and Stemming:
# Stemming typically refers to a crude heuristic process that chops off the ends
# of words to hopefully achieve this goal (???) most of the time and often
# includes the removal of derivational affixes
mysentence = """During a manned mission to Mars, Astronaut Mark Watney 
            (Matt Damon) is presumed dead after a fierce storm and left behind 
            by his crew.But Watney has survived and finds himself stranded and
alone on the hostile planet."""
mysentencetokens = nltk.word_tokenize(mysentence)
# Stemming
porter = nltk.PorterStemmer()
looper = 0
for token in mysentencetokens:
    mysentencetokens[looper] = porter.stem(token)
    looper += 1
print("Stemmed -->")
print(mysentencetokens)

