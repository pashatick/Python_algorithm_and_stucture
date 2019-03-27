def reverse_digit(number):
	nm = ''
	while number > 0:
		dg = str(number % 10)
		number //= 10
		nm += dg 
	print(nm)

b = int(input())
reverse_digit(b)


