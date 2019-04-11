import random

m = random.randint(1, 5)
arr = [random.randint(0, 10) for i in range(2*m + 1)]
print(arr)

half = int((len(arr)-1)/2)

i = 0
while i < len(arr):		
	mid  = arr[i]		
	count = 0	
	for j  in  arr:				
		if mid <= j:
			count += 1
		else:
			count += 0		
	if count == half:
		print('Медиана- ', mid)
		break		
	i += 1
			




