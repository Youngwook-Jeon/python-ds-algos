class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None

if __name__ == '__main__':
    custom_queue = Queue()
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)
    custom_queue.dequeue()
    print(custom_queue)
    print(custom_queue.is_empty())