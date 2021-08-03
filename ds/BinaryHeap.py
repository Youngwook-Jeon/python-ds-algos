class Heap:
    def __init__(self, size) -> None:
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

def peek_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]

def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])

def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index / 2)
    if index <= 1:
        return
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "Max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)

def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "The Binary Heap is full."
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value has been successfully inserted"

if __name__ == "__main__":
    new_heap = Heap(5)
    insert_node(new_heap, 4, "Min")
    insert_node(new_heap, 5, "Min")
    insert_node(new_heap, 2, "Min")
    insert_node(new_heap, 1, "Min")
    level_order_traversal(new_heap)