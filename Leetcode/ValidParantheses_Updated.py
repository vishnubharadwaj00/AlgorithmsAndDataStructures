s = str(input())
s = list(s)
stack = []
mapping = {")": "(", "}": "{", "]": "["}

for char in s:
    if char in mapping:
        top_element = stack.pop() if stack else '#'
        if mapping[char] != top_element:
            print(False)
    else:
        stack.append(char)
print(not stack)
