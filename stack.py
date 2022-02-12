class stack:
    def __init__(self):
        self.items=[]
    def insert(self,item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def remove(self):
        self.items.pop()
    def display(self):
        return self.items
    def peek(self):
        return self.items[-1]

s1=stack()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.remove()
print(s1.display())
print(s1.peek())
        
        
