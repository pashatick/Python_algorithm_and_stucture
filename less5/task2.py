ind_cn = int(input('Количество предприятий: '))

ind_name = {}

year_sum = 0

for i in range(ind_cn):
	name = input('Название предприятия: ')
	q = 4
	ysum = 0
	for j in range(q):
		qsum = int(input('Выручка за', j, '-й квартал: ')
		ysum += qsum
	ind_name[name] = ysum
	year_sum += ysum

print(ind_name)
