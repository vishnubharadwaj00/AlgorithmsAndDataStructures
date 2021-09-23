def isIsomorphic(s,t):
        if(s==None or t==None or len(s) != len(t)):
            return False
        
        dic = {}
        
        for i in range(0,len(s)):
            print(dic)
            if s[i] in dic:
                if t[i] != dic[s[i]]:
                    return False
            elif t[i] in dic.values():
                return False
            else:
                dic[s[i]]=t[i]
        return True

a = isIsomorphic("paper","title")
print(a)


                