import random


a = random.randint(1, 100)
while(True):
	b = int(input("Введите число: "))
	if (a < b):
		print("меньше!")
	elif (a > b):	
		print("больше!")
	elif ( a == b):
		print("ПРАВИЛЬНО!!!")
		quit()