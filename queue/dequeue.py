class Dequeue():
    # innitializing empty list
    def __init__(self):
        self.items=[]
    
    # check queue is empty or not if empty return true and if not return false

    def isempty(self):
        return self.items ==[]

    # add data to the front,for this we use append() this will add items in front

    def additemsfront(self,item):
        self.items.append(item)

    # add data to the rear end

    def addatrear(self,item):
        self.items.insert(0,item)

    # for deleting of front item we use pop()

    def removefront(self):
        if(self.items==[]):
            return ("queue is empty")
        else:
            return self.items.pop()

    # for removing items fron rear we use pop(0)
    def removerear(self):
        if(self.items==[]):
            return ("queue is empty")
        else:
            return self.items.pop(0)


    # checking size
    def size(self):
        return len(self.items)


# initializing dequeue
dq=Dequeue()
print(dq.isempty())

dq.additemsfront(20)
dq.additemsfront(26)
dq.additemsfront(27)

dq.addatrear(78)
dq.addatrear(565)
dq.addatrear(226)

dq.removerear()

print(dq.items)

