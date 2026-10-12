#delete 1st and last node
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def append(self,new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
    def append(self,new_node):
            if self.head == None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
                
     #display recordss           
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    #insertt        
    def insert(self,new_node,pos):
        if(pos == 1):
            new_node.next = self.head
            self.head = new_node
        else:
            p=1
            temp = self.head
            while p != pos-1:
                temp = temp.next
                p +=1
            new_node.next = temp.next
            temp.next = new_node
     #delete        
    def delete(self,value):
        temp = self.head
        if(temp.data == value): #first node to delete
            self.head = self.head.next
        else:
            while(temp.data != value and temp):
                prev = temp
                temp = temp.next
                if temp ==None:
                    print("Value isn't present")
                    return
                prev.next = temp.next
                temp = None
    #delmiddle value            
    
    def findMiddle(self):
        p1 = self.head
        p2 = self.head
        prev = None

        while p2 and p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next

        if p1:
            print("Middle Node:", p1.data)
            if prev:
                prev.next = p1.next
            else:
                self.head = p1.next
                p1 = None
        else:
            print("List is empty")

            
            def Delete(self): #delete 1st and last node
                temp1 = self.head
                temp1 = None
                prev = None
                temp = self.head = self.head.next
                while temp.next :
                    prev = temp
                    temp = temp.next
                prev.next = None
                temp = None
            
            
l1 = SLL()
n1 = Node(10)
n2 = Node(20)

print("Appended list :")    
l1.append(n1)
l1.append(n2)
l1.display()

print()
print("Inserted List :")
l1.insert(Node(30),1)
l1.insert(Node(50),3)
l1.display()

print("deleted Node :")
l1.delete(30)
l1.display()

print("Middle Value :")
l1.findMiddle()
