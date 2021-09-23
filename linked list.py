class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def push(self,new):
        newnode=Node(new)
        newnode.next = self.head
        self.head=newnode
       
    def append(self,new):
        newnode=Node(new)
        if self.head is None:
            self.head=newnode
            return 
        last = self.head
        while (last.next):
            last=last.next
        last.next=newnode
    
    def insert(self,prev,new):
        if prev is None:
            print("no node before")
            return
        newnode=Node(new)
        
        newnode.next=prev.next
        prev.next=newnode
        
        
        
    def printnode(self):
        temp=self.head
        while(temp):
            print (temp.value)
            temp=temp.next
            
if __name__=='__main__':
    llist = LinkedList()
    llist.append(1)
    llist.push(2)
    llist.push(3)
    llist.append(4)
    llist.insert(llist.head.next, 5)
    print('Created linked list is:')
    llist.printnode()            
