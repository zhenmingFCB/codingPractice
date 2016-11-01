def tabCompletion(prefix, wordlist):
	trie = TrieTree()
	for word in wordlist:
		trie.insert(word)
	return trie.startWith(prefix)

class TrieNode(object):

	def __init__(self):
		self.children = dict()
		self.word = None

class TrieTree(object):

	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				curr.children[c] = TrieNode()
			curr = curr.children[c]
		curr.word = word

	def startWith(self, prefix):
		from collections import deque
		curr = self.root
		for c in prefix:
			if c not in curr.children:
				return []
			curr = curr.children[c]
		res = []
		queue = deque()
		queue.append(curr)
		while queue:
			curr = queue.popleft()
			if curr.word:
				res.append(curr.word)
			for child in curr.children:
				queue.append(curr.children[child])
		return res

wordlist = ['apple','ad', 'app', 'apparent', 'appear', 'baby', 'around']
print tabCompletion('', wordlist)

