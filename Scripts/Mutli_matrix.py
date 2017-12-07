




def Mutli_matrix(x,y):
	dim = y+1 - x 

	matrix = createMatrix(dim)
	for i in xrange(0,dim):
		for j in xrange(x,y+1):
			matrix[i].append(j)

	# for j in xrange(x,y+1):
	# 	matrix[0].append(i)

	return matrix


def createMatrix(dim):
	matrix = []
	for i in xrange(0,dim):
		matrix.append([])

	return matrix



print Mutli_matrix(1,3)

