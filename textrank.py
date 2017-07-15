from nltk.tokenize import sent_tokenize
import networkx as nx
import math
import matplotlib.pyplot as plt
def sentences(text):
    '''Break text blob into sentences'''
    return sent_tokenize(text,language='norwegian')

def connect(nodes):
    '''Return a list of edges connecting the nodes, where the edges are given a
    weight based on their similarity.'''
    return [(start,end ,similarity(start, end)) for start in nodes for end in nodes if start is not end]

def similarity(c1,c2):
    '''Return the amount of similarity between two chunks.'''
    return len(common_words(c1, c2))/(math.log(len(c1))+math.log(len(c2)))

def common_words(c1,c2):
    elem1 = [x for x in c1.split()]
    elem2 = [x for x in c2.split()]
    #print (c1)
    #print(c2)
    c3=list()
    for item in elem1:
        if item in elem2:
            c3.append(item)
    #print(c3)
    return c3

def rank(nodes,edges):
    '''Return a dicitionary containing the scores for each vertex.'''
    graph=nx.diamond_graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    return nx.pagerank(graph)

def summarize(text,num_summaries=6):
    '''Create small summaries of larger text.'''
    nodes=sentences(text)
    edges=connect(nodes)
    print(edges)
    print(nodes)
    scores=rank(nodes,edges)
    print (scores)
    return sorted(scores,key=scores.get)[:num_summaries]

text= """"""

summary=summarize(text)
summary=str(summary).replace('\',','')
summary=summary.replace('\'','')
summary=summary.replace('[','')
summary=summary.replace(']','')

print (summary)