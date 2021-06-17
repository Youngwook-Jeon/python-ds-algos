# space complexity -> av : O(N), worst: O(N)
# insertion -> av: O(logN), worst: O(N)
# deletion -> av: O(logN), worst: O(N)
# search -> av: O(logN), worst: O(N)

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None

class SplayTree:
    def __init__(self):
        self.root = None
    
    # it is exactly the same as BST
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
    
    # BST insertion
    def insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
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
    def splay(self, node):
        # while we hit the root node - this is how we make the node 
        # to be the root node (caches)
        while node.parent is not None:
            # the node is a left or right child of the root
            if node.parent.parent is None:
                if node == node.parent.left_child:
                    self.rotate_right(node.parent)
                else:
                    self.rotate_left(node.parent)
            # doubly left heavy case ZIG-ZIG situation
            elif node == node.parent.left_child and node.parent == node.parent.parent.left_child:
                self.rotate_right(node.parent.parent)
                self.rotate_right(node.parent)
            elif node == node.parent.right_child and node.parent == node.parent.parent.right_child:
                self.rotate_left(node.parent.parent)
                self.rotate_left(node.parent)
            # ZIG-ZAG situation
            elif node == node.parent.left_child and node.parent == node.parent.parent.right_child:
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)
            else:
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)
    
    # the in-order traversal is the same after rotation
    def rotate_right(self, node):
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

if __name__ == '__main__':
    splay_tree = SplayTree()
    splay_tree.insert(10)
    splay_tree.insert(8)
    splay_tree.insert(3)
    splay_tree.insert(7)

    splay_tree.find(7)
    print(splay_tree.root.data)