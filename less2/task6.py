import random

number = random.randint(0, 100)

i = 0
while i < 11:
	if i != 10:
		un = int(input('Угадай число: '))
		if un == number:
			print('Да, вы угадали!!!')
			break
		elif un < number:
			i += 1
			print('Вваше число меньше, осталось ', 10 - i, 'попыток!')
		elif un > number:
			i += 1
			print('Вваше число больше, осталось ', 10 - i, 'попыток!')
		elif i == 11:
			print(number)
	else:
		print(number)
		break


