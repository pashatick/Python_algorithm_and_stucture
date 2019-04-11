
import random

arr = [random.randint(-100, 99) for i in range(200)]

print('Список до сортировки \n',arr)

def rev_buble(arr):
	count = 1
	N = len(arr)
	while count < len(arr):
		for i in range(N-count):
			if arr[i] < arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
		count += 1
	return arr
print()

print('Список после сортировки \n', rev_buble(arr))
		
