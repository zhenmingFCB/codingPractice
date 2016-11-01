def friendCircle(graph):
	"""
	graph[i][j] == 1 means i and j are friends
	return the number of friendCircles
	"""
	n = len(graph)
	UF = UnionFind(n)
	for i in range(n):
		for j in range(i+1, n):
			if graph[i][j] == 1:
				UF.union(i, j)
	return UF.count

class UnionFind(object):

	def __init__(self, n):
		self.count = n
		self.array = [i for i in range(n)]

	def find(self, i):
		curr = i
		while self.array[curr] != curr:
			curr = self.array[curr]
		self.array[i] = curr
		return curr

	def union(self, i, j):
		root1 = self.find(i)
		root2 = self.find(j)
		if root1 != root2:
			self.count -= 1
			self.array[root1] = root2

	def connect(self, i, j):
		return self.find(i)==self.find(j)


graph = [[1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1]]
print friendCircle(graph)