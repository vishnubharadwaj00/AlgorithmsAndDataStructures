from random import choice
from copy import deepcopy
from time import time

def load_graph(graph, file_name):
    with open("kargermincut.txt") as g_file:
        for line in g_file.readlines():
            vertices = line.split()
            graph[vertices[0]] = vertices[1:]
            
def get_random_edge(graph):
    v1=choice(list(graph.keys()))
    v2=choice(list(graph[v1]))
    
    return (v1,v2)

def karger_algorithm(graph):
    while len(graph)>2:
        (v1,v2)=get_random_edge(graph)
        graph[v1].extend(graph[v2])

        for vertex in graph[v2]:
            graph[vertex].remove(v2)
            graph[vertex].append(v1)
            
        while v1 in graph[v1]:
            graph[v1].remove(v1)
            
        del graph[v2]
        
    length=[len(graph[key]) for key in graph.keys()]
    return length[0]

def main():

    file_name = "kargermincut.txt"

    graph = {}

    load_graph(graph, file_name)

    initial_time = time()
    min_cut = karger_algorithm(deepcopy(graph))
    for i in range(len(graph.keys())):
        cut = karger_algorithm(deepcopy(graph))
        min_cut = cut < min_cut and cut or min_cut

    final_time = time()

    print("Minimum cut count:", min_cut)
    print("TIME TAKEN to find the minimum cut: %.5ss" %
          (final_time - initial_time))


main()