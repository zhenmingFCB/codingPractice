class XMLParser(object):

	def __init__(self, doc):
		self.doc = doc.split()
		self.i = 0

	def __iter__(self):
		return self

	def next(self):
		if self.i < len(self.doc):
			curr = self.doc[self.i]
			self.i += 1
			if curr[0] != '<':
				return curr, 'text'
			else:
				if curr[1] == '/':
					return curr[2:-1], 'end'
				else:
					return curr[1:-1], 'start'
			
		else:
			raise StopIteration()

class TreeNode(object):
	def __init__(self, label):
		self.children = []
		self.label = label

	def __repr__(self):
		res = self.label
		for child in self.children:
			res += ' '+str(child)

		return res


def parse(xmlParser):
	stack = []
	curr = None
	for label, token in xmlParser:
		if token == 'start':
			curr = TreeNode(label)
			if stack:
				stack[-1].children.append(curr)
			stack.append(curr)
		elif token == 'text':
			curr = TreeNode(label)
			if stack:
				stack[-1].children.append(curr)
		else:

			curr = stack.pop()
	return curr

doc = """
<a>
	<b>
		<c> hello </c>
	</b>
	<d>
		<e> world </e>
	</d>
</a>
"""
xmlParser = XMLParser(doc)
root = parse(xmlParser)
print root