class Stack(object):
    
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]

s=Stack()
print(s.isempty())
s.push(8)
s.push(9)
print(s.isempty())
print(s.items)
print(s.pop())
print(s.items)