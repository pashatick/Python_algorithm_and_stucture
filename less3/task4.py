

import random

arr = []
i = 0
while i < 45:
	arr.append(random.randrange(1,15))
	i += 1
print(arr)

b = list(set(arr))
print(b)

for i in b:
	count = 0	
	for j in arr:
		if i == j:
			count += 1
	print('Число', i, 'встречается', count, 'раз')


