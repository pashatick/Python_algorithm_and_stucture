n = int(input('Введите n: '))

def ldg(n):
	n1 = 0
	if n == 0:
		return(n)

	else:
		return n + ldg(n -1)

a = ldg(n)


def rdg(n):
	return n * (n + 1) / 2

b = rdg(n)


if a == b:
	print(True)
else:
	print(False)



