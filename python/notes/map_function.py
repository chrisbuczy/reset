#pretty much just a shortened for loop
numbers = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers)
print(numbers_int['1'])

names = ['sam', 'ali', 'max']
upper_cased = map(lambda name: name.upper(), names)
print(list(upper_cased))


