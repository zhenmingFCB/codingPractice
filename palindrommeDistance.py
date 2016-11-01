def palindromeDistance(string):
	str2 = string[::-1]
	dp = editDistance(string, str2)

	res = len(string)
	n = len(string)
	for i in range(1, len(string)+1):
		res = min(res, dp[i][n-1-i])
	return res




def editDistance(str1, str2):
	m, n = len(str1)+1, len(str2)+1
	dp = [[0] * n for i in range(m)]
	for i in range(m):
		dp[i][0] = i

	for j in range(n):
		dp[0][j] = j
	for i in range(1, m):
		for j in range(1, n):

			if str1[i-1]==str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
	return dp

print palindromeDistance('caba')

