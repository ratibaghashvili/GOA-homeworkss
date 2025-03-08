# 1)

# directionary- არის მონაცემთა სტრუქტურა, რომელიც ინახავს წყვილებად შერწყმულ ღირებულებებს ამ წყვილებს ეწოდება key-value pairs (key  და value).

# 2)


m = {
    'name': 'ჯამბული',
    'age': 18,
    'city': 'თბილისი',
    'profession': 'პროგრამისტი',
    'hobby': 'ფეხბუღთი'
}

print(m.keys())

# 3)
print(m.values())

# 4)
print(m.items())

# 5)

for key, value in m.items():
    print(f"Key: {key}, Value: {value}")

# 6)

age = m.get('age', 'Not Found')
print(age) 

not_exist= m.get('jambula', 'Not Found')
print(not_exist) 

# 7)

m['emzaras wlovaneba'] = 99
print('es aris emzaras wlovaneba da axali dictionary' , m)

