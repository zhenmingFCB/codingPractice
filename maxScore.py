class Person(object):
	def __init__(self, score):
		self.score = score
		self.nextSnap = []

class Solution(object):
	max_score = 0
	def maxScore(self, person, maxStep):
		self._maxScore(person, maxStep, dict(), [])
		return self.max_score

	def _maxScore(self, person, maxStep, visited, path):
		self.max_score = max(self.max_score, person.score)
		if maxStep==0:
			return
		path.append(person)
		for friend in person.nextSnap:
			if friend in path:
				continue
			if friend in visited and maxStep<=visited[friend]:
				continue
			self._maxScore(friend, maxStep-1, visited, path)
		visited[person] = maxStep
		path.pop()


	def printFriends(self, person):
		visited = set()
		self.dfs(person, visited)
		return [i.score for i in visited]

	def dfs(self, person, visited):
		visited.add(person)
		for friend in person.nextSnap:
			if friend in visited:
				continue
			self.dfs(friend, visited)



P1=Person(1)
P2=Person(2)
P3=Person(3)
P4=Person(4)
P1.nextSnap = [P2,P3]
P2.nextSnap = [P3,P1]
P3.nextSnap = [P4,P1]
solution = Solution()
print solution.maxScore(P2,2)
print solution.printFriends(P1)

