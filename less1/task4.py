#!/etc/python3.5

import random

n1 = int(input('введите число 1')
n2 = int(input('введите число 2')

random.uniform(n1, n2)
random.randint(n1, n2)

st1 = input('веди символ 1')
st2 = input('введите символ 2')

ls=[chr(x) for x in range(ord('a'),ord('z')+1)]
random.sample(ls, 2)
