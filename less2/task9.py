a = int(input('Введи число A: '))
b = (int(input('Введите число B:')))

def dig_sum(number):
	nm1 = 0
	if number // 10 == 0:
		return number
	else:
		while number != 0:
			dg = number % 10
			nm1 += dg
			number //= 10
	return nm1


if dig_sum(a) > dig_sum(b):
	print('Сумма цифр - ', dig_sum(a), 'числа А - ', a, 'болеше В')
else:
	print('Сумма цифр - ', dig_sum(b), 'числа В - ', b, 'больше А')
