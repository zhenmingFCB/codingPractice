def combinationSum(nums, target):
	res = []
	nums.sort()
	backtracking(nums, target, res, [])
	return res

def backtracking(nums, target, res, curr):
	if target==0:
		res.append(curr[:])
	temp = nums[0]
	for idx in range(len(nums)):
		if nums[idx]>target:
			return
		if idx>0 and nums[idx]==temp:
			continue
		curr.append(nums[idx])
		backtracking(nums, target-nums[idx], res, curr)
		curr.pop()

nums = [1,2,3]
print combinationSum(nums, 4)


