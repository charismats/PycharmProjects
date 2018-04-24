from __future__ import print_function
from LinkedList import LinkedList


class Queue(LinkedList):

    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, item):
        self.insertback(item)

    def dequeue(self):
        return self.removefront()