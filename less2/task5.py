for i in range(32, 128):
	print(chr(i), '-', ord(chr(i)), end = ' ')
	if (i - 1) % 10 == 0:
		print()
print()
