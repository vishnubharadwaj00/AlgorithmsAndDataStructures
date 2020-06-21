def repeatedsubstring(s):
    start=0
    end=1
    if(len(s)==1):
        return False
    while(end<=len(s)//2 if len(s)%2==0 else end<=len(s)//2+1):
        flag=0
        sub=s[start:end]
        sublen=len(sub)
        print(sub)
        for i in range(end,len(s),sublen):
            if (s[i:i+sublen]!=sub):
                end+=1
                flag=1
                break
        if(flag==0):
            return True
    return False

repeatedsubstring("ab")