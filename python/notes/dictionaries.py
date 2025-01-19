phone = input('phone:')
digitsmapping = {'1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four'}
output = ""
for number in phone:
    output += digitsmapping.get(number, '!')
print(output)