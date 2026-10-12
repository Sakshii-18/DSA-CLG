class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    
class SLL:
    def __init__(self):
         self.head = None
         
    def count_nodes(self):
            curr = self.head
            count = 0
    
            while curr:
                count +=1
                curr = curr.next
        
            return count
