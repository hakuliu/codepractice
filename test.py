__author__ = 'paul'
from datastructures import linkedlist
from datastructures.simplestackandqueue import Stack
import random

teststack = Stack()
w = teststack.push(random.randint(-100,100))
print('pushed %s' % w)
w = teststack.push(random.randint(-100,100))
print('pushed %s' % w)
w = teststack.pop()
print('popped %s' % w)
print ('empty? %s' % teststack.isEmpty());
w = teststack.pop()
print('popped %s' % w)
print ('empty? %s' % teststack.isEmpty());