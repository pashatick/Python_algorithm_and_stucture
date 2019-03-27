
def split_digit(number):
	chet = 0
	nechet = 0
	while number != 0:
		a = (number % 10) % 2
		if a == 0:
			chet += 1
		else:
			nechet += 1 
		number //= 10
	print("Количество четных: ", chet, "Количество нечетных: ", nechet)


b = int(input())
split_digit(b)
