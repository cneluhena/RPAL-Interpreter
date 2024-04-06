import string
import graphviz
tok_l = []
bt_list = []
with open("BU_AST_OG.txt", "r") as file:
    file_content = file.read()


letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punction = [')', '(', ';', ',']
operator_symbol = ['+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=',
                   '~', '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?']
lst = []
space = [' ', '\t', '\n']
a = 0
while (a < len(file_content)):
    string = ""
    token = ""
    if (file_content[a] == '"'):
        token = "<String>"
        t = 0
        while (a < len(file_content) and (file_content[a] in punction or file_content[a] in space or file_content[a] == '\\' or file_content[a] == '\"' or file_content[a] in letter or file_content[a] in digit or file_content[a] in operator_symbol)):
            string += file_content[a]
            a += 1
            if (file_content[a] == '"'):
                string += file_content[a]
                a += 1
                break
    elif (file_content[a] in letter):
        token = "<Identifier>"
        while (a < len(file_content) and (file_content[a] in letter or file_content[a] in digit or file_content[a] == '_')):
            string += file_content[a]
            a += 1
    elif (file_content[a] in space):
        token = "<DELETE>"
        while (a < len(file_content) and file_content[a] in space):
            string += file_content[a]
            a += 1
    elif (file_content[a] in punction):
        string = file_content[a]
        token = file_content[a]
        a += 1
    elif (file_content[a] in operator_symbol):
        token = "<OPERATOR>"
        while (a < len(file_content) and file_content[a] in operator_symbol):
            string += file_content[a]
            a += 1
    elif (file_content[a] in digit):
        token = "<DIGIT>"
        while (a < len(file_content) and file_content[a] in digit):
            string += file_content[a]
            a += 1

    print(repr(string), "=>", token)
    if (token != '<DELETE>'):
        tok_l.append(string)
stack = tok_l
stack.append('$')
i = 0
next_tok = stack[0]
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(stack)


def S():
    n_b = 1
    if next_tok == 'begin':
        Read('begin')
        S()
        while (next_tok in ['begin', 'id']):
            n_b += 1
            S()
        Read('end')
        BT('block', n_b)
    elif next_tok == 'id':
        Read('id')
        BT('id', 0)
        Read(':=')
        E()
        Read(';')
        BT('assign', 2)
    else:
        print('Error')


def E():
    T()
    while next_tok == '+':
        Read('+')
        T()
        BT('+', 2)


def T():
    P()
    while next_tok == '*':
        Read('*')
        T()
        BT('*', 2)


def P():
    if next_tok == '(':
        Read('(')
        E()
        Read(')')
    else:
        Read('id')
        BT('id', 0)


def Read(next_t):
    global stack, next_tok
    if stack[0] == next_t:
        stack = stack[1:]
        next_tok = stack[0]


def BT(a, b):
    text = 'BT(', a, ',', b, ')'
    print(text)
    bt_list.append((a, b))


S()


class BinaryTreeNode:
    def _init_(self, data):
        self.data = data
        self.children = []


def build_binary_tree(bt_list):
    if not bt_list:
        return None

    root_data = bt_list.pop(0)
    root = BinaryTreeNode(root_data[0])
    if root_data[1] > 0:
        for _ in range(root_data[1]):
            child = build_binary_tree(bt_list)
            if child:
                root.children.append(child)

    return root


def draw_binary_tree(root, dot):
    if root is None:
        return

    dot.node(root.data, root.data)
    for child in root.children:
        if child:
            draw_binary_tree(child, dot)
            dot.edge(root.data, child.data)


new_bt_list = []
for i, (data, count) in enumerate(bt_list):
    if data == 'id':
        new_bt_list.append(('id' + str(i + 1), count))
    else:
        new_bt_list.append((data, count))

# Reverse the new_bt_list
new_bt_list.reverse()
bt_list = new_bt_list
print(new_bt_list)

root = build_binary_tree(bt_list)

dot = graphviz.Digraph()

draw_binary_tree(root, dot)

dot.render('binary_tree_reversed', format='png', cleanup=True)
dot.view()