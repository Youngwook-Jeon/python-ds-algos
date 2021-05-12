class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def __str__(self) -> str:
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node
    
    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any node in the Queue"
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node
    
    def peek(self):
        if self.is_empty():
            return "There is no any node in the Queue"
        else:
            return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None

if __name__ == '__main__':
    custom_queue = Queue()
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)
    custom_queue.dequeue()
    print(custom_queue)