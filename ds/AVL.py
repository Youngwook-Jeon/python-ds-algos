class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def preorder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotate(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balanced(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

# time complexity: O(logN) 
def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)
    
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balanced(root_node)
    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotate(root_node)
    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotate(root_node)
    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        left_rotate(root_node)
    return root_node

new_avl = AVLNode(5)
new_avl = insert_node(new_avl, 10)
new_avl = insert_node(new_avl, 15)
new_avl = insert_node(new_avl, 20)
print(new_avl.data)