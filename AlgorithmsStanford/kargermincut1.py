import random
from copy import deepcopy

def randomedge(graph):
    v1=random.choice(list(graph.keys()))
    v2=random.choice(list(graph[v1]))
    
    return (v1,v2)

def kargermincut(graph):
    while len(graph)>2:
        u,v=randomedge(graph)
        graph[u].extend(graph[v])
        
        for vertex in graph[v]:
            graph[vertex].remove(v)
            graph[vertex].append(u)
            
        while u in graph[u]:
            graph[u].remove(u)
        
        del graph[v]
        
    length=[len(graph[key]) for key in graph.keys()]
    return length[0]



file="kargermincut.txt"
graph={}
with open(file) as f:
    for line in f.readlines():
        vertices=line.split()
        graph[vertices[0]]=vertices[1:]

mincut=kargermincut(deepcopy(graph))
print("Mincut in iteration",1,"is",mincut)
a=[mincut]
for i in range(len(graph.keys())):
    print("Mincut in iteration",i,"is",mincut)
    cut=kargermincut(deepcopy(graph))
    if cut < mincut:
        mincut = cut
    a.append(mincut)    
    if i>25:
        if(a[i-20]==a[i-1]):
            break

print("Final mincut",mincut)
