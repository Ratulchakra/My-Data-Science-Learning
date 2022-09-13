# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 01:18:44 2022

@author: RATUL
"""

class Node:
    next: None

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_start(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1

    def insert_k_pos(self, data, k):
        if k < 2:
            self.insert_start(data)
        else:
            newnode = Node(data)
            current = self.head
            for _ in range(k - 1):
                current = current.next
            newnode.next = current.next
            current.next = newnode
            self.length += 1

    def insert_end(self, data):
        self.insert_k_pos(data, self.length)

    def delete_start(self):
        if self.length == 0:
            print("No Element in Linked List")
        else:
            x = self.head.data
            self.head = self.head.next
            self.length -= 1
            print(x)

    def delete_k_pos(self, k):
        if k < 2:
            self.delete_start()
        else:
            current = self.head
            for _ in range(k - 2):
                current = current.next
            x = current.next.data
            current.next = current.next.next
            self.length -= 1
            print(x)

    def delete_end(self):
        self.delete_k_pos(self.length)

    def traversal(self):
        x = []
        current = self.head
        while current != None:
            x.append(current.data)
            current = current.next
        print("->".join([str(i) for i in x]), end="->Null")

    def search(self, ser):
        current = self.head
        found = False
        for i in range(self.length):
            if current.data == ser:
                found = True
                break
            current = current.next
        print(f"Found {ser} at position {i + 1}") if found else print("Not Found")

    def reverse(self):
        previous = None
        current = self.head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    def sort(self):
        current = self.head
        index = Node(None)
        if current == None:
            return
        else:
            while current != None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next


if __name__ == "__main__":
    print("A Linked list have been initialized")
    lnls = LinkedList()
    while 1 < 2:
        user = int(input("\nPress 1 for insertion at begining, 2 for k th position, 3 for insertion at end,\n "
                         "4 for deletion at begining, 5 for k th position, 6 for deletion at end,\n "
                         "7 for traversal, 8 for reversal, 9 for sorting, \n 0 to exit\n"))
        if user == 1:
            y = int(input("Enter element to insert: "))
            lnls.insert_start(y)
        elif user == 2:
            y = int(input("Enter element to insert: "))
            k = int(input("Position to enter: "))
            if k > lnls.length + 1:
                print("Index too big")
            else:
                lnls.insert_k_pos(y, k)
        elif user == 3:
            y = int(input("Enter element to insert: "))
            lnls.insert_end(y)
        elif user == 4:
            lnls.delete_start()
        elif user == 5:
            k = int(input("Position to delete: "))
            if k > lnls.length:
                print("Not enough element in Linked list")
            else:
                lnls.delete_k_pos(k)
        elif user == 6:
            lnls.delete_end()
        elif user == 7:
            lnls.traversal()
        elif user == 8:
            lnls.reverse()
        elif user == 9:
            lnls.sort()
        elif user == 0:
            print(f"At the end length of LinkedList is {lnls.length}")
            print("Good Bye! see you later ^_^")
            break
        else:
            print("Wrong Choice")
