from collections import defaultdict
def stringAnagram(target, pattern):
	diff = defaultdict(int)
	if len(target)<len(pattern):
		return False
	for c in pattern:
		diff[c]+=1
	for c in target[:len(pattern)]:
		diff[c]-=1
		if diff[c]==0:
			del diff[c]

	for start in range(len(target)-len(pattern)):
		if start>0:
			diff[target[start-1]] += 1
			if diff[target[start-1]]==0:
				del diff[target[start-1]]
			diff[target[start+len(pattern)-1]] -= 1
			if diff[target[start+len(pattern)-1]]==0:
				del diff[target[start+len(pattern)-1]]
		if len(diff)==0:
			print target[start:start+len(pattern)]
			return True
	return False

print stringAnagram('caabbd','abab')