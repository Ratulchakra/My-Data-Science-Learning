# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:37:59 2022

@author: RATUL
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.elements = 0
        self.record = []

    def insert(self, data):
        new_node = Node(data)
        if self.elements == 0:
            self.root = new_node
        else:
            current = self.root
            while current != None:
                if current.data < data:
                    if current.right == None:
                        break
                    current = current.right
                else:
                    if current.left == None:
                        break
                    current = current.left
            if current.data < data:
                current.right = new_node
            else:
                current.left = new_node
            new_node.parent = current
        self.elements += 1

    def traversal_inorder(self, root):
        if root:
            self.traversal_inorder(root.left)
            print(root.data)
            self.traversal_inorder(root.right)

    def traversal_preorder(self, root):
        if root:
            print(root.data)
            self.traversal_preorder(root.left)
            self.traversal_preorder(root.right)

    def traversal_postorder(self, root):
        if root:
            self.traversal_postorder(root.left)
            self.traversal_postorder(root.right)
            print(root.data)

    def search(self, ser):
        i = 1
        current = self.root
        while current != None:
            if current.data < ser:
                current = current.right
                i = 2 * i + 1
            elif current.data > ser:
                current = current.left
                i = 2 * i
            else:
                break
        if current != None:
            print(f"Found {ser} at flattened array index {i}")
        else:
            print("Not Found")

    def succ_node(self, root):
        current = root
        while current.left != None:
            current = current.left
        return current

    def deletion(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.deletion(root.left, key)
        elif key > root.data:
            root.right = self.deletion(root.right, key)
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp

            elif root.right == None:
                temp = root.left
                root = None
                return temp
            temp = self.succ_node(root.right)

            root.data = temp.data
            root.right = self.deletion(root.right, temp.data)
        return root

    def maximum(self):
        current = self.root
        while current.right != None:
            current = current.right
        print(f"Maximun in the binary search tree is: {current.data}")

    def minimum(self):
        current = self.root
        while current.left != None:
            current = current.left
        print(f"Minimum in the binary search tree is: {current.data}")

    def flatten(self, root):
        if root:
            self.flatten(root.left)
            self.record.append(root.data)
            self.flatten(root.right)

    def successor(self, data):
        self.record = []
        self.flatten(self.root)
        flat = self.record
        x = len(flat)
        for i in range(x):
            if flat[i] == data:
                if i == x - 1:
                    print("No successor node")
                else:
                    y = flat[i + 1]
                    print(f"The successor node value is {y}")
                return flat
        print("Node data not in existence")


if __name__ == "__main__":
    bst = BST()
    print("Binary Tree has been initialized")
    while 1<2:
        user = int(input("Press 1 for insertion, 2 for deletion, 3 for Inorder traversal, \n"
                         "4 for Preorder traversal, 5 for Postorder traversal, 6 for search,\n"
                         "7 for successor, 8 for minimum, 9 for maximum,\n0 to exit.  "))
        if user == 1:
            y = int(input("Enter the data, you wish to insert: "))
            bst.insert(y)
            print("Insertion complete")
        elif user == 2:
            y = int(input("Enter the data, you wish to delete: "))
            bst.deletion(bst.root, y)
            print("Deletion complete")
        elif user == 3:
            print("The traversal in-order: ")
            bst.traversal_inorder(bst.root)
        elif user == 4:
            print("The traversal pre-order: ")
            bst.traversal_preorder(bst.root)
        elif user == 5:
            print("The traversal post-order: ")
            bst.traversal_postorder(bst.root)
        elif user == 6:
            y = int(input("Enter the element, you wish to search: "))
            bst.search(y)
        elif user == 7:
            y = int(input("Enter the element, you wish to search the successor of: "))
            bst.successor(y)
        elif user == 8:
            bst.minimum()
        elif user == 9:
            bst.maximum()
        elif user == 0:
            print("See you later ^-^")
            break
        else:
            print("Wrong Choice.")



