def reverseVowels(s):
        stack=[]
        out=[]
        for i in range(len(s)):
            if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
                stack.append(i)
        stack.reverse()
        print(stack)
        for j in range(len(s)):
            if j not in stack:
                print(j)
                out.append(s[j])
                print(out)
            else: 
                out.append(s[stack[j]])
        return str(out)
                

a=reverseVowels("hello")
print(a)