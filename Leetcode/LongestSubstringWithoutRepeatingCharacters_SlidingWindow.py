def longestsubstring(s):
    used={}
    start=maxlength=0
    
    for i,c in enumerate(s):
        if c in used and start<=used[c]:
            start=used[c]+1
        else:
            maxlength=max(maxlength,i-start+1)
        used[c]=i
    return maxlength

x=longestsubstring("abcabcaa")
