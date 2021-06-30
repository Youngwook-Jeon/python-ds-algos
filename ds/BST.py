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

new_bst = BSTNode(None)
insert_node(new_bst, 70)
insert_node(new_bst, 60)
insert_node(new_bst, 80)
preorder_traversal(new_bst)
search_node(new_bst, 60)