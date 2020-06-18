s = str(input())
s = list(s)
lst = []
index = []
for i in range(0, len(s)):
    if(s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u"):
        lst.append(s[i])
        index.append(i)
lst = lst[::-1]
top = 0
for i in range(0, len(s)):
    if i in index:
        s[i] = lst[top]
        top += 1
st = ''.join(s)
print(st)
