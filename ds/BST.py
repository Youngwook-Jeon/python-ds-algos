class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
    
def insert_node(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)

def preorder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print("The value is found")
        else:
            search_node(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print("The value is found")
        else:
            search_node(root_node.right_child, node_value)

def min_value_node(bst_node):
    current = bst_node
    while (current.left_child is not None):
        current = current.left_child
    return current

def delete_node(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        temp = min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node

def delete_bst(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BST has been successfully deleted."

new_bst = BSTNode(None)
insert_node(new_bst, 70)
insert_node(new_bst, 60)
insert_node(new_bst, 80)
preorder_traversal(new_bst)
search_node(new_bst, 60)