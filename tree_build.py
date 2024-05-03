stack = []
new_stack = []
class Node:
    def __init__(self, value, child_number):
        self.value = value
        self.left = None
        self.right = None
        self.child_number = child_number


def print_tree(node, N=0):
    if node is None:
        return

    # Deal with the node
    print(f'{"."*N}{node.value}')

    # Recur on left subtree
    print_tree(node.left, N+1)

    # Recur on right subtree
    print_tree(node.right,N)

def pre_order_traverse(node ,special_value):
    if node is None:
        return
    
    # Deal with the node
    if node.value == special_value:
        new_stack.append(node)
   
    # Recur on left subtree
    pre_order_traverse(node.left, special_value)

    # Recur on right subtree
    pre_order_traverse(node.right, special_value)


def print_st(node, N=0):
    if node is None:
        return

    # Deal with the node
    print(f'{"."*N}{node.value}')

    # Recur on left subtree
    print_st(node.left, N+1)

    # Recur on right subtree
    print_st(node.right,N)

        

def BT(value, children_number):
    p = None
    for i in range(children_number):
        c = stack.pop()
        c.right = p
        p = c
    newNode = Node(value, children_number)
    newNode.right = None
    newNode.left = p
    stack.append(newNode)


def print_tree_postorder(node):
    if node is None:
        return

    # Recur on left subtree
    print_tree_postorder(node.left)

    # Recur on right subtree
    print_tree_postorder(node.right)

    # Deal with the node
    print(f'{node.value}')
