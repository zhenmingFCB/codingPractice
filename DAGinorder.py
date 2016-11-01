class Node(object):

	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def inorder(root, k):
	count = 0
	stack = []
	stack.append((root, False))
	while stack:
		curr, visited = stack.pop()
		if visited:

			count += 1
			print curr.val, count
			if count == k:
				return curr
			if curr.right is not None:
				stack.append((curr.right, False))
		else:
			stack.append((curr, True))
			if curr.left is not None:
				stack.append((curr.left, None))


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.left = node2
node1.right = node3
node2.right, node3.left = node4, node4

print inorder(node1, 3).val



