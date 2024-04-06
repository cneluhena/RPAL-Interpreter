import string
import tree_build as tb


next_token = None
tree = []
digits = []
strings = []
identifiers = []
operators = []
input = []
keywords = ['fn', 'where', 'let', 'aug', 'within', 'in', 'rec', 'eq', 'gr', 'ge',
            'ls', 'le', 'ne', 'or', '@', 'not', '&', 'true', 'false', 'nil', 'dummy', 'and', '|']


    
def read(token):
    global input
    global next_token
    if input[0] == token:
        input = input[1:]
        # print('token is read', next_token)
        if len(input) != 0:
            next_token = input[0]


def E():
    global next_token
    print(next_token, 'E()')
    if next_token == None:
        next_token = 'let'
        read('let')
        D()
        read('in')
        E()
        BT('let', 2)

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
    print(next_token, 'D()')

    Da()
    if next_token == 'within':
        read('within')
        D()
        BT('within', 2)


def Da():
    global next_token
    print(next_token, 'Da()')

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
    print(next_token, 'Dr()')
    if next_token == 'rec':
        read('rec')
        Db()
        BT('rec', 1)
    else:
        Db()


def Db():
    global next_token
    print(next_token, 'Db()')
    if next_token in identifiers:
        if input[1] == ',':
            Vl()
            read('=')
            BT('=', 2)
            E()
        elif input[1] == '=':
            BT(f'<ID:{next_token}>', 0)
            print('This is the token', next_token)
            read(next_token)
            read('=')
            E()
            BT('=', 2)


        elif input[1] in identifiers or input[1] == '(':
            BT(f'<ID:{next_token}>', 0)
            read(next_token)
            N = 1
            Vb()
            print(next_token, 'Vb()')
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
    print(next_token, 'Vb()')
    if next_token in identifiers:
        BT(f'<ID:{next_token}>', 0)
        read(next_token)
        print(next_token)
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
    print(next_token, 'Vl()')
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
            print('Number of child', N)
            BT(',', N)


def Ew():
    global next_token
    print(next_token, 'Ew()')
    T()
    print('after T next token', next_token)
    if next_token == 'where':
        read(next_token)
        Dr()
        BT('where', 2)


def T():
    global next_token
    print(next_token, 'T()')
    Ta()
    N = 1
    if next_token == ',':
        read(next_token)
        Ta()
        N += 1
        while next_token == ',':
            print('Reacehd tau')
            read(next_token)
            Ta()
            N += 1
        BT('tau', N)


def Ta():
    global next_token
    print(next_token, 'Ta()')
    Tc()
    while next_token == 'aug':
        read(next_token)
        Tc()
        BT('aug', 2)


def Tc():
    global next_token
    print(next_token, 'Tc()')
    B()
    if next_token == '->':
        read('->')
        Tc()
        read('|')
        Tc()
        BT('->', 3)


def B():
    global next_token
    print(next_token, 'B()')
    Bt()
    while next_token == 'or':
        read(next_token)
        Bt()
        BT('or', 2)


def Bt():
    global next_token
    print(next_token, 'Bt()')
    Bs()
    while next_token == '&':
        read(next_token)
        Bs()
        BT('&', 2)


def Bs():
    global next_token
    print(next_token, 'Bs()')
    if next_token == 'not':
        read(next_token)
        Bp()
        BT('not', 1)
    else:
        Bp()


def Bp():
    global next_token
    print(next_token, 'Bp()')
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
    print(next_token, 'A()')
    if next_token == '+':
        read(next_token)
        At()
    elif next_token == '-':
        read(next_token)
        At()
        BT('neg', 1)
    else:
        At()
        while next_token == '+' or next_token == '-':
            print('Reached this point')
            sign = next_token
            read(next_token)
            At()
            BT(sign, 2)


def At():
    global next_token
    print(next_token, 'At()')
    Af()
    while next_token in ['*', '/']:
        read(next_token)
        Af()
        BT(next_token, 2)
        # Output code for performing the operation op


def Af():
    global next_token
    print(next_token, 'Af()')
    Ap()
    while next_token == '**':
        read('**')
        Af()
        BT('**', 2)
        # Output code for performing the operation '**'


def Ap():
    global next_token
    print(next_token, 'Ap()')
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
    print(next_token, 'R()')

    Rn()
    while next_token in identifiers or next_token in digits or next_token in strings or next_token in ['true', 'false', 'nil', 'dummy', '(']:
        Rn()
        BT('gamma', 2)


def Rn():
    global next_token
    print(next_token, 'Rn()')

    if next_token in identifiers or next_token in digits or next_token in strings:
        if next_token in identifiers:
            BT(f'<ID:{next_token}>', 0)
        elif next_token in digits:
            BT(f'<INT:{next_token}>', 0)
        read(next_token)
        print(input)
    elif next_token in ['true', 'false', 'nil', 'dummy']:
        read(next_token)
        BT(next_token, 0)
    elif next_token == '(':
        read('(')
        print(input)
        E()
        read(')')


def BT(element, no_of_children):
    global tree
    tree.append((element, no_of_children))
    print('BT', element)


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

print(input)
E()
print(tree)
tree.reverse()
print(tree)


root = tb.build_tree(tree)
tb.print_tree(root)
