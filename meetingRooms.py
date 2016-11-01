from heapq import *

def meetingRooms(intervals):
	
	if not intervals:
		return []
	intervals = sorted(intervals, key=lambda intv:intv[0])
	heap = []
	for intv in intervals:
		if not heap:
			heappush(heap, (intv[1], [intv]))
		else:
			top = heappop(heap)
			
			if top[0] > intv[0]:
				heappush(heap, top)
				heappush(heap, (intv[1], [intv]))
			else:
				top[1].append(intv)
				heappush(heap, (intv[1], top[1]))

	res = []
	while heap:
		res.append(heappop(heap)[1])
	return res

def freeTime(meetings):
	"""
	Given a list of meeting times, return free time from 7:00AM-7:00PM
	meetings could have overlapping
	"""
	meetings.sort(key=lambda m:m[0])
	res = []
	end_time = 7
	for m in meetings:
		if m[0]>end_time:
			res.append([end_time, m[0]])
		end_time = max(end_time, m[1])
	if end_time<19:
		res.append([end_time, 19])
	return res

def maxTimestamps(stamps, window):
	i, j = 0, 0
	max_count, count = 0, 0
	max_i, max_j = 0, 0
	for i in range(len(stamps)):
		start = stamps[i]
		while j<len(stamps) and stamps[j]-start<window:
			count+=1
			j+=1
		if max_count<count:
			max_count = count
			max_i, max_j = i, j-1
		count -= 1

	print max_i, max_j, max_count
	length = stamps[max_i]+window-stamps[max_j] 
	return [stamps[max_i]-length, stamps[max_i]]





if __name__ == '__main__':
	# test meeting rooms
	print meetingRooms([[3, 6], [6, 9], [5, 7]])

	# test free time
	print freeTime([[6,10], [9,12], [14,15]])

	# test max time stamps
	stamps = [1, 3, 4, 8, 9, 10, 12, 17]
	print maxTimestamps(stamps, 5)
	
