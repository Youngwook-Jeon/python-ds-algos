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

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

new_BT = TreeNode("Drinks")
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
new_BT.left_child = left_child
new_BT.right_child = right_child

def preorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

preorder_traversal(new_BT)

def inorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)

inorder_traversal(new_BT)

def postorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)

postorder_traversal(new_BT)

def levelorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)

levelorder_traversal(new_BT)

def search_BT(root_node, node_value):
    if not root_node:
        return "The BT does not exist"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value.data == node_value:
                return "Success"
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)
        return "Not Found"

print(search_BT(new_BT, "Cola"))

def insert_node_BT(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return "Successfully Inserted"
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return "Successfully Inserted"

def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)
        deepest_node = root.value
        return deepest_node

def delete_deepest_node(root_node, d_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value is d_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is d_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is d_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)

def delete_node_BT(root_node, node):
    if not root_node:
        return "The BT does not exist."
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value.data == node:
                d_node = get_deepest_node(root_node)
                root.value.data = d_node.data
                delete_deepest_node(root_node, d_node)
                return "The node has been successfully deleted."
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)
        return "Failed to delete."

def delete_BT(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BT has been successfully deleted."