stack = []
new_stack = []
cs_stack = []
ctr_structures = []


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
    def __init__(self, index=0, env=None):
        self.prev_cs = None
        self.elements = []
        self.index = index
        self.prec_cs = None
        self.env = None


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
    print_tree(node.right, N)


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
    special_values = ['let', 'where', 'fcn_form', 'tau', 'lambda', 'within']
    if node is None:
        return

    # Deal with the node
    if node.value in special_values:
        new_stack.append(node)

    # Recur on left subtree
    pre_order_traverse(node.left)

    # Recur on right subtree
    pre_order_traverse(node.right)


def print_st(node, stNode,  N=0):
    if node is None:
        return

    # Deal with the node
    print(f'{"."*N}{node.value}')

    # Recur on left subtree
    print_st(node.left, N+1)

    # Recur on right subtree
    print_st(node.right, N)


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


counter = 0


def generate_cs(node, current_cs=None, num_of_lambdas=0):
    global counter
    if node is None:
        return

    # Deal with the node
    if current_cs is None:
        current_cs = CS()
        ctr_structures.append(current_cs)

    if node.value == 'lambda':
        top = node.left
        # newNode = STNode(top.value)
        newNode = top
        counter += 1
        csNode = CSNode(newNode, counter, node)
        current_cs.elements.append(csNode)
        cs_stack.append(current_cs)
        # print('current cs index', current_cs.index, [ele.value for ele in current_cs.elements])
        current_cs = CS(index=counter)
        ctr_structures.append(current_cs)
        node.left = node.left.right
        generate_cs(csNode.node.left, current_cs=current_cs,
                    num_of_lambdas=counter)

        prev_cs = cs_stack.pop()
        generate_cs(csNode.node.right, current_cs=prev_cs,
                    num_of_lambdas=counter)

    elif node.value == '->':
        current_index = current_cs.index + 1
        then_cs = CS(index=current_cs.index+1)
        else_cs = CS(index=current_cs.index+2)
        ctr_structures.append(then_cs)
        ctr_structures.append(else_cs)
        current_cs.elements.append(then_cs)
        current_cs.elements.append(else_cs)
        beta_node = STNode('beta')
        current_cs.elements.append(beta_node)
        then_node = node.left.right
        else_node = node.left.right.right
        then_node.right = None
        generate_cs(then_node, then_cs, num_of_lambdas)
        print('thencs', [ele.value for ele in then_cs.elements])
        generate_cs(else_node, else_cs, num_of_lambdas)
        print('elsecs', [ele.value for ele in else_cs.elements])
        node.left.right = None
        generate_cs(node.left, current_cs, num_of_lambdas)
        # check condition
    else:
        current_cs.elements.append(node)
        # print('current cs index', current_cs.index, [ele.value for ele in current_cs.elements])

        generate_cs(node.left, current_cs, num_of_lambdas)
        generate_cs(node.right, current_cs, num_of_lambdas)
