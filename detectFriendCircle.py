import unittest
class Snap(object):

	def __init__(self, val):
		self.next = []
		self.val = val
	
	def dectCircle(self):
		# dfs with pruning
		visited = set()
		if dfs(self, visited, []):
			return True
		else:
			return False

def dfs(snap, visited, path):
	for friend in snap.next:
		if friend in visited:
			continue
		if friend in path:
			return True
		else:
			path.append(friend)
			if dfs(friend, visited, path):
				return True
	visited.add(snap)
	return False	


class myTest(unittest.TestCase):
	def test(self):
		snap1, snap2, snap3, snap4, snap5 = Snap(1), Snap(2), Snap(3), Snap(4), Snap(5)
		snap1.next = [snap2, snap3, snap4]
		snap2.next = [snap3, snap4]
		snap3.next = [snap4]
		snap4.next = [snap3]
		self.assertTrue(snap1.dectCircle())

unittest.main()