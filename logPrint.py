def parseLog(logs):
	
	stack = []
	curr = 0
	res = []
	for i, log in enumerate(logs.split('\n')):
		if log=='':
			continue
		job, status, ts = log.split(' ')
		time_stamp = int(ts)

		if not stack:
			stack.append([job, 0])
		else:
			if status == 'start':
				stack[-1][1] += time_stamp-curr
				stack.append([job, 0])
			else:
				ended, time = stack.pop()

				res.append(ended+':'+str(time_stamp-curr+time))
		curr = time_stamp

	return res[::-1]

	
log = """
f1 start 0
f2 start 2
f3 start 4
f3 end 5
f2 end 8
f1 end 9
"""
print log.split('\n')
print parseLog(log)
