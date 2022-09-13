# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:30:16 2021

@author: RATUL
"""

# Stack Algorithm

n = int(input("Initialize length of stack: "))
stack = [0]*n
index = 0


def push(s):
    global index
    if index < n:
        x = int(input("Element to enter: "))
        s[index] = x
        index += 1
    else:
        print("Overflow")


def pop(s):
    global index
    if index > 0:
        x = s[index - 1]
        s[index - 1] = 0
        index -=1
        print(x)
    else:
        print("Underflow")


y = 9
while y != 0:
    y = int(input("Press 1 for push, 2 for pop, 3 for traversing, 4 for number of elements in stack, 0 to exit. "))
    if y == 1:
        push(stack)
    elif y == 2:
        pop(stack)
    elif y == 3:
        print(stack)
    elif y == 4:
        print(f"Number of elements in stack: {index}")
    elif y == 0:
        print("See you later ^_^")
    else:
        print("Wrong Choice!")

