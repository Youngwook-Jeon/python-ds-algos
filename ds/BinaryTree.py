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