

a1 = list(range(1, 22))

a2 = []

print(a1)

for i in a1:
	if i % 2 == 0:
		a2.append(a1.index(i))

print(a2)
