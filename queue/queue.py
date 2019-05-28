class Queue(object):

    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if(self.items==[]):
            return ("queue is empty")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()
print(q.isempty())
q.enqueue(12)
q.enqueue(189)
q.enqueue(756)
print(q.dequeue())
print(q.size())
print(q.items)


