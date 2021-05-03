class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class SplayTree:
    def __init__(self):
        self.root = None
    
    # it is exactly the same as BST
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert(data, self.root)
    
    # BST insertion
    def insert(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        else:
            if node.right_child:
                self.insert(data, node.right_child)
            else:
                node.right_child = Node(data, node)
    
    # find a given arbitrary item in the BST
    def find(self, data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left_child
            elif data > node.data:
                node = node.right_child
            else:
                self.splay(node)
                return node.data
    
    # the in-order traversal is the same after rotation
    def right_rotation(self, node):
        temp_left_node = node.left_child
        t = temp_left_node.right_child

        temp_left_node.right_child = node
        node.left_child = t

        if t is not None:
            t.parent = node
        
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_child == node:
            temp_left_node.parent.left_child = temp_left_node
        
        if temp_left_node.parent is not None and temp_left_node.parent.right_child == node:
            temp_left_node.parent.right_child = temp_left_node
        
        if node == self.root:
            self.root = temp_left_node
    
    def rotate_left(self, node):

        temp_right_node = node.right_child
        t = temp_right_node.left_child

        temp_right_node.left_child = node
        node.right_child = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_child == node:
            temp_right_node.parent.left_child = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_child == node:
            temp_right_node.parent.right_child = temp_right_node

        if node == self.root:
            self.root = temp_right_node

