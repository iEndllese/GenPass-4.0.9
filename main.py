#Генератор паролей 4.0.9
import config
import random
import time
import os
from colorama import Fore, Style, init
init()

#Переменные украшения текста
reset_all = Fore.RESET
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
r = Fore.RED + Style.BRIGHT
m = Fore.MAGENTA + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT

#Загрузка необходимых библиотек
os.system("pip install --upgrade pip")
os.system("pip install colorama")
os.system("pip install rich")
os.system("pip install pyfiglet")
os.system("cls || clear")

#Вывод из config предлагаемые варианты
console = config.console
print(g, config.teg_passgen)
console.print(config.version)
console.print(config.tab_1)


#Создания необходимых файлов для хранения
file_one = open("EasyPass.txt", "w+") #Легкий пароль
file_two = open("HardPass.txt", "w+") #Сложный пароль
file_ru = open("RuPass.txt", "w+") #Русские буквы | Символы

#Сам процесс генерации паролей
while True:

	#Выбор нужного значения
	for spros in c + "Выберите значение":
		print(spros, end = "", flush = True)
		time.sleep(00.03)
	inp = input(" >>> " + m)

	if inp == "0":
		for exit in r + "Программа завершена!":
			print(exit, end = "", flush = True)
			time.sleep(00.01)
		os.system("cls||clear")
		print(reset_all)
		break

	#Ввод нужных данных
	if inp == "1":
		col = int(input(f"{c}Введите количество паролей >> {m}"))
		dlin = int(input(f"{c}Введите длину паролей >> {m}"))

		#Процесс генерации пароля
		for i in range(col):
			time.sleep(00.03)
			password = ""
			for n in range(dlin):
				password += random.choice(config.chare_one)
			file_one.write(str(password) + "\n")
			print(g + password)
		file_one.close()
		print(f"\n{g}Готово!\n{y}Ваш пароль сохранен в <<EasyPass>>\n")

	elif inp == "2":
		col = int(input(f"{c}Введите количество паролей >> {m}"))
		dlin = int(input(f"{c}Введите длину паролей >> {m}"))

		for i in range(col):
			time.sleep(00.03)
			password_hard = ""
			for n in range(dlin):
				password_hard += random.choice(config.chare_two)
			file_two.write(password_hard + "\n")
			print(g + password_hard)
		file_two.close()
		print(f"\n{g}Готово!\n{y}Ваш пароль сохранен в <<HardPass>>\n")

	elif inp == "3":
		col = int(input(f"{c}Введите количество паролей >> {m}"))
		dlin = int(input(f"{c}Введите длину паролей >> {m}"))

		for i in range(col):
			time.sleep(00.03)
			password_ru = ""
			for n in range(dlin):
				password_ru += random.choice(config.chare_ru)
			file_ru.write(password_ru + "\n")
			print(g + password_ru)
		file_ru.close()
		print(f"\n{g}Готово!\n{y}Ваш пароль сохранен в <<RuPass>>\n")

	else:
		print(f"{r}Неверное значение!")
