# FIFO, first in first out
queue = []

# always insert and pop at index 0
queue.insert(0, 1)
queue.insert(0, 2)
queue.insert(0, 3)
print(queue)

queue.pop(0)
print(queue)

''' 
where are queues useful

1. keyboard buffer (letters should appear on the screen in order pressed)
2. printer queue (print jobs should be completed in order)
3. used in linked lists, priority queues, breadth-first search
'''