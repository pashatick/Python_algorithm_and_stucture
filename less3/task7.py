import random

arr = []
i = 0
while i < 45:
	arr.append(random.randrange(-20,15))
	i += 1

print(arr)

a = arr.pop(arr.index(min(arr)))
b = min(arr)
print (a,b)
