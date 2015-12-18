__author__ = 'paul'

class NodeSingleLL:
    def __init__(self, data=None, nextnode=None):
        self.data = data
        self.nextnode = nextnode

    def getdata(self):
        return self.data

    def getnext(self):
        return self.nextnode

    def setnext(self, nextnode):
        self.nextnode = nextnode

class NodeDoubleLL(NodeSingleLL):
    '''
    using the same stuff from singly-linked nodes, so we only really need to code for the prev stuff.
    '''
    def __init__(self, data=None, nextnode=None, prevnode=None):
        NodeSingleLL.__init__(data, nextnode)
        self.prevnode = prevnode

    def getprev(self):
        return self.prevnode

    def setprev(self, prevnode):
        self.prevnode = prevnode

class LinkedListSingle:
    '''
    Linked lists are not very good for random lookup, but it's great for insertion.
    It maintains a O(1) time to add a node. and also a O(1) time for deletion.
    However, doing a lookup will use O(n) time.
    This is fine for cases where you'd need to iterate through all of the list for lookup anyways
    good uses are for stacks and for collision lookup in Hashmaps.

    I should add comparator for the data in case it's not a primative or something...for later.
    '''
    def __init__(self, head=None):
        self.head = head

    def addnode(self, data):
        newhead = NodeSingleLL(data, self.head)
        self.head = newhead

    def delnode(self, lookup):
        '''
        deletes a node based on a lookup value.
        We have to do a lookup for the value, which is O(n) :(
        :param lookup data used for the lookup:
        :return: the node that's deleted, or none if we didn't delete anything
        '''
        prevtodel = self.lookforPrev(lookup)
        if(prevtodel != None):
            rv = prevtodel.getnext()
            prevtodel.setnext(rv.getnext())
            #do I set the rv's next to None here? Idk...
            return rv
        return None

    def lookforPrev(self, lookup):
        '''
        look for a piece of data.
        :param lookup:
        :return: node WITH THE NEXT NODE as the data (because that's what I need for delete...)
        '''
        if(self.head == None):
            return None
        current = self.head
        while(current.getnext()!=None):
            if(current.getnext().getdata() == lookup):
                return current
        return None

    def pop(self):
        '''
        just delete and pop out the head
        :return: whatever node that was popped.
        '''
        rv = self.head
        if(rv == None):
            return None
        self.head = rv.getnext()
        return rv