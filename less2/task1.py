

answer = 0

while True: 

	number1 = int(input('Введите число 1: '))
	number2 = int(input('Введите число 2: '))

	arg = input('Введи знак операции: ')

	if arg == '+':
		print(number1 + number2)
	elif arg == '-':
		print(number1 - number2)
	elif arg == '*':
		print(number1 * number2)
	elif arg == '/':
		if number2 == 0:
			print('На ноль делить нельзя!(')
		else:
			print(number1 / number2)
	elif arg == '0':
		break
	else:
		print("Неверная операция, попробуйте еще раз!(")

