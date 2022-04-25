
from inspect import stack


class Stack:
    def __init__(self,limit):
        self.stack=[]
        self.top=0
        self.size=limit

    def push(self,value):
        self.stack.append(value)
        self.top+=1

    def pop(self):
        self.top-=1
        Value=self.stack.pop()
        return Value


    def display(self):
        print(self.stack)


if __name__=="__main__":
    s1=Stack(10)
    s1.push(12)
    s1.push(13)
    s1.push(2)
    s1.pop()
    s1.display()
