
import random

arr = []
i = 0
while i < 20:
	arr.append(random.randrange(1,15))
	i += 1
print(arr)

# 1 вариант
N = len(arr)
def sort_to_max(a):
	for i in range(N-1):
    		for j in range(N-i-1):
        		if a[j] > a[j+1]:
        		    a[j], a[j+1] = a[j+1], a[j]
				
	return a
print(sort_to_max(arr))

arr[0], arr[-1] = arr[-1], arr[0]

print(arr)

# 2 вариант

iMAX = arr.index(max(arr))
iMIN = arr.index(min(arr))

arr[iMAX],arr[iMIN] = arr[iMIN],arr[iMAX]


print(arr) 



