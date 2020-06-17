# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:13:11 2020

@author: Vishnu
"""
from collections import defaultdict

def add_edge(G,u,v):
    G[u].append(v)
    return G

def BFS(G,s):
    visited=[0]*len(G)
    visited[s]=1
    
    Q=[]
    Q.append(s)
    while len(Q)!=0:
        x=Q.pop(0)
        print(x,end= " ")
        for i in G[x]:
            if(visited[i]!=True):
                Q.append(i)
                visited[i]=True

G=defaultdict(list)
G=add_edge(G,0,1)
G=add_edge(G,0,2)
G=add_edge(G,1,2)
G=add_edge(G,2,0)
G=add_edge(G,2,3)
G=add_edge(G,3,3)

BFS(G,1)

