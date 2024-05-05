stack = []
new_stack = []
cs_stack = []
class Node:
    def __init__(self, value, child_number):
        self.value = value
        self.left = None
        self.right = None
        self.child_number = child_number

class STNode:
    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

class CS:
    def __init__(self, index =0):
        self.elements = []
        self.index =index


class CSNode:
    def __init__(self, top, bottom, node):
        self.top = top
        self.bottom = bottom
        self.node = node
        self.value = node.value

def print_tree(node, N=0):
    if node is None:
        return

    # Deal with the node
    print(f'{"."*N}{node.value}')

    # Recur on left subtree
    print_tree(node.left, N+1)

    # Recur on right subtree
    print_tree(node.right,N)


def find_parent(root, child_node):
    if root is None:
        return None
    if root.right == child_node:
        return root
    left_parent = find_parent(root.left, child_node)
    if left_parent:
        return left_parent
    return find_parent(root.right, child_node)


def pre_order_traverse(node):
    special_values = ['let' ,'where', 'fcn_form', 'tau', 'lambda', 'within']
    if node is None:
        return
    
    # Deal with the node
    if node.value in special_values:
        new_stack.append(node)
   
    # Recur on left subtree
    pre_order_traverse(node.left)

    # Recur on right subtree
    pre_order_traverse(node.right)


def print_st(node,stNode,  N=0):
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


def generate_cs(node, current_cs=None):
    if node is None:
        return

    # Deal with the node
    if current_cs is None:
        current_cs = CS()

    if node.value == 'lambda':
        top = node.left
        newNode = STNode(top.value)
        newIndex = current_cs.index + 1
        csNode = CSNode(newNode, newIndex, node)
        current_cs.elements.append(csNode)
        cs_stack.append(current_cs)
        print('current cs index', current_cs.index, [ele.value for ele in current_cs.elements])

        current_cs = CS(index=newIndex)
        node.left = node.left.right

    else:
        current_cs.elements.append(node)
        print('current cs index', current_cs.index, [ele.value for ele in current_cs.elements])

        

    generate_cs(node.left, current_cs)
    if node.value == 'lambda':
        current_cs = cs_stack[-2]
        # Recur on right subtree
        generate_cs(node.right, current_cs)
    else:
        generate_cs(node.right, current_cs)
    
    