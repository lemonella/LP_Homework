'''
Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

school_marks = {
'1a': [3, 5, 5, 4, 2, 4, 4, 5],
'1b': [2, 3, 3, 2, 4, 2, 5, 2],
'2a': [5, 4, 5, 4, 5, 5],
'2b': [3, 4, 5, 3, 4, 4, 3],
'3a': [1, 2, 3, 2, 3, 3, 4],
'4a': [5, 5, 5, 5, 5, 4],
'4b': [4, 5, 3, 4, 4, 3],
'4c': [1, 5, 2, 5, 3 , 4],
}

class_average_marks = {}
average_marks_by_classes = []

def count_average_marks(marks_list):
	marks_sum = 0
	count_marks = 0
	for mark in marks_list:
		marks_sum += mark
		count_marks += 1
	return round(marks_sum / count_marks, 1)

# let's count class average marks
for class_name in school_marks:
	class_marks_sum = 0
	count_marks = 0
	class_average_marks[class_name] = count_average_marks(school_marks[class_name])
	average_marks_by_classes.append(class_average_marks[class_name])

class_average_marks = sorted(class_average_marks.items())

# Let's count school average mark
school_average_mark = count_average_marks(average_marks_by_classes)

print('Средний балл по всей школе: ' + str(school_average_mark))
print('Средние баллы по классам:')

for i in class_average_marks:
	print (str(i[0]) + ': ' + str(i[1]))
