import networkx as nx
from pyvis.network import Network
from operator import itemgetter
import matplotlib.pyplot as plt


def build_word_network(input_text):
    G = nx.Graph()
    for x in range(0, len(input_text.split())):
        window = input_text.split()[x:x+4]
        if len(window) ==4:
            G.add_edge(window[0], window[1], weight=3)
            G.add_edge(window[0], window[2], weight=2)
            G.add_edge(window[0], window[3], weight=1)

            
    ## Scale nodes by naive Degree
    scale=2 # Scaling the size of the nodes by 10*degree
    d = dict(G.degree)

    #Updating dict
    d.update((x, scale*y) for x, y in d.items())

    #Setting up size attribute
    nx.set_node_attributes(G,d,'size')
    
    return G

def top_bet_cen(G, n):
    bet_centrality = nx.betweenness_centrality(G, normalized = True, 
                                              endpoints = False)
    return dict(sorted(bet_centrality.items(), key = itemgetter(1), reverse = True)[:n])

def top_close_cen(G, n):
    closeness_centrality = nx.closeness_centrality(G)
    return dict(sorted(closeness_centrality.items(), key = itemgetter(1), reverse = True)[:n])

def top_PR_cen(G, alpha=0.8, n=5):
#     closeness_centrality = nx.closeness_centrality(G)
    pr = nx.pagerank(G, alpha = 0.8)
    return dict(sorted(pr.items(), key = itemgetter(1), reverse = True)[:n])

def pyvis_from_nx(G):
    nt = Network('1000px', '750px', notebook=True)
    nt.from_nx(G)
    
    return nt