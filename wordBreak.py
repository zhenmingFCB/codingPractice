def wordBreakWays(n):
	dp = [0]*(n+1)
	dp[0] = 1
	for i in range(1, n+1):
		for j in range(i):
			dp[i] += dp[i-1-j]*dp[j]
	return dp[-1]

def wordBreak(word, dictionary):
	"""
	dp[word] = # of ways break word
	"""
	dp = dict()
	dp[''] = ['']
	return helper(word, dictionary, dp)

def helper(word, dictionary, dp):
	if word in dp:
		return dp[word]

	res = []
	for i in range(len(word)):
		if word[:i+1] in dictionary:
			partial_break = helper(word[i+1:], dictionary, dp)
			for rest in partial_break:
				if rest=='':
					res.append(word[:i+1])
				else:
					res.append(word[:i+1]+' '+rest)
	dp[word] = res
	return res


print wordBreakWays(4)

dictionary = {'i', 'love', 'ny', 'ilove', 'loveny'}
print wordBreak('iloveny', dictionary)
