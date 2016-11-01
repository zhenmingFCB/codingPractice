def isBipartite(graph):
	"""
	Define whether a graph is a bipartite
	undirected, presenting by matrix
	equals to coloring a graph using 2 colors
	"""
	n = len(graph)
	color = 0
	colors = [-1]*n
	colors[0] = 1
	return dfs(graph, colors, 0)

def bfs(graph, colors):
	from collections import deque
	n = len(graph)
	color = 0
	queue = deque()
	queue.append(0)
	colors[0] = 1
	while queue:
		size = len(queue)
		for i in range(size):
			curr = queue.popleft()
			for neighbor in range(curr+1, n):
				if graph[curr][neighbor]==1:
					if colors[neighbor]==-1:
						colors[neighbor]=color
						queue.append(neighbor)
					elif colors[neighbor]==colors[curr]:
						return False
		color = (color+1)%2
	return True

def dfs(graph, colors, i):
	for neighbor in range(i+1, len(graph)):
		if graph[i][neighbor]==0:
			continue
		if colors[neighbor]==-1:
			colors[neighbor]=(colors[i]+1)%2
			if not dfs(graph, colors, neighbor):
				return False
		elif colors[neighbor]==colors[i]:
			return False
	return True


graph = [[1,1,1,1], [0,1,1,0],[0,0,1,0],[0,0,0,1]]
print isBipartite(graph)



