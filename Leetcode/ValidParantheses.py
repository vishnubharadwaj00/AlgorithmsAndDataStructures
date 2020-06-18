word = str(input())
s = list(word)
n = len(s)
stack = []
top = -1
flag = 0
for i in range(0, n):
    if(s[i] == "(" or s[i] == "{" or s[i] == "["):
        stack.append(s[i])
        top += 1
    else:
        if(top == -1):
            flag = 1
            break
        elif((s[i] == ")" and stack[top] == "(") or (s[i] == "]" and stack[top] == "[") or (s[i] == "}" and stack[top] == "{")):
            stack.pop(top)
            top -= 1
        else:
            flag = 1
            break
    print(top)
    print(stack)
if(top == -1 and flag == 0):
    print(True)
else:
    print(False)
