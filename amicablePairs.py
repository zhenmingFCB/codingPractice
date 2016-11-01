def amicablePairs(n):
	"""
	Find all amicablePairs less than n
	"""
	dp = [1]*(n+1)
	for i in range(2, n/2+1):
		for j in range(i+i, n+1, i):
			dp[j] += i

	res = []
	for i, num in enumerate(dp):
		if num<n and i==dp[num] and i<num:
			res.append([i, num])
	return res

print amicablePairs(300)

