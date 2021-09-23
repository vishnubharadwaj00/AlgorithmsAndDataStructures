def longestCommonPrefix(strs)
    lcp=[]
    if (len(strs)==0):
        return ''.join(lcp)
        
    index = 0
    for c in list(strs[0]):
        for i in range(1,len(strs)):
            if(index >= len(strs[i]) or c!=strs[i][index]):
                return lcp
        lcp.append(c)
        index+=1
        
    return str(lcp)

a=longestCommonPrefix(["flower","flow","flight"])
print(a)