'''
Добавить команду /wordcount котрая считает сова в присланной фразе. 
Например на запрос /wordcount "Привет как дела" бот должен посчитать количество слов в кавычках и ответить: 3 слова.
'''

# Function returns number of words in the message
import re

def count_words_in_message (message):
	result = -1

	if not message.startswith('/wordcount'):
		return result

	bare_phrase = re.findall('\"(.*)\"', message)
	if bare_phrase:
		result = len(bare_phrase[0].split())
	else:
		result = "Не удалось посчитать слова. Фраза для подсчета слов должна быть в кавычках и не должна быть пустой"

	return result


if __name__ == '__main__':
	print(count_words_in_message(input('Введи фразу: ')))
	#print(count_words_in_message('/wordcount sfhvlskjfhgsl'))