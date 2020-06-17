#from collections import defaultdict
def isomorphic(s,t):
    index={}
    word=list(s)
    for i,char in enumerate(s):
        if char in index:
            word[i]=index[char]
        elif t[i] not in index.values():
            index[word[i]]=t[i]
            word[i]=t[i]
            print(index)
    word=''.join(word)
    print(index)
    if word==t:
        return True
    else:
        return False
            
s="paper"
t="title"
w=isomorphic(s,t)

w

x=set(zip(s,t))
y=set(zip(t,s))
print(x,y)
