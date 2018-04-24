from __future__ import print_function


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)