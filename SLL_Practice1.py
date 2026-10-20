class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def append(self,new_node):
        temp = self.head
        if self.head == None:
            self.head = new_node
        else:
            while temp.next:
                temp=temp.next
            temp.next = new_node
            
    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            while p != pos-1:
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
                
    def delete(self,value):
        temp = self.head
        prev = None
        if value == temp.data:
            self.head = self.head.next
        else:
            while temp and temp.data != value:
                prev = temp
                temp = temp.next
                if temp == None:
                    print("value isn't present")
                    return
            prev.next = temp.next
            temp = None
            
    def findMid(self):
        slow = self.head
        fast = self.head
        prev = None

        if self.head == None:
            return

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev == None:
            self.head = None
        else:
            prev.next = slow.next
        
            
    def deleteAlternative(self) :
        temp = self.head
        while temp!= None and temp.next != None:
            temp.next = temp.next.next
            temp = temp.next
            
        
    def rev(self):
        temp = self.head
        prev = None
        while temp :
            next_node =temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev   
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
l = SLL()
n1 = Node(10)
n2 = Node(20)

print("append : ")
l.append(n1)
l.append(n2)
l.append(Node(30))
l.display()

print("Insert :")
l.insert(Node(55),2)
l.insert(Node(18),4)
l.display()
            
print("deleted :")
l.delete(550)
l.display()

print("Middle Value :")
l.findMid()
l.display()

print("rev:")
l.rev()   
l.display()
        
print("Delete Alternative :")
l.deleteAlternative()
l.display()