from math import sqrt
import random
import timeit
import cProfile


 
# через решито Эратосфена
def erat():
	n = 100	
	a = []
	for i in range(n + 1):
    		a.append(i)

	a[1] = 0
 
	i = 2
	while i <= n:
    		if a[i] != 0:
        		j = i + i
        		while j <= n:
            			a[j] = 0
            			j = j + i
    		i += 1
 
	a = list(set(a))
	a.remove(0)
	#k = int(input('введите k-й элемент: '))
	k = 15	
	return a[k]

#без алгоритма "решито Эратосфена"

def not_erat():
	n = 100	
	a = []	
	lst=[i for i in range(2, n)]
	for i in lst:
		for j in a:
			if j > int((sqrt(i)) + 1):
				a.append(i)
				break
			if (i % j == 0):
				break
		else:
			a.append(i)
	#k = int(input('введите k-й элемент: '))
	k = 15	
	return a[k]
	

print(erat())
print(not_erat())

def main():
	erat()
	not_erat()

com1 = (timeit.timeit("erat()", setup="from __main__ import erat", number = 100000))
com2 = (timeit.timeit("not_erat()", setup="from __main__ import not_erat", number = 100000))
com3 = cProfile.run('main()')
__doc__ = com1, com2, com3
print(__doc__)

