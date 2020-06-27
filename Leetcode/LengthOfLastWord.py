def lengthoflastword(s):
    end = len(s)-1
    length = 0
    if(len(s) == 0 or s.isspace() == True):
        return 0
    if(len(s) == 1):
        return 1
    while(end != 0):
        length += 1
        end -= 1
        if(s[end] == ' '):
            return length
    return 0


x = lengthoflastword("a ")
print(x)
