import ephem

raw_planets_list = ephem._libastro.builtin_planets()
planets_list = {}

for i in raw_planets_list:
	if (i[1] != 'Planet'):
		continue
	a = getattr(ephem, i[2])('2016/09/23')
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