# Dictionaries :Python hash tables

'''
Mapping types with Key, Value pairs
'''

# dictionaries with strings as keys and integers as keys

city_weather = {'Jinja': 80, 'Newark': 30}

print(type(city_weather))
print(city_weather)
print(city_weather['Jinja'])

flower_color = dict([('daisy',['white','blue']), ('sunflower',{'yellow', 'brown'})])
print(flower_color['daisy'][1])

print(flower_color['sunflower'])

info = {'City':['Kampala', 'New York City'], 'Ages':(79, 80, 15)}