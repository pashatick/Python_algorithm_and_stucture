import random

arr = []
i = 0
while i < 45:
	arr.append(random.randrange(-20,15))
	i += 1
print(min(arr),'index =', arr.index(min(arr)))



