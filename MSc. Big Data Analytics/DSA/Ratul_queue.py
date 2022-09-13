# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:51:21 2021

@author: RATUL
"""

# Circular Queue Algorithm

n = int(input("Initialize the length of the queue: "))
queue = [0]*n
front = 0
rear = 0
flag = 0


def enqueue(q):
    global rear, flag
    if front == rear and flag == 1:
        print("Overflow")
    else:
        x = int(input("Enter the element: "))
        q[rear] = x
        rear = (rear+1) % n
        flag = 1


def dequeue(q):
    global front, flag
    if front == rear and flag == 0:
        print("Underflow")
    else:
        x = q[front]
        q[front] = 0
        front = (front+1) % n
        flag = 0
        print(x)


def no_ele():
    if rear == front and flag == 1:
        ele = n
    elif rear >= front:
        ele = rear - front
    else:
        ele = n - front + rear
    print (f"Number of elements in queue: {ele}")


y = 9
while y != 0:
    y = int(input("Press 1 for Enqueue, 2 for Dequeue, 3 for traversing, 4 for number of elements in Queue, 0 to exit. "))
    if y == 1:
        enqueue(queue)
    elif y == 2:
        dequeue(queue)
    elif y == 3:
        print(queue)
    elif y == 4:
        no_ele()
    elif y == 0:
        print("See you later ^_^")
    else:
        print("Wrong Choice!")

