#singly linked list : 10 oct 2026

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
    #append val
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
    #find middle value            
    def findMiddle(self):
        p1 = self.head
        p2 = self.head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        if p1:
            print(p1.data)
        else:
            print("list is empty")
                
    def reverse(self):
            prev = None
            current = self.head
            while current :
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev
        
    def SumOfNode(self): #Calculate the sum of every two consecutive node values
        current = self.head
        while current and current.next:
            sum = current.data + current.next.data
            print(sum)
            current = current.next
            
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



print("Reverse List :")
l1.reverse()
l1.display()

print()
print("Sum of 2 consecutive nodes : ")
l1.SumOfNode()

print("Middle value:")
l1.findMiddle()
