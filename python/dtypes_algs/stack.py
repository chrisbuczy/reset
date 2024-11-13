# LIFO, last in first out

x = []

# use pop and append to add and remove to stack
x.append(1)
x.append(2)
x.append(3)
print(x)


x.pop()
print(x)
print(x.index(1))

'''
uses of stacks?

1. undo/redo features in text editors
2. moving back/forward through browser history
3. backtracking algorithms (maze, file directories)
4. calling functions (call stack)
'''