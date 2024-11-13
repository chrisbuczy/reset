# FIFO data structure that serves elements with higher priority to lower priority

gpa = []

gpa.insert(0, "B")
gpa.insert(0, "C")
gpa.insert(0, "A")
gpa.insert(0, "F")
gpa.insert(0, "D")
gpa.sort(reverse = True)

while gpa:
    print(gpa.pop(0))


gpa.insert(0, 3.0)
gpa.insert(0, 1.5)
gpa.insert(0, 4.0)
gpa.insert(0, 3.5)
gpa.insert(0, 2.5)
gpa.sort(reverse = True)

while gpa:
    print(gpa.pop(0))