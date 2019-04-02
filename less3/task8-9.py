import random

matrix = []

for i in range(5):
	matrix.append([])
	for j in range(4):
		matrix[i].append(int(input('Введите число:'))		
		#matrix[i].append(random.randint(1, 15))
	matrix[i].append(sum(matrix[i]))
	

for i in matrix:
	print(i)
#task9


rot_matrix = list(map(list, zip(*matrix)))
MIN_ar = []

for i in rot_matrix:
	MIN_ar.append(min(i))

print('Максимальное минимально число = ', max(MIN_ar))
	


'''
N = len(matrix[0])
count = 0
def fst_el(arr, k):
	return arr[k]
k = 0
count = 0
for i in matrix:
	k = 0	
	for j in i:
		MIN = matrix[0][0]	
		if fst_el(i, k) < MIN:
			MIN = fst_el(i, k)
		else: 
			MIN = MIN
	k += 1	
	a.append(MIN)

print(a)
print(max(a))
'''
