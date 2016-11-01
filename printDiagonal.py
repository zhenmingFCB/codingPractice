def printDiagonal(matrix):
	m, n = len(matrix), len(matrix[0])
	for s in range(m+n-1):
		i_start = max(0, s-(n-1))
		i_end = min(m-1, s)
		level = []
		for i in range(i_start, i_end+1):
			level.append(matrix[i][s-i]) 
		print level

printDiagonal([[1,2,3,4],[5,6,7,8],[9,10,11,12]])