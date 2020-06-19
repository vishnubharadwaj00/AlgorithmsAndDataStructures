def lengthoflongestsubstring(s):
    if len(s)==0 or len(s)==1:
        return len(s)
    else:
        length_list=[]
        for i in range(0,len(s)):
            longest=[s[i]]
            length=1
            for j in range(i+1,len(s)):
                if s[j] not in longest:
                    longest.append(s[j])
                    length+=1
                    if(j==len(s)-1):
                        length_list.append(length)
                else:
                    length_list.append(length)
                    break
                    
        print(length_list)
        return max(length_list)
            
x=lengthoflongestsubstring("pprstlmpm")
x