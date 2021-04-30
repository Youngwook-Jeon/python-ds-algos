# capacity of the cache
CAPACITY = 4

# node in the doubly linked list
class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.previous_node = None
        self.next_node = None

class DoublyLinkedList:

    # update the first and last items in O(1)
    def __init__(self):
        self.head = None
        self.tail = None

class LRUCache:
    def __init__(self):
        self.actual_size = 0
        # we store integer node id - Node pairs
        self.dictionary = {}
        self.linked_list = DoublyLinkedList()
    
    # data can be website
    def put(self, id, data):
        # update the node if already exists
        if id in self.dictionary:
            node = self.dictionary[id]
            node.data = data
            # update the node to be the head (cache feature)
            self.update(node)
            return
        
        # the data is not present in the cache so insert
        node = Node(id, data)

        # we have to insert into the cache + set it to be the head node
        if self.actual_size < CAPACITY:
            self.actual_size = self.actual_size + 1
            self.add(node)
        else:
            # the cache is full: we have to remove the last item + insert the new one
            self.remove_tail()
            self.add(node)
    
    # add node to the head of the doubly linked list
    def add(self, node):
        node.next_node = self.linked_list.head
        node.previous_node = None

        # we have to update the previous head: point to the new head
        if self.linked_list.head:
            self.linked_list.head.previous_node = node
        
        # update the head node
        self.linked_list.head = node

        # if there is 1 node in the list: it is the head as well as the tail
        if not self.linked_list.tail:
            self.linked_list.tail = node
        
        # we have to update the dictionary with the node
        self.dictionary[node.id] = node

    # remove last item (least frequently used)
    def remove_tail(self):
        last_node = self.dictionary[self.linked_list.tail.id]

        # new tail node is the prev node
        self.linked_list.tail = self.linked_list.tail.previous_node

        # set the next node to be a null
        if self.linked_list.tail:
            self.linked_list.tail.next_node = None
        
        last_node = None
    
    # get the item with ID id + move to the head because we've visited this item
    def get(self, id):
        if not self.dictionary[id]:
            return None
        
        # the dict contains the item
        node = self.dictionary[id]
        # move to head
        self.update(node)
        return node
    
    # move the given node to the front
    def update(self, node):
        previous_node = node.previous_node
        next_node = node.next_node

        # so it is a middle node(not the head) in the list
        if previous_node:
            previous_node.next_node = next_node
        else: # this is the head node (first node)
            self.linked_list.head = next_node
        
        # so not the last node
        if next_node:
            next_node.previous_node = previous_node
        else: # this is the last node
            self.linked_list.tail = previous_node
        
        # we have to move the node to the front
        self.add(node)
    
    def show(self):
        actual_node = self.linked_list.head

        while actual_node:
            print("%s->" % actual_node.data)
            actual_node = actual_node.next_node

if __name__ == '__main__':
    cache = LRUCache()
    cache.put(0, 'www.google.com')
    cache.put(1, 'www.facebook.com')
    cache.put(2, 'www.apple.com')
    cache.put(3, 'www.udemy.com')
    cache.put(4, 'www.naver.com')
    cache.show()
    print('\n' + cache.get(3).data + '\n')
    print('\n' + cache.get(2).data + '\n')
    cache.put(5, 'www.inflearn.com')
    cache.show()
