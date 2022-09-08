import random


score = 0
while(True):
	print("Ваш счет: ", score)
	a = random.randint(1, 3)
	print("Камень - 1")
	print("Ножницы - 2")
	print("Бумага - 3\n")
	b = int(input("Выберите что-нибудь: "))
	print()

	if (a == b):
		print("Ничья\n")
	elif (a == 1 and b == 2):
		print("Компьютер: камень")
		print("Камень ломает ножницы - вы проиграли\n")
	elif (a == 2 and b == 1):
		print("Компьютер: ножницы")
		print("Камень ломает ножницы - вы выиграли!!!\n")
		score+=1
	elif (a == 1 and b == 3):
		print("Компьютер: камень")
		print("Бумага накрывает камень - вы выиграли!!!\n")
		score+=1
	elif (a == 3 and b == 1):
		print("Компьютер: бумага")
		print("Бумага накрывает камень - вы проиграли\n")
	elif (a == 2 and b == 3):
		print("Комьютер: ножницы")
		print("Ножницы режут бумагу - вы проиграли\n")
	elif (a == 3 and b == 2):
		print("Компьютер: бумага")
		print("Ножницы режут бумагу - вы выиграли!!!\n")
		score+=1
	else:
		print("Вы не выбрали жест!!!!")