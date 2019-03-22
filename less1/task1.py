number = int(input('Введите число:'))

dg1 =  number//100
dg2 = (dg1//10)%10
dg3 = number%10
print("The sum of numbers,", dg1 + dg2 + dg3)
print("The product of numbers,", dg1 * dg2 * dg3)
