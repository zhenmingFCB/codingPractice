class Employee(object):
	def __init__(self, name, manager, sold):
		self.name = name
		self.manager = manager
		self.sold = sold
		self.subs = []

	def __repr__(self):
		return self.name

class Company(object):
	def __init__(self, employees):
		self.ceo = employees[0]
		for e in employees:
			if e.manager == None:
				self.ceo = e
			else:
				e.manager.subs.append(e)

	def printHierachy(self):
		self.postOrder(self.ceo)

		# preorder print
		self.preOrder(self.ceo, '')

	

	def preOrder(self, node, prefix, last=False):
		print prefix+node.name+' '+str(node.sold)
		if len(prefix)>1:
			if last:
				prefix = prefix[:-2]+'  '
			else:
				prefix = prefix[:-2]+'| '
		for i, child in enumerate(node.subs):
			if i == len(node.subs)-1:
				self.preOrder(child, prefix+'\_', True)
			else:
				self.preOrder(child, prefix+'|-')

	def postOrder(self, node):
		for sub in node.subs:
			if sub:
				node.sold += self.postOrder(sub)
		return node.sold

	def commanAncestor(self, employee1, employee2):

		if employee1==self.ceo or employee2==self.ceo:
			return self.ceo
		# n order tree post order traversal
		def postOrder(node, path1, path2):
			if node==employee1:
				self.found += 1
				if not path2:
					for p in path1:
						path2.append(p)
					path2.append(node)
				
			elif node==employee2:		
				self.found += 1
				if not path2:
					for p in path1:
						path2.append(p)
					path2.append(node)
				
			if self.found == 2:
				path1.append(node)
				print 'found path:'
				print path1, path2
				# compare two path:
				for i in range(min(len(path1), len(path2))):
					if path1[i]!=path2[i]:
						self.reporter = path1[i-1]
						return
				if len(path1)<len(path2):
					self.reporter = path1[-1]
					return
				else:
					selr.reporter = path2[-1]
					return

			path1.append(node)
			for child in node.subs:
				postOrder(child, path1, path2)
			path1.pop()

		self.found = 0
		self.reporter = None
		postOrder(self.ceo, [], [])
		return self.reporter





mark = Employee('mark', None, 10)
jerry = Employee('Jerry', mark, 5)
peep = Employee('peep', jerry, 6)
carlo = Employee('Carlo', jerry, 7)
bob = Employee('Bob', mark, 8)
alice = Employee('Alice', bob, 9)
fib = Employee('fib', alice, 10)
employees = [mark, jerry, peep, carlo, bob, alice, fib]
company = Company(employees)
company.printHierachy()

print company.commanAncestor(carlo, peep)