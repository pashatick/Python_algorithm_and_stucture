import random

'''
Алгоритм сортировки слиянием
'''

arr = [random.randint(0, 49) for i in range(10)]
print('До сортировки', arr)
print()	
'''
Функция 'merge' обрабатывает каждую пару массивов из функции 'mergesort'
'''
def merge(left, right):
	result = []
	i ,j = 0, 0
	while i < len(left) and j < len(right): # сравнивает элементы двух массивов
		if left[i] <= right[j]:
			result.append(left[i]) # и помещает меньший элемент в отсортированныый массив
			i += 1
		else:
			result.append(right[j]) 
			j += 1
	print('промежуточный результат',result)
	result += left[i:]		# когда счетчик одного из массивов заканчивается остатоk от другого помещается в result, 
	result += right[j:]		# так как оставшиеся значения автоматически больше	
	print()	
	return result
'''
Функция 'mergesort' рекурсивно делит массив на две части > 50/2 > 25/2, 25/2 > 12/2, 12/2, 12/2, 12/2 > ... и тд
'''
def mergesort(arr):
	if len(arr) < 2:
		return arr
	middle = int(len(arr) / 2)   
	print('середина', middle)	
	left = mergesort(arr[:middle])
	right = mergesort(arr[middle:])
	print("Левый и правый массив", left, right)	
	return merge(left, right)


print()
print('После сортировки', mergesort(arr))
