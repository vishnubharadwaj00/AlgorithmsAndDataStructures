def lengthOfLongestSubstring(s):
	if len(s) == 0: 
		return 0
	p1 = 0
	p2 = 0
	maxlen = 1 
	seen = set()
	while p2<len(s):
		if s[p2] not in seen:
			seen.add(s[p2])
			p2+=1
			maxlen = max(maxlen,len(seen))
		else: 
			seen.remove(s[p1])
			p1+=1
	print(maxlen)

lengthOfLongestSubstring("bbbbbb")