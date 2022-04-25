#list

class Stack: 
    def __init__(self, items = []): 
        self.items = list(items) 
        
        
    def push(self,item): 
        self.items = [item] + self.items 
        return self.items 

    def pop(self): 
        self.items = self.items[1:] 
        return self.items 

    def display(self):
        print(self.items)
  
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

if __name__=="__main__":
    stack = Stack([]) 
    stack.push(12) 
    stack.push(6) 
    stack.push(8)
    stack.pop()
    stack.display()
    print(stack.size())
    