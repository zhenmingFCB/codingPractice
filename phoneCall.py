def makePhoneCall(nums):
	needToCall = dict()
	for i in range(len(nums)):
		needToCall[i] = []
	needToCall[-1] = []
	for i in range(len(nums)-1, -1, -1):

		# calculate for self
		totalTime = 0
		callers = sorted(needToCall[i], key=lambda x:-x)
		for j in range(len(callers)):
			totalTime = max(callers[j]+j+1, totalTime)

		curr = nums[i]
		needToCall[curr].append(totalTime)

	print needToCall
	return needToCall[-1]

nums1 = [-1,0,0]
nums2 = [-1,0,0,2,2]
nums3 = [-1,0,1,2,3]
nums4 = [-1,0,0,1,1,1,2,2,3,3,4,4,5,5,6,7,7,8,12,13,14,16,16,16]
print makePhoneCall(nums1)
print makePhoneCall(nums2)
print makePhoneCall(nums3)
print makePhoneCall(nums4)
