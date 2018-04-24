from __future__ import print_function
from Node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isempty(self):
        return self.size == 0

    def insertfront(self, item):
        print("Insert " + str(item) + " at front")
        if self.isempty():
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return

    def insertback(self, item):
        print("Insert " + str(item) + " at back")
        if self.isempty():
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        newNode = Node(item)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def printlist(self):
        currnode = self.head
        print("List contents : ")
        while currnode is not None:
            print(currnode)
            currnode = currnode.next

    def removefront(self):
        print("Remove item from front")
        if self.size == 1:
            item = self.head.item
            self.head = None
            self.tail = None
            self.size -= 1
            return item
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return item

    def removeback(self):
        print("Remove item from back")
        if self.size == 1:
            item = self.head.item
            self.head = None
            self.tail = None
            self.size -= 1
            return item

        curr_node = self.head
        while curr_node.next is not self.tail:
            curr_node = curr_node.next

        item = self.tail.item
        tail = curr_node
        tail.next = None
        self.size -= 1
        return item


