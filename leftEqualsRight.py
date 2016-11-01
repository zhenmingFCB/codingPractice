def leftEqualRight(nums):
	"""
	find the index, that make the sum of left part equals right parts
	"""
	total = sum(nums)
	left_s, right_s = 0, total-nums[0]
	for i in range(len(nums)-1):
		if left_s == right_s:
			return i
		left_s += nums[i]
		right_s -= nums[i+1]

	return -1

print leftEqualRight([1,2,3,2,1])
print leftEqualRight([1,2,3,4])
print leftEqualRight([-1,-1,2,-2])
