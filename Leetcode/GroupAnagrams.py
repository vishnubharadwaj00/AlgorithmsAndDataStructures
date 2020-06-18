import collections
strs=list(map(str,input().split()))
ans = collections.defaultdict(list)
for s in strs:
print(ans.values())
