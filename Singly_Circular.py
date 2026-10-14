class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class SCL :
    def __init__(self):
        self.head = None
        
    def append(self,new_node): #print
        if(self.head == None):
            self.head = new_node
            new_node.next = self.head
            return
            
        else:
            temp = self.head
            while(temp.next != self.head): #changed for SCL
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head #SCL
    
    def insert(self,new_node,pos): #insert
        if pos ==1:
            temp = self.head #changed for SCL v
            while temp.next !=self.head: #find last node
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
                
            temp.next = self.head
            
        else: #insert node from 2nd pos to last 
            p = 1
            temp = self.head
            while (p != pos-1 and temp.next != self.head):#changed for SCL v
                temp = temp.next
                p +=1
            new_node.next = temp.next
            temp.next = new_node
    
    def delete(self,value):
        temp = self.head
        prev = None
        if(temp.data == value): #first node to delete #changed for SCL v
            # self.head = self.head.next
            while temp.next != self.head: #find the last node
                temp = temp.next
            self.head = self.head.next #Chnaged for SCL
            temp.next = self.head
        else:
            while(temp.data != value and temp):
                prev = temp
                temp = temp.next
                if temp ==self.head:
                    print("Value isn't present")
                    return
            prev.next = temp.next
            temp = None
             
    
    def display(self): #changed for SCL
        # print("List elements :")
        temp = self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            print(temp.data , end= " ")
            temp = temp.next
            if temp == self.head:
                break
 
list1 = SCL()           
n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
print()
print("List elements :")
list1.display()

# #insert
list1.insert(Node(77),9)
print()
print("insert List elements :")
list1.display()

#delete
list1.delete(10)
print()
print("deleted List elements :")
list1.display()

