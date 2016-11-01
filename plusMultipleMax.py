
def onlyPlusAndMultiple(nums):
	dp = [0]*len(nums)
	dp[0] = nums[0]
	for i in range(1, len(nums)):
		dp[i] = nums[i]*dp[i-1]

	for i in range(1, len(nums)):
		last = 1
		for j in range(i-1, -1, -1):
			last = last*nums[j+1]
			dp[i] = max(dp[i], dp[j]+last) 

	return dp[-1]

def plusMulitpleBracket(nums):
	expression = dict()
	dp = [[0]*len(nums) for _ in range(len(nums))]
	for i in range(len(nums)):
		dp[i][i] = nums[i]
		expression[(i,i)] = str(nums[i])

	for length in xrange(2, len(nums)+1):
		for start in xrange(0, len(nums)+1-length):
			max_value, max_expression = 0, ''
			for mid in xrange(start, start+length-1):
				if dp[start][mid]*dp[mid+1][start+length-1] > dp[start][mid]+dp[mid+1][start+length-1] and dp[start][mid]*dp[mid+1][start+length-1]> max_value:
					max_expression = expression[(start,mid)]+'*'+expression[(mid+1,start+length-1)]
				elif dp[start][mid]*dp[mid+1][start+length-1] < dp[start][mid]+dp[mid+1][start+length-1] and dp[start][mid]+dp[mid+1][start+length-1]> max_value:
					left_exp = expression[(start,mid)]
					if left_exp[-1] == ')':
						left_exp = left_exp[1:-1]

					right_exp = expression[(mid+1,start+length-1)]
					if right_exp[0] == '(':
						right_exp = right_exp[1:-1]

					max_expression = '('+left_exp+'+'+right_exp+')'

				max_value = max(max_value, dp[start][mid]*dp[mid+1][start+length-1], dp[start][mid]+dp[mid+1][start+length-1])
			dp[start][start+length-1] = max_value
			expression[(start,start+length-1)] = max_expression
	print expression[(0, len(nums)-1)]
	return dp[0][-1]

if __name__ == '__main__':
	print(plusMulitpleBracket([4,2,0.1,5,8]))