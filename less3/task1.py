

a1 = list(range(2, 100))

a2 = list(range(2, 10))

a = [0]*8
for i in a1:
	for j in a2:
		if i % j ==0:
			a[j-2] += 1
i = 0
while i < len(a):
	print(a[i], 'чисел из ряда а1 кратны числу -', a2[i])
	i += 1
