###############################################
my_str = '0123456789'
for symbol in my_str:
	for symbol2 in my_str:
		result = symbol + symbol2
		print(int(result))
