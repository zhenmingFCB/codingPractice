from collections import deque
from heapq import *

def minPath(matrix,start, dest):
	"""
	0:wall 1:path
	"""

	if matrix[start[0]][start[1]]!=1:
		return []

	m, n = len(matrix), len(matrix[0])
	visited = dict()
	queue = deque()
	queue.append(start)
	visited[start] = start
	directions = [(1,0),(0,1),(-1,0),(0,-1)]

	while queue:
		curr = queue.popleft()
		for di in directions:
			next = (curr[0]+di[0], curr[1]+di[1])
			if next in visited:
				continue
			if next[0]<m and next[0]>=0 and next[1]<n and next[1]>=0 and matrix[next[0]][next[1]]==1:
				visited[next] = curr
				queue.append(next)
				if next==dest:
					temp = next
					res = []
					while visited[temp]!=temp:
						res.append(temp)
						temp = visited[temp]
					res.append(temp)
					res.reverse()
					return res
	return []

def minPathBreaking(matrix, start, dest):
	"""
	0:wall 1:path
	We can break wall, but pay for cost 1
	"""
	m, n = len(matrix), len(matrix[0])
	visited = dict()
	queue = []
	heappush(queue, (matrix[start[0]][start[1]], start))
	visited[start] = start
	directions = [(1,0),(0,1),(-1,0),(0,-1)]

	while queue:
		cost, curr = heappop(queue)
		for di in directions:
			next = (curr[0]+di[0], curr[1]+di[1])
			if next in visited:
				continue
			if 0<=next[0]<m and 0<=next[1]<n:
				cost += matrix[next[0]][next[1]]
				visited[next] = curr
				heappush(queue, (cost, next))
				if next==dest:
					temp = next
					path = []
					while visited[temp]!=temp:
						path.append(temp)
						temp = visited[temp]
					path.append(temp)
					path.reverse()
					print path
					return cost
	return -1



if __name__ == '__main__':
	matrix = [[1,0,0],[1,1,0],[0,1,1]]

	matrix2 = [[1,0,0],[1,0,0],[0,1,1]]
	print minPathBreaking(matrix2, (0,2), (2,0))




