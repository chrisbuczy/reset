numbers = [1, 3, 5, 7, 9]

# new_list = [new_item for item in list if condition]

# new_item - how you are going to change the item
# item - the item in the list that you are using to change
# list - the list you are duplicating/changing
# the if statement allows you to change numbers according to a condition (this isn't needed)

doubled_numbers = [num * 2 for num in numbers if num > 3]

print(doubled_numbers)

bits = [True, False, True, False, True, False, True, False]
new_bits = [1 if b == True else 0 for b in bits]
print(new_bits)

my_string = 'HelloMyNameIsMariya'
my_string = ''.join(
    [i if i.islower() else ' ' + i.lower() if i in ['N', 'I']else ' ' + i for i in my_string]  #print i if it is lower else add a space in fron of i.
#to make an elif statement you first do the action (add a space and make i lowercase if i is in the list ['N', 'I'])
    )[1:] #this prints every letter other then the extra space at the beggining
print(my_string)

