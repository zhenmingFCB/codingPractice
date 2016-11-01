def numOfWays(m, n, start, k):
	"""
	find how many ways to reach (0,0) within k step from start point
	You could move in 4 directions
	"""
	if sum(start)>k:
		return 0
	directions = [(-1,0),(0,-1),(0,1),(1,0)]
	dp = [ [[0]*n for _ in range(m)] for _ in range(k+1)]
	dp[0][0][0] = 1
	for h in range(1,k+1):
		print ('reach in %d steps' % h)
		for i in range(min(m, h+1)):
			for j in range(h+1-i):
				num_ways = 0
				for di in directions:
					next_x, next_y = i+di[0], j+di[1]
					if 0<=next_x<m and 0<=next_y<n:
						num_ways += dp[h-1][next_x][next_y]
				print i,j,num_ways
				dp[h][i][j] = num_ways

	return sum([dp[i][start[0]][start[1]] for i in range(k+1)])

print numOfWays(8, 8, [0,1], 3)


