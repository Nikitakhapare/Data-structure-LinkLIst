class Queue:    
    def __init__(self,limit):
        self.queue=[]
        self.size=limit
    
    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is Empty.")

        else:
            self.queue.pop()

    def display(self):
        print(self.queue)

if __name__=="__main__":
    q1=Queue(10)
    q1.enqueue(3)
    q1.enqueue(6)
    q1.enqueue(9)
    q1.display()
    q1.dequeue()
    q1.display()
