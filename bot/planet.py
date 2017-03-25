import ephem
import datetime
date = datetime.datetime.now()

raw_planets_list = ephem._libastro.builtin_planets()
planets_list = {}

for i in raw_planets_list:
	if (i[1] != 'Planet'):
		continue
		
	# let's create an object for all planets by their names from list
	a = getattr(ephem, i[2])(date.strftime('%Y/%m/%d'))
	planets_list[i[2]] = ephem.constellation(a)[1]

def get_sign_by_planet (planet):
	try:
		sign = planets_list[planet]
	except KeyError:
		sign = 'В нашем списке нет такой планеты, сорри.'

	return sign





'''
mars = ephem.Mars('2016/09/23')
print(mars)
print(ephem.constellation(mars))
'''
if __name__ == '__main__':
	print(get_sign_by_planet(input('Введи планету: ')))