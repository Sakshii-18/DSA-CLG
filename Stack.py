#stack using inked list
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class stack:
    def __init__(self):
        self.top = None
        
    def isempty(self):
        return self.top is None
    
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node
       
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp = self.top
            print("Popped elements : ",temp.data)
            self.top = self.top.next
            temp = None
       
    def display(self):
        temp = self.top
        print("Stack elements :")
        while temp:
            print(temp.data)
            temp = temp.next
    
    
    def rev(self):
        temp = self.top
        while temp is not None:   
            s2.push(Node(temp.data)) 
            temp=temp.next
            
s = stack()
s2 = stack()
n1 = 10
n2 = 20
s.push(Node(n1))
s.push(Node(n2))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.display()

print()
s.pop()
s.display()

s.rev()
s2.display()