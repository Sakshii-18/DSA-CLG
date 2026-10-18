class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class DLL :
    def __init__(self):
        self.head = None
        
    def append(self,new_node):
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp #Changed
            
    def insert(self,new_node,pos): #insert
            if pos ==1:
                new_node.next = self.head
                self.head.prev = new_node #changed
                self.head = new_node
            else:
                p = 1
                temp = self.head
                while (p != pos-1 and temp.next):#when temp.next is none it terminated and adds at last
                    temp = temp.next
                    p +=1
                # if temp.next : #changed for last node if temp.next exist at last then only execute this
                
                new_node.next = temp.next
                temp.next = new_node
                temp.next.prev = new_node #changed cus before updating we have to use it
                new_node.prev = new_node #changed
                
                
        
    
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
 
l = DLL()
n1 = Node(10)
n2 = Node(20)

print("Append List :")
l.append(n1)
l.append(n2)
l.display()
print()

print("Inserted List : ")
l.insert(Node(30),3)
l.insert(Node(40),4)
l.insert(Node(400),10)
l.display()