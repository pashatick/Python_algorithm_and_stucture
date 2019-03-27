number = int(input("Введите последовательность цифр: "))
digit = int(input("Введи искомое число: "))

i = 0 
while number != 0:
	d = number % 10
	number //= 10
	if d == digit:
		i += 1
	else:
		pass



print(i)
