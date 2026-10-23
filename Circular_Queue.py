#Linear Queue using linked list 
class Node :
    def __init__(self,value):
        self.data = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.rear = self.front = None
        
    def enqueue(self,new_node):    
        if self.rear == None:
            self.front = self.rear=new_node
        else:
            
            self.rear.next = new_node
            self.rear = new_node
        self.rear.next = self.front #added for circular queue       
                
    def deq(self):
        if self.front: #atleast 1 node is in queue
            temp = self.front 
            
            
            if self.front == self.rear: #only 1 node in queue
                self.front =self.rear =  None 
                print("Queue is empty")
                
            else:
                self.front = self.front.next
                self.rear.next = self.front #added for CQ
            temp = None
       GU 
              
                
    def display(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.front:
                break
        print()
            
l = Queue()
n1 = 10
n2 = 20
print("Enqueue Elements : ")
l.enqueue(Node(n1))
l.enqueue(Node(20))
l.display()

print("Dequeue :")
l.deq()
l.deq()
l.display()