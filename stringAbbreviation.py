def stringAbbreviation(strings):
	from collections import defaultdict
	sortedStrings = sorted(strings, key=lambda s:(len(s), s[0]+s[-1], s))
	print sortedStrings
	res = []
	abbreved = defaultdict(int)
	for i, s in enumerate(sortedStrings):
		prefix = 0
		if i<len(strings)-1 and s[-1]==sortedStrings[i+1][-1] and s[0]==sortedStrings[i+1][0]:
			for j in range(len(s)):
				if s[j]==sortedStrings[i+1][j]:
					prefix+=1
				else:
					break
			abbreved[s] = max(abbreved[s], prefix)
			abbreved[sortedStrings[i+1]] = prefix


	for s in strings:
		if len(s)<=abbreved[s]+2+len(str(len(s))):
			res.append(s)
		else:
			res.append(s[:abbreved[s]+1]+str(len(s))+s[-1])
		
	return res

strings = ['like', 'god', 'internal', 'me', 'internet', 'interval', 'intension', 'face', 'intrusion']
strings2 = ['intabcxyz', 'intdecxyz', 'intdfcxyz']
print stringAbbreviation(strings)