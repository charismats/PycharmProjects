from __future__ import print_function
from LinkedList import LinkedList


class Stack(LinkedList):

    def __init__(self):
        super(Stack, self).__init__()

    def push(self, item):
        self.insertfront(item)

    def pop(self):
        return self.removefront()

