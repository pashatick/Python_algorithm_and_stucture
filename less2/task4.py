n = int(input('Введите n: '))

x = 0
s = 0
i = 0
a = 1
while i < n:
	s += a
	a = a/-2
	i += 1

print(s)
