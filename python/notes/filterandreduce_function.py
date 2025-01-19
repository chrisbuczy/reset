#it takes a function and an iterable just like the map function
#filters things from a iterable(list, dictionary, set) using boolean values
#reduce function also takes a function and iterable and it returns a single value insteal of a iterable
#only reduce is in functools module
from functools import reduce

numbers = [1, 2, 3, 4, 5]  
def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str) #you can add an initializer (the third argument to the reduce function) which will make the first argument of the function ou used whatever you assigned it
print(total)
