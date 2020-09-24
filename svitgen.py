# Svitgen beta v0.3 
import time
import os
import sys
# Лого
print("=============================")
print("""

  ______     _____ ____   ____ _____ _   _  
 / ___\ \   / /_ _|  _ \ / ___| ____| \ | | 
 \___  \ \ / / | || | | | |  _|  _| |  \| | 
  ___) |\ V /  | || |_| | |_| | |___| |\  | 
 |____/  \_/  |___|____/ \____|_____|_| \_| 
                                            
""")
print("=============================")
# Действия
print("""
1. Генерировать""")
print("2. Как пользоваться")
print("3. Выйти")
a = input("Введите действие: ")	
if a == "3":
	sys.exit()
if a == "2":
	print("Это приложение SVIDGEN. Оно специализируется на генерации свидание по таким параметра как время и бюджет.")
	sys.exit()
if a == "1" or "Генерировать" or "генерировать":
	print("1. Утро (до 12 часов)")
	print("2. День (с 13 до 18)")
	print("3. Вечер (с 19 до 22)")
	print("4. Ночь (с 22 до 00)")
vremya = input("Введите время суток для свидания: ")
but = input("Введите свой бюджет: ")
if vremya == "1" or vremya == "Утро" or vremya == "утро":

# Бюджет если утро
	if but == "100":
		time.sleep(0.5)
		print("Можно: \nКупить мороженное или булки \nКупить напиток \nПогулять по парку \nПокататься на велосипедах")
	
	if but == "150":
		print('debil')
# Бюджет если день
if vremya == "2" or vremya == "День" or vremya == "день":
	if but == '100':
		time.sleep(0.5)
		print("")

	elif but == "150":
		time.sleep(0.5)
		print("lll")

	elif but == '200':
		time.sleep(0.5)
		print()

	elif but == '250':
		time.sleep(0.5)
		print()

	elif but == '300':
		time.sleep(0.5)
		print()

	elif but == '350':
		time.sleep(0.5)
		print()

	elif but == '400':
		time.sleep(0.5)
		print()

	elif but == '450':
		time.sleep(0.5)
		print()

	elif but == '500':
		time.sleep(0.5)
		print()
# Бютжет если вечер
if vremya == "3" or vremya == "Вечер" or vremya == "вечер":
	if but == '100':
		time.sleep(0.5)
		print("")

	elif but == "150":
		time.sleep(0.5)
		print("lll")

	elif but == '200':
		time.sleep(0.5)
		print()

	elif but == '250':
		time.sleep(0.5)
		print()

	elif but == '300':
		time.sleep(0.5)
		print()

	elif but == '350':
		time.sleep(0.5)
		print()

	elif but == '400':
		time.sleep(0.5)
		print()

	elif but == '450':
		time.sleep(0.5)
		print()

	elif but == '500':
		time.sleep(0.5)
		print()
# Бютжет если ночь
if vremya == "4" or vremya == "Ночь" or vremya == "ночь":
	if but == '100':
		time.sleep(0.5)
		print("")

	elif but == "150":
		time.sleep(0.5)
		print("lll")

	elif but == '200':
		time.sleep(0.5)
		print()

	elif but == '250':
		time.sleep(0.5)
		print()

	elif but == '300':
		time.sleep(0.5)
		print()

	elif but == '350':
		time.sleep(0.5)
		print()

	elif but == '400':
		time.sleep(0.5)
		print()

	elif but == '450':
		time.sleep(0.5)
		print()

	elif but == '500':
		time.sleep(0.5)
		print()
