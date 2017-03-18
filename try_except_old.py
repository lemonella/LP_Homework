'''
Написать бесконечный цикл, 
а затем отловить Traceback клавиатуры и выкинуть Exception
'''


try:
	a = 1
	while True:
		print(a)
		a += 1
except KeyboardInterrupt:
	print ('Поздравляю, вы вышли из бесконечного цикла!')