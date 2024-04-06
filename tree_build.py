# stack = []
# new_stack = []
# class TreeNode:
#     def __init__(self, element):
#         self.val = element[0]
#         self.child_number = element[1]
#         self.children = []

# def print_tree(root: TreeNode):
#     tree_stack = []
#     tree_stack.append(root)
#     print(root.val)
#     N = 0
#     while len(tree_stack) != 0:
#         if len(tree_stack[-1].children) > 0:
#             N += 1
#             tree_stack.append(tree_stack[-1].children.pop(0))
#             print(f'{"."*N}{tree_stack[-1].val}')
            
#         else:
#             N -= 1
#             tree_stack.pop()


# def insert_rightmost(ele):
#     node = TreeNode(ele)
#     global stack
#     if len(stack) != 0:
#         top_node = stack[-1]
#         print(top_node.val)
#         while top_node.child_number ==0 and len(stack) != 0:
#             stack.pop()
#             new_stack.pop()
#             print('new-stack', new_stack)
#             if len(stack) > 0:
#                 top_node = stack[-1]

#         if node.child_number != 0:
            
#             if len(stack) != 0:
#                 top_node = stack[-1]
#                 top_node.child_number = top_node.child_number -1
#                 top_node.children.insert(0,node)
#                 stack.append(node)
#                 new_stack.append(node.val)
#         else:
#             if len(stack) != 0:
#                 top_node = stack[-1]
#                 top_node.children.insert(0,node)
#                 top_node.child_number = top_node.child_number -1

        
#     else:
#         new_stack.append(node.val)
#         stack.append(node)

#     if len(stack) != 0:
#         temp = stack[-1]
#         print(temp.val)
#         get_child_val(temp.children)


# def get_child_val(array):
#     temp_array = []
#     for ele in array:
#         temp_array.append(ele.val)
#     print(temp_array)
    


# def build_tree(tokens):
#     for ele in tokens:
#         insert_rightmost(ele)
#         print('new stack', new_stack)
#         if len(stack) != 0:
#             print('top node', stack[-1].val)
#             print('top node', stack[-1].child_number)
#             print('\n')
#     return stack[0]
    
    

stack = []
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

