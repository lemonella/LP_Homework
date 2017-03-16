'''
1) Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
2) Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
3) Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
4) При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
'''

names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

# Task 1
for name in names_list:
	if name == 'Валера':
		print (name + ' нашелся!')
		break

# Task 2. Now the same with a function
def find_person(name, names_list):
	for n in names_list:
		if n == name:
			print (name + ' нашелся!')
			break

# Task 3, 4 
def ask_user(greeting):

	message = input(greeting + ' ').lower()

	if message == 'хорошо':
		print("Пока!")
	else:
		ask_user('И всё-таки, как дела?')


ask_user('Как дела?')