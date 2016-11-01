class Solution(object):
	def stringCombination(self, input1, input2):
		self.res = []
		count = 0
		self.charSum = len(input1)
		input_hist = [0]*26

		for c in input1:
			input_hist[ord(c)-ord('A')]+=1

		self.dfs(input_hist, input2, 0, count, [])
		return self.res

	def dfs(self, target, source, pos, count, tempRes):
		if count>self.charSum:
			return

		if count==self.charSum:
			tempHist = target[:]
			for word in tempRes:
				for c in word:
					tempHist[ord(c)-ord('A')] -= 1
					if tempHist[ord(c)-ord('A')]<0:
						return
			self.res.append(tempRes[:])
			return

		for idx in range(pos, len(source)):
			tempRes.append(source[idx])
			self.dfs(target, source, idx+1, count+len(source[idx]), tempRes)
			tempRes.pop()

if __name__ == '__main__':
	input1 = 'CATDOG'
	input2 = ['CAT','DOG', 'CD', 'GOAT','BAD', 'COOL	']
	solution = Solution()
	print solution.stringCombination(input1, input2)


