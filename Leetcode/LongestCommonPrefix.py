strs=["flower","flow","flop"]

def lowestcommonprefix(strs):
    if not strs:
        return ""
    shortest_str=min(strs,key=len)
    for i,char in enumerate(shortest_str):
        for strings in strs:
            if strings[i]!=char:
                return shortest_str[:i]
    return shortest_str

a=lowestcommonprefix(strs)
print(a)
    