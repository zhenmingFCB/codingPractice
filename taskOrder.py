class Task(object):
	def __init__(self, message):
		self.message = message
		self.dependency = []

	def execute(self):
		print 'execute: '+str(self.message)

def taskOrder(tasks):
	from collections import deque,defaultdict
	n = len(tasks)
	degrees = dict()
	graph = defaultdict(list)
	queue = deque()
	for t in tasks:
		degrees[t] = len(t.dependency)
		for depend in t.dependency:
			graph[depend].append(t)
		if degrees[t]==0:
			del degrees[t]
			queue.append(t)

	while queue:
		curr = queue.popleft()
		curr.execute()
		for next_task in graph[curr]:
			degrees[next_task] -= 1
			if degrees[next_task]==0:
				del degrees[next_task]
				queue.append(next_task)
	if degrees:
		raise Exception('Has Circle')


t1,t2,t3,t4 = Task(1), Task(2), Task(3), Task(4)
t4.dependency += [t2, t3]
t2.dependency.append(t1)
t3.dependency.append(t1)
#t1.dependency.append(t4)
taskOrder([t1,t2,t3,t4])






