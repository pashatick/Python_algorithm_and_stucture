import random

arr = []
i = 0
while i < 45:
	arr.append(random.randrange(1,15))
	i += 1

print(arr)

if arr.index(min(arr)) < arr.index(max(arr)):
	a = (arr[arr.index(min(arr))+1:arr.index(max(arr))])
	print(sum(a), a) 
else:
	a = (arr[arr.index(max(arr))+1:arr.index(min(arr))])
	print(sum(a), a)
#[arr.index(min(arr)):arr.index(max(arr))]


