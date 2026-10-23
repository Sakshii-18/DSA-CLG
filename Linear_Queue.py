#Linear Queue using linked list 
class Node :
    def __init__(self,value):
        self.data = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.rear = self.front = None
        
    def enqueue(self,new_node):
        # temp = self.front
        # if self.rear is None and self.front is None:
        #     self.rear = self.front = new_node
        # else :
        #     while temp:
        #         temp = temp.next
        #         self.rear.next = new_node
        #         self.rear = new_node
        
        if self.rear == None:
            self.front = self.rear=new_node
        else:
            
            self.rear.next = new_node
            self.rear = new_node
                
                
    def deq(self):
        if self.front: #if its not empty
            temp = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            temp = None
        else:
            print("Queue is empty")
              
                
    def display(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next
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
l.deq()
l.display()