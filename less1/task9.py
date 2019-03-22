a = input("число a")
b = input("число b")
c = input("число c")

if c<a<b or b<a<c:
	print(a)
elif b<c<a or a<c<b:
	print(c)
else:
	print(b)

	
