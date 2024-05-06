import string 
from tree_build import BT, print_tree,stack, print_tree_postorder, Node, pre_order_traverse, new_stack, STNode, find_parent, generate_cs, cs_stack, ctr_structures, CSNode


import re

next_token = None

digits = []
strings = []
identifiers = []
operators = []
input = []
keywords = ['fn', 'where', 'let', 'aug', 'within', 'in', 'rec', 'eq', 'gr', 'ge',
            'ls', 'le', 'ne', 'or', '@', 'not', '&', 'true', 'false', 'nil', 'dummy', 'and', '|']


class Env:
    def __init__(self, value=None, variable=None, index=0, parent_env = None):
        self.value = value
        self.variable = variable
        self.index = index
        self.child_env = []
        self.parent_env = parent_env




def read(token):
    global input
    global next_token

    if input[0] == token:
        input = input[1:]
        if len(input) != 0:
            next_token = input[0]
        else:
            next_token = None
    # else:
    #     print('Error')
    #     next_token = None


def E():
    global next_token
    global input
    if next_token == None:
        next_token = input[0]
        E()


    elif next_token == 'let':
        read('let')
        D()
        read('in')
        E()
        BT('let', 2)

    elif next_token == 'fn':
        read('fn')
        Vb()
        N = 1
        while next_token in identifiers or next_token == '(':
            Vb()
            N += 1
        read('.')
        E()
        BT('lambda', N+1)
    else:
        Ew()


def D():
    global next_token
    Da()
    if next_token == 'within':
        read('within')
        D()
        BT('within', 2)


def Da():
    global next_token
    Dr()
    if next_token == 'and':
        read('and')
        Dr()
        N = 1
        while next_token == 'and':
            read('and')
            Dr()
            N += 1
        BT('and', N+1)


def Dr():
    global next_token
    if next_token == 'rec':
        read('rec')
        Db()
        BT('rec', 1)
    else:
        Db()


def Db():
    global next_token
    if next_token in identifiers:
        if input[1] == ',':
            Vl()
            read('=')
            BT('=', 2)
            E()
        elif input[1] == '=':
            BT(f'<ID:{next_token}>', 0)
            read(next_token)
            read('=')
            E()
            BT('=', 2)


        elif input[1] in identifiers or input[1] == '(':
            BT(f'<ID:{next_token}>', 0)
            read(next_token)
            N = 1
            Vb()
            N += 1
            while next_token in identifiers or next_token == '(':
                Vb()
                N += 1
            read('=')
            E()
            BT('fcn_form', N+1)
        
        
    elif next_token == '(':
        read('(')
        D()
        read(')')


def Vb():
    global next_token
    if next_token in identifiers:
        BT(f'<ID:{next_token}>', 0)
        read(next_token)
    elif next_token == '(':
        read(next_token)
        if next_token in identifiers:
            Vl()
            read(')')
        elif next_token == ')':
            read(next_token)
            BT('()', 0)


def Vl():
    global next_token
    if next_token in identifiers:
        BT(f'<ID:{next_token}>', 0)
        read(next_token)
        N = 1
        while next_token == ',':
            read(next_token)
            if next_token in identifiers:
                BT(f'<ID:{next_token}>', 0)
                read(next_token)
                N += 1
        if N != 1:
            BT(',', N)


def Ew():
    global next_token
    T()
    if next_token == 'where':
        read(next_token)
        Dr()
        BT('where', 2)
    


def T():
    global next_token
    Ta()

    N = 1
    if next_token == ',':
        read(next_token)
        Ta()
        N += 1
        while next_token == ',':
            read(next_token)
            Ta()
            N += 1
        BT('tau', N)


def Ta():
    global next_token
    Tc()
    
    while next_token == 'aug':
        read(next_token)
        Tc()
        BT('aug', 2)


def Tc():
    global next_token
    B()

    if next_token == '->':
        read('->')
        Tc()
        read('|')
        Tc()
        BT('->', 3)


def B():
    global next_token
    Bt()

    while next_token == 'or':
        read(next_token)
        Bt()
        BT('or', 2)


def Bt():
    global next_token
    Bs()
    while next_token == '&':
        read(next_token)
        Bs()
        BT('&', 2)


def Bs():
    global next_token
    if next_token == 'not':
        read(next_token)
        Bp()
        BT('not', 1)
    else:
        Bp()
        


def Bp():
    global next_token
    A()
    if next_token == 'gr' or next_token == '>':
        read(next_token)
        A()
        BT('gr', 2)
    elif next_token == 'ge' or next_token == '>=':
        read(next_token)
        A()
        BT('ge', 2)
    elif next_token == 'ls' or next_token == '<':
        read(next_token)
        A()
        BT('ls', 2)
    elif next_token == 'le' or next_token == '<=':
        read(next_token)
        A()
        BT('le', 2)
    elif next_token == 'eq':
        read(next_token)
        A()
        BT('eq', 2)
    elif next_token == 'ne':
        read(next_token)
        A()
        BT('ne', 2)


def A():
    global next_token
    if next_token == '+':
        read(next_token)
        At()

    elif next_token == '-':
        read(next_token)
        At()
        BT('neg', 1)
    
    At()
    while next_token == '+' or next_token == '-':
        sign = next_token
        read(next_token)
        At()
        BT(sign, 2)


def At():
    global next_token
    Af()
    while next_token in ['*', '/']:
        temp_token = next_token
        print('next token is',next_token)
        read(next_token)
        Af()
        BT(temp_token, 2)
        # Output code for performing the operation op


def Af():
    global next_token
    Ap()
    while next_token == '**':
        read('**')
        Af()
        BT('**', 2)
        # Output code for performing the operation '**'


def Ap():
    global next_token
    R()
    while next_token == "@":
        read(next_token)
        if next_token in identifiers:
            BT(f'<ID:{next_token}>', 0)
            read(next_token)
            R()
            BT('@', 2)
        else:
            print('Invalid')


def R():
    global next_token

    Rn()
    while next_token in identifiers or next_token in digits or next_token in strings or next_token in ['true', 'false', 'nil', 'dummy', '(']:
        Rn()
        BT('gamma', 2)


def Rn():
    global next_token

    if next_token in identifiers or next_token in digits or next_token in strings:
        if next_token in identifiers:
            BT(f'<ID:{next_token}>', 0)
            read(next_token)

        elif next_token in digits:
            BT(f'<INT:{next_token}>', 0)
            read(next_token)

    elif next_token in ['true', 'false', 'nil', 'dummy']:
        read(next_token)
        BT(next_token, 0)
    elif next_token == '(':
        read('(')
        E()
        read(')')
    


with open("a.txt", "r") as file:
    file_content = file.read()
    print(file_content)

letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punction = [')', '(', ';', ',']
operator_symbol = ['+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=',
                   '~', '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?']
lst = []
space = [' ', '\t', '\n']
digits = []
strings = []

a = 0
identifiers = []
operators = []
input = []
while (a < len(file_content)):
    str = ""
    token = ""
    if (file_content[a] == '"' or file_content[a] == "'"):
        token = "<String>"
        t = 0
        while (a < len(file_content) and (file_content[a] in punction or file_content[a] in space or file_content[a] == '\\' or file_content[a] == '\"' or file_content[a] in letter or file_content[a] in digit or file_content[a] in operator_symbol)):
            str += file_content[a]
            a += 1
            if (file_content[a] == '"'):
                str += file_content[a]
                a += 1
                break
    elif (file_content[a] in letter):
        token = "<Identifier>"
        while (a < len(file_content) and (file_content[a] in letter or file_content[a] in digit or file_content[a] == '_')):
            str += file_content[a]
            a += 1
    elif (file_content[a] in space):
        token = "<DELETE>"
        while (a < len(file_content) and file_content[a] in space):
            str += file_content[a]
            a += 1
    elif (file_content[a] in punction):
        str = file_content[a]
        token = file_content[a]
        a += 1
    elif (file_content[a] in operator_symbol):
        token = "<OPERATOR>"
        while (a < len(file_content) and file_content[a] in operator_symbol):
            str += file_content[a]
            a += 1
    elif (file_content[a] in digit):
        token = "<DIGIT>"
        while (a < len(file_content) and file_content[a] in digit):
            str += file_content[a]
            a += 1

    print(repr(str), "=>", token)

    if str not in keywords:
        if token == '<Identifier>':
            identifiers.append(str)
        elif token == '<String>':
            strings.append(str)
        elif token == '<OPERATOR>':
            operators.append(str)
        elif token == '<DIGIT>':
            digits.append(str)

    if token != '<DELETE>':
        input.append(str)


def std_let(root_node: Node):
    root_node.value = 'gamma'
    root_node.left.value = 'lambda'
    exchange_node1 = root_node.left.right
    exchange_node2 = root_node.left.left.right
    root_node.left.left.right = exchange_node1
    root_node.left.right = exchange_node2


def std_where(root_node):
    node1 = root_node.left
    node2 = node1.right
    node3 = node2.left
    node4 = node3.right
    node2.right = node4
    node1.right = None
    root_node.left = node2
    node3.right = node1
    root_node.value = 'gamma'
    node2.value = 'lambda'


def std_fcn_form(root_node):
    root_node.value = '='
    vari_node = root_node.left.right
    f_node = root_node.left
    newNode = STNode('lambda')
    first_child = f_node.right
    f_node.right = newNode
    newNode.left = first_child
    vari_node = first_child
    while '<ID:' in vari_node.right.value:
        newNode = STNode('lambda')
        newNode.left = vari_node.right
        vari_node.right = newNode
        vari_node = newNode.left 


def std_tuple(root_node, root):
    child = root_node.left
    sibling = root_node.right
    children = []
    children.append(child)
    while child.right != None:
        child = child.right
        children.append(child)
    prev_node = None
    print([child.value for child in children])
    for child in children:
        node1 = STNode('gamma')
        node2 = STNode('gamma')
        node3 = STNode('aug')
        node1.left = node2
        node2.left = node3
        node2.right = child
        node2.right.right = None
        if prev_node is None:
            prev_node = node1
            node3.right = STNode('nil')
        else:
            node3.right = prev_node
            prev_node = node1
    prev_node.right = root_node.right
    parent_node = find_parent(root, root_node)
    parent_node.right = prev_node



def std_multi_param(root_node):
    variables_stack = []
    child = root_node.left
    if child is not None and '<ID:' in child.value:
        while '<ID:' in child.right.value:
            sibling = child.right
            newNode = STNode('lambda')
            newNode.right = sibling.right
            sibling.right = None
            newNode.left = sibling
            child.right = newNode
            child = newNode


def std_within(root_node):
    left_child = root_node.left
    right_child = root_node.left.right
    root_node.value = '='
    right_child.value = 'gamma'
    X1 = left_child.left
    X2 = right_child.left
    E1 = X1.right
    E2 = X2.right
    newNode = STNode('lambda')
    newNode.left = X1
    X1.right = E2
    newNode.right = E1
    right_child.left = newNode
    X2.right = right_child
    root_node.left = X2

def extract_number(input_string):
    match = re.search(r'<INT:(-?\d+)>', input_string)
    if match:
        return int(match.group(1))
    else:
        return None



print('\n', '\n')
print(input)

E()
root = stack[0]
pre_order_traverse(root)
new_stack.reverse()
for node in new_stack:
    if node.value == 'let':
        std_let(node)
    elif node.value == 'where':
        std_where(node)
    elif node.value == 'fcn_form':
        std_fcn_form(node)
    elif node.value == 'tau':
        std_tuple(node, root)
    elif node.value == 'lambda':
        std_multi_param(node)
    elif node.value == 'within':
        std_within(node)
    

print_tree(root)
generate_cs(root)
print('\n')

#cse machine
control_stack = []
variable_stack = []
inital_env = Env(index=0)
current_env = inital_env
inital_cs = ctr_structures[0]
control_stack.append(inital_env)
variable_stack.append(inital_env)
control_stack = control_stack + ctr_structures[0].elements

while len(control_stack) != 0:
    last_ele = control_stack[-1]
    if isinstance(last_ele, Node):
        if '<INT:' in last_ele.value:
            variable_stack.insert(0, last_ele)
            control_stack.pop()
        elif '<ID:' in last_ele.value:
            id_value = last_ele.value
            if id_value == current_env.variable.value:
                control_stack.pop()
                variable_stack.insert(0, current_env.value)
            else:
                flag = True
                temp_env = current_env.parent_env
                while flag:
                    if id_value == temp_env.variable.value:
                        control_stack.pop()
                        variable_stack.insert(0, temp_env.value)
                        flag = False
                    temp_env = temp_env.parent_env

        elif last_ele.value == 'neg':
            control_stack.pop()
            
            element = variable_stack.pop(0)
            number = extract_number(element.value)
            new_number = int(number * -1)
            new_node = STNode(f'<INT:{new_number}>')
            variable_stack.insert(0, new_node)
            

       
        elif last_ele.value == 'ls':
            control_stack.pop()

            result = ''
            operand1 = extract_number(variable_stack[0].value)
            
            operand2 = extract_number(variable_stack[1].value)
            if operand1 < operand2:
                result = STNode('true')
            else:
                result = STNode('false')
            variable_stack.pop(0)
            variable_stack.pop(0)
            variable_stack.insert(0, result)
            print(variable_stack[1].value)

        

        elif last_ele.value == 'gamma' and isinstance(variable_stack[0], CSNode):
           
            control_stack.pop()
            variable = variable_stack[0].top
            cs_index = variable_stack[0].bottom
            value = variable_stack[1]
            newEnv = Env(value=value, variable=variable, index = current_env.index+1, parent_env=current_env)
            current_env.child_env.append(newEnv)
            current_env = newEnv
            control_stack.append(current_env)
            variable_stack.pop(0)
            variable_stack.pop(0)
            variable_stack.insert(0, current_env)
            control_stack = control_stack + ctr_structures[cs_index].elements
            
           
        
        elif last_ele.value == '+':
            #print('chamoe', variable_stack.pop(0).value)
            operand_1 = extract_number(variable_stack.pop(0).value)
            operand_2 = extract_number(variable_stack.pop(0).value)
            if last_ele.value == '+':
                control_stack.pop()
                total = operand_1 + operand_2
                total_node = STNode(f'<INT:{total}>')
                variable_stack.insert(0, total_node)


    elif isinstance(last_ele, CSNode):
        
        last_ele.env = current_env
        variable_stack.insert(0, last_ele)
        control_stack.pop()
        
    elif last_ele.value == 'beta':
        control_stack.pop()
        print('last' ,control_stack[-1].index)
        if variable_stack[0].value == 'true':
            control_stack.pop()
            print('reached this point')
            print('cjamod', variable_stack[0].value)
            control_stack = control_stack + control_stack.pop().elements
            variable_stack.pop(0)
            
        elif variable_stack[0].value == 'false':
            control_stack.pop(-2)
            control_stack = control_stack + control_stack.pop().elements
            variable_stack.pop(0)
        
     
    
    elif isinstance(last_ele, Env):
        if last_ele == variable_stack[1]:
            control_stack.pop()
            variable_stack.pop(1)
print(extract_number(variable_stack[0].value))
    
    

    
    
        

