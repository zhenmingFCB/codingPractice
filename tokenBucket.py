import time
class TokenBucket(object):

	def __init__(self, limit_rate):
		self.limit_rate = limit_rate
		self.tokens = limit_rate
		self.ts = time.time

	def take(self):
		now = time.time
		self.tokens += int(now-self.ts)*self.limit_rate
		if self.tokens>self.limit_rate:
			self.tokens = self.limit_rate
		self.ts = now
		if self.tokens<1:
			return False
		else:
			self.tokens-=1
			return True

