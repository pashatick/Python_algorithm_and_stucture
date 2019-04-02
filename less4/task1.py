

import random
import timeit
import cProfile

matrix = []

for i in range(5):
	matrix.append([])
	for j in range(4):
		#matrix[i].append(int(input('Введите число:'))		
		matrix[i].append(random.randint(1, 15))
	matrix[i].append(sum(matrix[i]))
	
for i in matrix:
	print(i)


def matr1():
	mat = matrix	
	rot_matrix = list(map(list, zip(*mat)))
	MIN_ar = []

	for i in rot_matrix:
		MIN_ar.append(min(i))

	return max(MIN_ar)
	

def matr2():
	mat = matrix	
	MAX = None
	for j in range(len(mat[0])):
	    MIN = matrix[0][j]
	    for i in range(len(mat)):
        	if mat[i][j] < MIN:
        	    MIN = mat[i][j]

	if MAX is None or MAX < MIN:
        		MAX = MIN

	return MAX

print(matr1())
print(matr2())

def main():
	matr1()
	matr2()

com1 = timeit.timeit("matr1()", setup="from __main__ import matr1", number = 100000)
com2 = timeit.timeit("matr2()", setup="from __main__ import matr2", number = 100000)
com3 = cProfile.run('main()')
__doc__ = com1, com2, com3
print(__doc__)


																																																																																		
