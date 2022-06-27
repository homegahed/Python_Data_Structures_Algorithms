""""
Lesson 2: Reverse a string using stack

Build an algorithm which utilizes class "stack" which was built in the previous
lesson, the algorithm will reverse letters which are inside a string
"""

import unit1_class1_stack as stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string = reversed_string + s.pop()

print(reversed_string)
