__author__ = 'paul'
from linkedlist import LinkedListSingle


class Stack:
    def __init__(self):
        self.list = LinkedListSingle()

    def push(self, data):
        self.list.addnode(data)
        return data

    def peek(self):
        return self.list.peek().getdata()

    def pop(self):
        return self.list.pop().getdata()

    def isEmpty(self):
        return self.list.isEmpty()