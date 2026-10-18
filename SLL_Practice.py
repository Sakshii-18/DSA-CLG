class Node: #manages single node
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SLL: #manages whole LL
    def __init__(self):
        self.head = None
        
    def append(self,new_node):
        temp = self.head
        if self.head == None:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next =  new_node
            
    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            
        else:
            p =1
            while p!= pos-1:
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
            
            
    def delete(self,value):
        temp = self.head
        if temp == None:
            print("Value isnt present")
            return 
        
        if temp.data == value:
            self.head = self.head.next
            return
    
        else:
            while temp and temp.data!=value:
                prev = temp
                temp = temp.next
                if temp == None:
                    print("Value isnt present")
                    return
            prev.next = temp.next
            temp = None
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    
          
          
          
l = SLL()
n1 = Node(10)
n2 = Node(20)

print("Appended list:")
l.append(n1)
l.append(n2)
l.display()

print("Insert :")
l.insert(Node(30),2)
l.display()

print("Deleted :")
l.delete(30)
l.display()

        