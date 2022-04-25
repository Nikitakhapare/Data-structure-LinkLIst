class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def insert_at_postion(self,data,pos):
        node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def deletion_at_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def deletion_at_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delection_at_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None


    def display(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end=" ")
                temp = temp.next


if __name__ == '__main__':
    l = LinkedList()
    n1 = Node(10)
    l.head = n1
    n2 = Node(20)
    n1.next = n2
    n3 = Node(40)
    n2.next = n3
    n4 = Node(50)
    n3.next = n4
    # #l.delection_at_position(2)

    # l.insert_at_end(18)
    # # l.insert_begining(25)
    # l.insert_at_postion(35, 3)
    # # l.deletion_at_begining()
    l.display()
