def minSquareMax(nums):
	"""
	delete from left, delete how many times so that min^2<max
	"""
	n = len(nums)
	mins, maxs = [0]*n, [0]*n
	for i in range(n-1, -1, -1):
		num = nums[i]
		if i==n-1:
			mins[i], maxs[i] = num, num
		else:
			mins[i] = min(mins[i+1], num)
			maxs[i] = max(maxs[i+1], num)

	for i in range(n):
		if mins[i]**2 < maxs[i]:
			return i
	return -1

def minSquareMax2(nums):
	"""
	delete from left or right, delete how many times so that min^2<max
	"""
	n = len(nums)
	mins_right, maxs_right = [0]*n, [0]*n
	mins_left, maxs_left = [0]*n, [0]*n
	for i in range(n):
		if i==0:
			mins_left[0], maxs_left[0] = nums[i], nums[i]
			mins_right[-1], maxs_right[-1] = nums[-1], nums[-1]
		else:
			mins_left[i] = min(mins_left[i-1], nums[i])
			maxs_left[i] = max(maxs_left[i-1], nums[i])
			mins_right[n-1-i] = min(mins_right[n-i], nums[n-1-i])
			maxs_right[n-1-i] = max(maxs_right[n-i], nums[n-1-i])

	i, j = 0, n-1
	
	return -1

print minSquareMax([1])
print minSquareMax([1,2,3,4,5])
print minSquareMax([10,9,8,7])
print minSquareMax([-9,-7,-5,-3,5,7,9,10])
print minSquareMax([-9,3,5,7,10,-7])
