numbers = [1, 1, 1, 1, 6]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#easy example
for eachnumber in range(4):
    for each_number in range(3):
        print(f'({eachnumber}, {each_number})')
#a nested loop is just a loop inside of a loop